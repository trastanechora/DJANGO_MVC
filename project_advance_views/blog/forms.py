from django import forms
from .models import Blog

class PostForm(forms.ModelForm):
   class Meta:
       model = Blog
       fields = ('title', 'content', 'cover_image', 'posted_at', 'posted_by', 'comment_count')