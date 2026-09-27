#character
from django.db import models

# models.Model - базовая модель

# Create your models here.
class Post(models.Model):

    title1 = models.CharField(max_length=255)
    content = models.TextField()
    is_publish = models.BooleanField()


# создает миграции
# python manage.py makemigrations

# применение миграции
# python manage.py migrate


# CharField() - поле для сохранения строки
# TextField() - поле для сохранения большой строки
# IntegerField() - поле для сохранения числа
# BooleanField() - поле для булевых значений (True/False)
