from django.db import models
from .utils import get_random_str


class ApiKey(models.Model):
    api_key = models.CharField(max_length=64, unique=True)
    api_secret = models.CharField(max_length=128, default=get_random_str)
    source = models.CharField(default='127,192,172', max_length=256, blank=True,
                              help_text='if not provided, all source ip is allowed')
    expired_at = models.DateTimeField(
        blank=True, null=True, help_text='valid permanently if empty')
    timeout_in = models.PositiveSmallIntegerField(
        default=60, help_text='set 0 to ignore checking')
    description = models.TextField(blank=True)
    revoked = models.BooleanField(default=False)

    class Meta:
        ordering = ('-id',)
