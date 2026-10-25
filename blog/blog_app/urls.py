# Импортировать path
from blog_app.views import render_post
from django.urls import path

from blog_app.views import render_form, handle_form_request


urlpatterns = [
    path('posts/<int:pk>', render_post, name='post_view'),
    path('form/', render_form, name = 'form_view'),
    path('form_request/', handle_form_request, name='form_request')
]
