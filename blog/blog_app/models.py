from django.db import models
from django.urls import reverse
from user_app.models import Author


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    is_publish = models.BooleanField(default=False)

    author = models.ForeignKey(
        Author,
        on_delete = models.CASCADE,
        null = True # разрешаем пустое поле
    )

    def get_absolute_url(self):

        return reverse("post_view", kwargs={"pk": self.pk})

# 1. модель
# 2. on_delete - что произойдет при удалении связанной записи
# models.CASCADE - если удалена связанная запись, то и эта будет тоже удалена

# ForeignKey - создается связь One-to-Many