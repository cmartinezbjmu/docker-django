from django.contrib.auth.models import User
from django.db import models
from datetime import datetime

# Create your models here.

class APP(models.Model):
    APP_TYPES = (
        ('1', 'Aplicación WEB'),
        ('2', 'APP Android'),
        ('3', 'APP iOS'),
    )
    U_ID = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usuario')
    A_NAME = models.CharField('Nombre', max_length=200)
    AT_ID = models.CharField('Tipo de aplicación', max_length=1, choices=APP_TYPES)
    A_DESCRIPTION = models.TextField('Descripción')
    A_PATH_TO_BINARY = models.CharField('Link', max_length=200)


    class Meta:
        ordering = ['-id']
        verbose_name = 'Aplicación'
        verbose_name_plural = 'Aplicaciones'

class APP_TESTING_ROUND(models.Model):
    ATR_NAME = models.CharField('Nombre', max_length=200)
    ATR_PROGRAMMED_EXECUTION = models.DateTimeField('Fecha', default=datetime.now)
    ATR_ID = models.ForeignKey(APP, on_delete=models.CASCADE, related_name='ATR_APP')


    class Meta:
        ordering = ['-id']
        verbose_name = 'App Testing Round'
        verbose_name_plural = 'App Testing Rounds'


class E2E_TEST(models.Model):
    E2ET_PATH_TO_SCRIPT = models.CharField('Path del script', max_length=200)
    E2ET_HEADLESS = models.BooleanField('')
    ATR_ID = models.ForeignKey(APP_TESTING_ROUND, on_delete=models.CASCADE, related_name='E2E_ATR')


    class Meta:
        ordering = ['-id']
        verbose_name = 'E2E Test'
        verbose_name_plural = 'E2E Tests'

class RANDOM_TEST(models.Model):
    RT_NUM_EVENTS = models.PositiveIntegerField('Número de eventos')
    RT_DURATION = models.DateTimeField('Fecha', default=datetime.now)
    ATR_ID = models.ForeignKey(APP_TESTING_ROUND, on_delete=models.CASCADE, related_name='RT_ATR')


    class Meta:
        ordering = ['-id']
        verbose_name = 'Random Test'
        verbose_name_plural = 'Random Tests'