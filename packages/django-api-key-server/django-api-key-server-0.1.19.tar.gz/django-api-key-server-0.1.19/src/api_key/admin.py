from django.contrib import admin
from django.contrib.admin import register
from .models import ApiKey


@register(ApiKey)
class ApiKeyAdmin(admin.ModelAdmin):
    list_display = ('id', 'api_key', 'api_secret', 'timeout_in', 'description', 'source', 'revoked')
    list_display_links = ('api_key',)
    