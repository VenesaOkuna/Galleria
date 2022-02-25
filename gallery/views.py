from django.http  import HttpResponse, Http404
from django.shortcuts import render, redirect
from .models import Image, Location, Category



# Create your views here.

def gallery(request):
    images = Image.get_all_images()
    locations = Location.objects.all()
    title = 'Galleria'

    return render(request, 'index.html', {'title':title, 'images':images, 'locations':locations})

#search for image functionality
def search_image(request):
    title = 'Search'
    categories = Category.objects.all()
    locations = Location.objects.all()
    if 'image_category' in request.GET and request.GET['image_category']:
        search_term = request.GET.get('image_category')
        found_results = Image.search_by_category(search_term)
        message = f"{search_term}"
        print(search_term)
        print(found_results)

        return render(request, 'search.html',{'title':title,'images': found_results, 'message': message, 'categories': categories, "locations":locations})
    else:
        message = 'No searches yet'
        return render(request, 'search.html',{"message": message})