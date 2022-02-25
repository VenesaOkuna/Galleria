from django.http  import HttpResponse, Http404
from django.shortcuts import render, redirect
from .models import Image, Location, Category



# Create your views here.

def gallery(request):
    images = Image.get_all_images()
    locations = Location.objects.all()
    title = 'Galleria'

    return render(request, 'index.html', {'title':title, 'images':images, 'locations':locations})