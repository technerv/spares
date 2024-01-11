from django.contrib import admin
from django.urls import path
from spareapp import views
from .views import *

app_name = 'spareapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('add_item/', views.add_item, name='add_item'),
    path('edit_item/<int:pk>/', views.edit_item, name='edit_item'),
    path('update_item/<int:pk>/', views.update_item, name='update_item'),
    path('delete_item/<int:pk>/', views.delete_item, name='delete_item'),
]
