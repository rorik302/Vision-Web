import uuid

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import pre_save


class ClientManager(BaseUserManager):
    def create_user(self, email, password, **kwargs):
        if not email:
            raise ValueError('E-mail должен быть указан')
        if not password:
            raise ValueError('Пароль должен быть указан')

        email = self.normalize_email(email)

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
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = ClientManager()

    class Meta:
        db_table = 'clients'

    @staticmethod
    def pre_save(sender, instance, **kwargs):
        if instance._state.adding is True:
            if instance.is_superuser:
                instance.is_active = True
            else:
                instance.is_active = False
                instance.is_staff = True


pre_save.connect(Client.pre_save, Client)
