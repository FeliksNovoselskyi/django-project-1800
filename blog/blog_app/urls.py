# Импортировать path
from blog_app.views import handle_form, render_form, render_post
from blog_app.views import render_tags
from django.urls import path

urlpatterns = [
    path('posts/<int:pk>', render_post, name='post_view'),
    path('form/', render_form, name = 'form_view'),
    path('request/', handle_form, name='form_request'),
    # Миша Морозов. Создать маршрут для функции render_tags
    path('render_tags/', render_tags, name = 'render_tags')
]
