from django.db import models
from django.forms.fields import EmailField
from django.urls import reverse


class Author(models.Model):
    name = models.CharField(max_length = 250)

    def get_absolute_url(self):
        return reverse("author_view", kwargs={"pk": self.pk})
