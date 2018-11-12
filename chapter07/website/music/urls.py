from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # /music/
    path('', views.index, name='index'),

    # /music/1/
    path('<int:album_id>/', views.detail, name='detail'),

]

