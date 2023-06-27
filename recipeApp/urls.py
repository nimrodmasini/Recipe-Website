from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('create/', views.create_recipe, name = 'create'),
    path('view/', views.view_recipe, name = 'view'),
]