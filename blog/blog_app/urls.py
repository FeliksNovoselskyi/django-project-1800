from django.urls import path
from blog_app.views import render_post
# Камилла: создать маршрут для функции render_post
# posts/

urlpatterns = [
    path('posts/<int:pk>', render_post, name = 'post')
]

# <> - динамическая часть адреса
# int - тип этой части
# pk - название уникальной части
