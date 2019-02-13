from django.shortcuts import render
from .models import Mentee

# Create your views here.
def mentee(request):
    return render(request, 'mentee/mentee.html', {})

def db_mentee(request):
   mentee = Mentee.objects.all()
   return render(request, 'mentee/mentee.html', {'mentees': mentee})