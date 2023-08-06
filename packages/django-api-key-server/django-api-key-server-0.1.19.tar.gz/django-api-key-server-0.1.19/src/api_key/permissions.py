from django.db.models import Q
from .models import ApiKey
from rest_framework.permissions import BasePermission
from rest_framework.exceptions import PermissionDenied
from hashlib import md5
from .utils import sort_query_string
from django.utils import timezone
from django.conf import settings
from django.utils.dateparse import parse_datetime
import zoneinfo
from datetime import datetime

def restore_request_sign(url, api_secret):
    """Retrieve Sign from url and api_secret"""
    query_string = url.split('?')[1] if '?' in url else url
    data_string = query_string.split('&sign')[0]
    data = sort_query_string(data_string) + 'api_secret=' + api_secret
    sign = md5(data.encode('utf-8')).hexdigest()
    return sign


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


class CheckSourceIP(BasePermission):
    message = 'Your IP is not allowed'

    def has_permission(self, request, view):
        api_key = request.query_params.get('api_key')
        try:
            app_obj = ApiKey.objects.get(api_key=api_key)
            api_source = app_obj.source
        except ApiKey.DoesNotExist:
            self.message = "api key not found."
            raise PermissionDenied(self.message)

        if not api_source:
            return True

        ip_list = api_source.replace(' ', '').split(',')
        ip = get_client_ip(request)
        return ip.split('.')[0] in ip_list


class CheckApiKeySign(BasePermission):
    message = "api sign incorrect."

    def has_permission(self, request, view):
        api_key = request.query_params.get('api_key')
        query_string = request.META['QUERY_STRING']
        timestamp = request.query_params.get('timestamp')
        sign = request.query_params.get('sign')
        try:
            key = ApiKey.objects.get(api_key=api_key)
            api_secret = key.api_secret
            api_timeout_in = key.timeout_in
            api_expired_at = key.expired_at
        except ApiKey.DoesNotExist:
            self.message = "api key not found."
            raise PermissionDenied(self.message)

        # Check timeout
        if has_timeout(timestamp, api_timeout_in):
            self.message = "api request timeout, please create new timestamp for new request."
            raise PermissionDenied(self.message)

        # Check key expired
        if has_expired(api_expired_at):
            self.message = "API Key and Secret has expired."
            raise PermissionDenied(self.message)

        restored_sign = restore_request_sign(query_string, api_secret)
        if restored_sign == sign:
            return True
        else:
            raise PermissionDenied(self.message)


class CheckApiKeyAuth(BasePermission):
    def has_permission(self, request, view):
        api_key = request.query_params.get('api_key')
        post_secret = request.query_params.get('api_secret')
        try:
            obj = ApiKey.objects.get(Q(api_key=api_key, revoked=False),
                                     Q(expired_at__isnull=True) |
                                     Q(expired_at__gt=timezone.now()))
            api_secret = obj.api_secret
        except ApiKey.DoesNotExist:
            raise PermissionDenied(self.message)

        return post_secret == api_secret


def has_timeout(request_timestamp, timeout_in):
    if timeout_in <= 0:
        return False
    datetime_object = datetime.strptime(request_timestamp, '%Y%m%d%H%M%S')
    now_timestamp = round(timezone.now().timestamp())
    request_timestamp = round(datetime_object.replace(tzinfo=zoneinfo.ZoneInfo(settings.TIME_ZONE)).timestamp())
    interval = now_timestamp - request_timestamp
    return interval > timeout_in


def has_expired(expired_at):
    if expired_at and isinstance(expired_at, datetime):
        now = timezone.now()
        return now > expired_at
    else:
        return False

