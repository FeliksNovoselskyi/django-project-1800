from django.urls import path
from user_app.views import render_auth, render_reg, render_author_view


urlpatterns = [
    path("auth/", render_auth, name="auth_page"),
    path("reg/", render_reg, name="reg_page"),
    # Данил
    # Собрать динамический адрес на страницу автора
    # render_author_view
    # name="author_view"
    path("author/<int:pk>", render_author_view, name="author_view")
]
