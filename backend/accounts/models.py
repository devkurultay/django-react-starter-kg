from django.db import models
from authtools.models import AbstractEmailUser


class User(AbstractEmailUser):
    telegram_username = models.CharField(
        'Telegram username', max_length=255, blank=True, null=True)
