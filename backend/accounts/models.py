from authtools.models import AbstractEmailUser
from phonenumber_field.modelfields import PhoneNumberField

from django.db import models
from django.utils.translation import ugettext_lazy as _


class User(AbstractEmailUser):
    # dj-rest-auth bug: in its app_settings it imports serializers.py
    # which triggers line #151 where UserMode.EMAIL_FIELD is used
    # In our case, EMAIL_FIELD is useless, but we have to make dj-rest-auth happy
    EMAIL_FIELD = 'email'

    # TODO(murat): Consider moving first_name and last_name to Profile
    first_name = models.CharField(_('First name'), max_length=30, blank=True, null=True)
    last_name = models.CharField(_('Last name'), max_length=30, blank=True, null=True)
    phone = PhoneNumberField(_('Phone number'), blank=True, null=True, unique=True)