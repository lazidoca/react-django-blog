from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from files.models import Files
from countries.models import Countries

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    profile_img = models.ForeignKey(Files, null=True, blank=True, on_delete=models.CASCADE)
    country = models.ForeignKey(Countries, null=True, blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)


    def __str__(self):
        return self.email