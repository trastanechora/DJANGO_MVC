from django.shortcuts import render
from .models import Blog
from .forms import PostForm
from django.shortcuts import redirect
from django.shortcuts import get_list_or_404, get_object_or_404

# Create your views here.
def blog(request):
    return render(request, 'blog/blog.html', {})

def db_blog(request):
   blog = Blog.objects.all()
   return render(request, 'blog/blog.html', {'blogs': blog})

def model_form_upload(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'blog/post_new.html', {
        'form': form
    })

def get_page_description(request, requested_id):
    content = Blog.objects.get(pk=requested_id)
    return render(request, 'blog/blog_description.html', {'content': content})