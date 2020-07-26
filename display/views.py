from django.shortcuts import render
from .models import Profile

# Create your views here.
def home(request):
    profile = Profile.objects.all()
    return render(request, 'home.html', {'profile': profile})