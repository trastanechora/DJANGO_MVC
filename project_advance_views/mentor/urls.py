from django.urls import path
from . import views

urlpatterns = [
   path('mentor', views.db_mentor, name='mentor'),
]
