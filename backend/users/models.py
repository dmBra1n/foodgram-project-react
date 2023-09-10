from django.contrib.auth.models import AbstractUser
from django.core.validators import EmailValidator
from django.db import models
from users.validators import validate_username


class User(AbstractUser):
    """Модель пользователя"""
    email = models.EmailField(
        max_length=254,
        unique=True,
        verbose_name='Адрес электронной почты',
        validators=(EmailValidator,)
    )
    username = models.CharField(
        max_length=150,
        unique=True,
        verbose_name='Логин пользователя',
        validators=(validate_username,)
    )

    first_name = models.CharField(
        blank=False,
        max_length=150,
        verbose_name='Имя'
    )
    last_name = models.CharField(
        blank=False,
        max_length=150,
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
