from django.db import models
from django.forms.fields import EmailField

# User

# id
# email - EmailField
# password_hash - CharField

class User(models.Model):
    
    email = models.EmailField()
    password_hash = models.CharField()

# Create your models here.



# CharField() - поле для сохранения строки
# TextField() - поле для сохранения большой строки
# IntegerField() - поле для сохранения числа
# BooleanField() - поле для булевых значений (True/False)
