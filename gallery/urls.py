from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.gallery, name = 'gallery'),
    path('search/', views.search_image, name = 'search_image'),
    path('image/<image_id>/', views.Picture.as_view(),name='image'),
    path('image/<category_name>/<image_id>/)',views.single,name = 'single'),
    path('location/<image_location>/)', views.location_filter, name='location_filter')
]

