from django.urls import path
from . import views

urlpatterns = [
    path('', views.dojo_info, name='dojo_info'),
]