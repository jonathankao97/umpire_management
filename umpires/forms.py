from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from umpires.models import Auth_code

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_activeCode(value):
    if not Auth_code.objects.filter(code_text__startswith=value):
        raise ValidationError(
            _('%(value)s is not a valid code'),
            params={'value': value},
        )

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    auth_code = forms.CharField(validators=[validate_activeCode], min_length=8, max_length=8, required=True, help_text='Received from Manager/Administrator.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'auth_code' )