from django.urls import path
from . import views

urlpatterns = [
   path('blog', views.db_blog, name='blog'),
   path('input_new', views.model_form_upload, name="post_new"),
   path('post_description/<int:requested_id>', views.get_page_description, name="post_description")
]