from django.contrib.auth.models import AbstractUser
from django.db import models


class Roles(models.TextChoices):
    ADMINISTRATOR = 'admin'
    MODERATOR = 'moderator'
    USER = 'user'


class User(AbstractUser):
    email = models.EmailField('Почтовый адрес', unique=True, help_text='Введите почтовый адрес')
    bio = models.TextField('Биография', max_length=500, blank=True, help_text='Заполните данные о себе')
    role = models.CharField(
        'Права доступа',
        max_length=32,
        choices=Roles.choices,
        default=Roles.USER,
        help_text='Выберите права доступа',
    )

    def __str__(self):
        return self.username[0:30]

    @property
    def is_admin(self):
        return self.role == Roles.ADMINISTRATOR or self.is_superuser

    @property
    def is_moderator(self):
        return self.role == Roles.MODERATOR

    @property
    def is_user(self):
        return self.role == Roles.USER

    class Meta:
        ordering = ['username']
