from django.contrib.auth.forms import (
    UserChangeForm as DjangoUserChangeForm
)

from authtools.forms import UserChangeForm


class AdminUserChangeForm(UserChangeForm):
    """Fixes password reset form bug"""

    def __init__(self, *args, **kwargs):
        super(AdminUserChangeForm, self).__init__(*args, **kwargs)
        if not self.fields['password'].help_text:
            self.fields['password'].help_text = \
                DjangoUserChangeForm.base_fields['password'].help_text.format('../password')