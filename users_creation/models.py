from django.db import models
from django.contrib.auth.models import User


class UserCreation(User):
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
    ADMIN = 1
    PREMIUM = 2
    SIMPLE = 3
    USER_TYPE = (
        (ADMIN, 'ADMIN'),
        (PREMIUM, 'PREMIUM'),
        (SIMPLE, 'SIMPLE')
    )
    MALE = 1
    FEMALE = 2
    OTHER = 3
    GENDER_TYPE = (
        (MALE, 'MALE'),
        (FEMALE, 'FEMALE'),
        (OTHER, 'OTHER')
    )
    user_type = models.IntegerField(choices=USER_TYPE, verbose_name='Уровень пользователя', default=SIMPLE)
    phone_number = models.CharField('phone_number', max_length=100)
    gender = models.IntegerField(choices=GENDER_TYPE, verbose_name='Неопределенный')
    education = models.CharField(max_length=200)
    country = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
