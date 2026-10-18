from django.db import models
from django.forms.fields import EmailField
from django.urls import reverse

# Миша
# Собрать модель Author
# name
class Author(models.Model):
    name = models.CharField(max_length = 250)
    
    # Прописать метод get_absolute_url(), настроив ссылку на страницу автора
    def get_absolute_url(self):
        return reverse("author_view", kwargs={"pk": self.pk})

# author_view

# НазваниеМодели.objects - обращение к записям этой модели