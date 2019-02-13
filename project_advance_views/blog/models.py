from django.db.models import CharField
from django.db.models import TextField
from django.db.models import IntegerField
from django.db.models import FileField
from django.utils import timezone
from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(max_length=10000)
    cover_image = models.FileField(upload_to='blog/', null=True, verbose_name="")
    posted_at = models.DateTimeField(default=timezone.now)
    posted_by = models.CharField(max_length=50)
    comment_count = models.IntegerField()
    def __str__(self):
        return self.title