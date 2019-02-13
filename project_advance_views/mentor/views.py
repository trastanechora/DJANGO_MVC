from django.shortcuts import render
from .models import Mentor

# Create your views here.
def mentor(request):
    return render(request, 'mentor/mentor.html', {})

def db_mentor(request):
   mentor = Mentor.objects.all()
   return render(request, 'mentor/mentor.html', {'mentors': mentor})