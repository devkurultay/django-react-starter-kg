from django.contrib import admin
from authtools.admin import StrippedNamedUserAdmin

from .models import User
from .forms import AdminUserChangeForm

# This fixes django-authtool's password reset form bug
# Remove after migration to v2.0
StrippedNamedUserAdmin.form = AdminUserChangeForm

admin.site.register(User, StrippedNamedUserAdmin)
