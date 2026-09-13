from django.contrib import admin
from django.urls import path
from userapp.views import render_reg

urlpatterns = [
    path("reg/", render_reg)
]

