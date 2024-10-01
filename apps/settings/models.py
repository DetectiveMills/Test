from django.db import models

# Create your models here.

class Settings(models.Model):
    logotip = models.ImageField(
        upload_to='logotip/'
    )
    title_1 = models.CharField(
        max_length=155,
        verbose_name='Заголовок 1'
    )
    title_2 = models.CharField(
        max_length=155,
        verbose_name='Заголовок 2'
    )

class Collections(models.Model):
    banner = models.ImageField(
        upload_to='logotip/'
    )
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовок'
    )

class Sellers(models.Model):
    banner = models.ImageField(
        upload_to='logotip/'
    )
    title = models.CharField(
        max_length=155,
        verbose_name='Ник'
    )
    money = models.ImageField(
        max_length=155,
        verbose_name='Деньги'
    )