from django.shortcuts import render
from .models import Pics
# Create your views here.

def index(request):
    images = Pics.objects.all()
    context={'images': images}

    return render(request, 'index.html', context)
