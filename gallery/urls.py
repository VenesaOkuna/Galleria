from django.urls import path
from . import views

urlpatterns = [
    path('', views.gallery, name = 'gallery'),
    path('search/', views.search_image, name = 'search_image'),
    path('^image/(?P<category_name>\w+)/(?P<image_id>\d+)',views.single,name = 'single')
]
