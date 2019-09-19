from django.db import models

# Create your models here.

class App(models.Model):
    APP_TYPES = (
        ('1', 'Aplicación WEB'),
        ('2', 'APP Android'),
        ('3', 'APP iOS'),
    )
    name = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)
    path_to_binary = models.CharField(max_length=200)
    user_id = models.IntegerField()
    app_type_id = models.CharField(max_length=1, choices=APP_TYPES)

    class Meta:
        ordering = ['-id']
