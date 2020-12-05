from django.contrib import admin
from authtools.admin import StrippedUserAdmin

from .models import User
from .forms import AdminUserChangeForm

# This fixes django-authtool's password reset form bug
# Remove after migration to v2.0
StrippedUserAdmin.form = AdminUserChangeForm

class StrippedCustomUserAdmin(StrippedUserAdmin):
    list_display = (
        'is_active', 'email', 'phone',
        'first_name', 'last_name',
        'is_superuser', 'is_staff',)
    list_display_links = ('email', 'phone',)
    search_fields = ('email', 'first_name', 'last_name', 'phone',)

admin.site.register(User, StrippedCustomUserAdmin)