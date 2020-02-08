from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from umpires.models import Umpire
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
    auth_code = forms.CharField(validators=[validate_activeCode], min_length=8, max_length=8, required=True,
                                help_text='Received from Manager/Administrator.')
    class Meta:
        model = Umpire
        fields = ('username', 'name', 'email', 'password1', 'password2', 'auth_code' )