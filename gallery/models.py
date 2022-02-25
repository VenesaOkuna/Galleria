from django.db import models
from pyuploadcare.dj.models import ImageField

# Create your models here.


class Image(models.Model):
    image = ImageField( blank = False, manual_crop= 60)
    image_name = models.CharField(max_length = 60)
    image_description = models.TextField()
    image_location = models.ForeignKey('Location')
    image_category = models.ForeignKey('Category')



    



