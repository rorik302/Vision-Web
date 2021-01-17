from django.contrib.auth.models import AbstractUser
from django.db import models


class Client(AbstractUser):
    """Модель клиента"""

    username = None
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'clients'
