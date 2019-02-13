from django.db.models import CharField
from django.db.models import TextField
# from django.db.models import ForeignKey
from django.utils import timezone
from django.db import models

# Create your models here.

class Mentee(models.Model):
    name = models.CharField(max_length=255)
    nickname = models.CharField(max_length=50)
    full_name = models.TextField(max_length=255)
    gender = models.CharField(max_length=1)
    telephone = models.TextField(max_length=25)
    mobile = models.TextField(max_length=25)
    address = models.TextField(max_length=255)
    def __str__(self):
        return self.name

class BlogPost(models.Model):
    Created_at = models.DateTimeField(default=timezone.now)
    Updated_at = models.DateTimeField(default=timezone.now)
    Title = models.CharField(max_length=50)
    Content = models.TextField(max_length=255)
    Created_by = models.CharField(max_length=50)
    Posted_by = models.ForeignKey(Mentee, on_delete=models.CASCADE)
    def __str__(self):
        return self.Title
