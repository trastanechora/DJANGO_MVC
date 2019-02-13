from django.urls import path
from . import views

urlpatterns = [
   # path('mentee', views.mentee, name='mentee'),
   path('mentee', views.db_mentee, name='mentee'),
]
