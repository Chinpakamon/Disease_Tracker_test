from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxLengthValidator, MinLengthValidator

from .validators import username_validator, password_validator


class User(AbstractUser):
    email = models.EmailField(verbose_name='Email address', max_length=150,
                              unique=True)
    username = models.CharField(verbose_name='Username', max_length=150,
                                unique=True, validators=[username_validator])
    password = models.TextField(verbose_name='Password', max_length=150,
                                validators=[MinLengthValidator(limit_value=8,
                                                               message='The password must be more than 6 characters'),
                                            MaxLengthValidator(limit_value=150,
                                                               message='The password must be less than 15 characters'),
                                            password_validator,
                                            ]
                                )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'password']

    class Meta:
        verbose_name = 'User'

    def __str__(self):
        return self.email
