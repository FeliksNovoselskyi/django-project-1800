from django.db import models
from django.urls import reverse
from user_app.models import Author


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    is_publish = models.BooleanField(default=False)
    
    author = models.ForeignKey(Author,null= True,on_delete=models.CASCADE)
    
    def get_absolute_url(self):
        return reverse("post_view", kwargs={"pk": self.pk})
