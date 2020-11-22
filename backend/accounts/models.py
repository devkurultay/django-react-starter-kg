from authtools.models import AbstractNamedUser

from django.db import models


class User(AbstractNamedUser):
    # dj-rest-auth bug: in its app_settings it imports serializers.py
    # which triggers line #151 where UserMode.EMAIL_FIELD is used
    # In our case, EMAIL_FIELD is useless, but we have to make dj-rest-auth happy
    EMAIL_FIELD = 'email'