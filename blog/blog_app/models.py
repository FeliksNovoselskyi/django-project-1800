#character
from django.db import models

# models.Model - базовая модель

# Create your models here.
class Post(models.Model):

    title1 = models.CharField(max_length=255)
    content = models.TextField()
    is_publish = models.BooleanField()
    
    def __str__(self):
        return f"{self.id}" 

# Редактирование записи
# 1. получить обхект
# 2. поменять значения полей
# 3. сохранить


# id__gt = 1 - получить записи, чей id больше 1

# gt - greater than
# lt - less than 
# gte - greater than / equal
# lte - less that / equal

# Пишем через __
# gt - >
# lt - <
# gte - >=
# lte - <=

# id__lt


# CharField() - поле для сохранения строки
# TextField() - поле для сохранения большой строки
# IntegerField() - поле для сохранения числа
# BooleanField() - поле для булевых значений (True/False)
