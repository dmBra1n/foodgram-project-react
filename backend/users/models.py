from django.contrib.auth.models import AbstractUser
from django.core.validators import EmailValidator
from django.db import models
from users.validators import validate_username

from foodgram.settings import USER_MAX_FIELD_LENGTH, EMAIL_MAX_LENGTH


class User(AbstractUser):
    """Модель пользователя"""
    email = models.EmailField(
        max_length=EMAIL_MAX_LENGTH,
        unique=True,
        verbose_name='Адрес электронной почты',
        validators=(EmailValidator,)
    )
    username = models.CharField(
        max_length=USER_MAX_FIELD_LENGTH,
        unique=True,
        verbose_name='Логин пользователя',
        validators=(validate_username,)
    )

    first_name = models.CharField(
        blank=False,
        max_length=USER_MAX_FIELD_LENGTH,
        verbose_name='Имя'
    )
    last_name = models.CharField(
        blank=False,
        max_length=USER_MAX_FIELD_LENGTH,
        verbose_name='Фамилия'
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'last_name', 'first_name']

    class Meta:
        ordering = ('id',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username


class Follow(models.Model):
    """Модель подписки на автора рецепта."""
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower',
        verbose_name='Пользователь'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='author',
        verbose_name='Автор'
    )

    class Meta:
        ordering = ('-id',)
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'author'],
                name='unique_follower'
            )
        ]

    def __str__(self):
        return f'{self.user} подписан на {self.author}'
