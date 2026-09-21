from django.urls import path
from user_app.views import render_auth, render_reg


urlpatterns = [
    path("auth/", render_auth, name="auth_page"),
    path("reg/", render_reg, name="reg_page")
]
