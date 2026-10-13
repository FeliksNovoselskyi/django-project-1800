from django.db import models
from django.forms.fields import EmailField


# Миша
# Собрать модель Author
# name
class Author(models.Model):
    name = models.CharField(max_length = 250)

# НазваниеМодели.objects - обращение к записям этой модели