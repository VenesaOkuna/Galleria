from django.db import models
from pyuploadcare.dj.models import ImageField

# Create your models here.

class Location(models.Model):
    location_name = models.CharField(max_length = 50)

    @classmethod
    def tag_articles(cls):
        tags = cls.objects.all()
        return tags

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    def update_location(self, update):
        self.location_name = update
        self.save()

    @classmethod
    def get_location_id(cls, id):
        locate = Location.objects.get(pk = id)
        return locate

    def __str__(self):
        return self.location_name




class Image(models.Model):
    image = ImageField( blank = False, manual_crop= 60)
    image_name = models.CharField(max_length = 60)
    image_description = models.TextField()
    image_location = models.ForeignKey('Location')
    image_category = models.ForeignKey('Category')



    



