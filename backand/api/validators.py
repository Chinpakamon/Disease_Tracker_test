import re

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

user = re.compile(r'^[\w.@+-]+\Z')
# Password example: Password123, myPassword_2022, Secure_Passw0rd
password = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z0-9_]+')


def username_validator(value):
    if not user.match(value):
        raise ValidationError(
            _('%(value)s is invalid username!'),
            params={'value': value})
    return value


def password_validator(value):
    if not password.match(value):
        raise ValidationError(
            _('%(value) is invalid password!'),
            params={'value': value}
        )
    return value
