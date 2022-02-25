from django.urls import path
from . import views

urlpatterns = [
    path('', views.gallery, name = 'gallery'),
    path('search/', views.search_image, name = 'search_image')
]
