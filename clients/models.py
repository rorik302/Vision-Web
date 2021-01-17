from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


class ClientManager(BaseUserManager):
    def create_user(self, email, password, **kwargs):
        if not email:
            raise ValueError('E-mail должен быть указан')
        if not password:
            raise ValueError('Пароль должен быть указан')

        email = self.normalize_email(email)
        kwargs.setdefault('is_active', False)

        client = self.model(email=email, **kwargs)
        client.set_password(password)
        client.save()
        return client

    def create_superuser(self, email, password, **kwargs):
        kwargs.setdefault('is_superuser', True)
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_active', True)

        if kwargs.get('is_staff') is not True:
            raise ValueError('Значение is_staff должно быть True')
        if kwargs.get('is_superuser') is not True:
            raise ValueError('Значение is_superuser должно быть True')
        return self.create_user(email, password, **kwargs)


class Client(AbstractUser):
    """Модель клиента"""

    username = None
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = ClientManager()

    class Meta:
        db_table = 'clients'
