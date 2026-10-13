# Импортировать path
from blog_app.views import render_post
from django.urls import path

urlpatterns = [
    path('posts/<int:pk>', render_post, name='post_view')
]
