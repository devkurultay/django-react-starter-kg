from authtools.models import AbstractNamedUser

from django.db import models


class User(AbstractNamedUser):
    EMAIL_FIELD = 'email'
