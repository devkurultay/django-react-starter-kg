from django.db import transaction
from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers
from allauth.utils import email_address_exists
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from allauth.account.utils import user_email
from allauth.account.utils import user_field
from allauth.account import app_settings as allauth_settings

from .models import User


class RegisterUserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255, required=False)
    email = serializers.EmailField(max_length=255)
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    def validate_email(self, email):
        email = get_adapter().clean_email(email)
        if allauth_settings.UNIQUE_EMAIL:
            if email and email_address_exists(email):
                raise serializers.ValidationError(
                    _("A user is already registered with this e-mail address."))
        return email

    def validate_password1(self, password):
        return get_adapter().clean_password(password)

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError(_("The two password fields didn't match."))
        return data

    def get_cleaned_data(self):
        return {
            'name': self.validated_data.get('name', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', '')
        }

    def save_user(self, request, user, form):
        data = form.cleaned_data
        name = data.get('name')
        email = data.get('email')
        user_email(user, email)
        if name:
            user_field(user, 'name', name)
        if 'password1' in data:
            user.set_password(data['password1'])
        else:
            user.set_unusable_password()
        user.save()
        return user

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        self.save_user(request, user, self)
        setup_user_email(request, user, [])
        return user


class NamedEmailUserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'pk',
            'email',
            'name',
        )
        read_only_fields = ('pk',)