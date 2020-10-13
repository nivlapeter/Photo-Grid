from django.db import models
from django.utils import timezone
import datetime as dt

# Create your models here.

class Uploader(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField
    phone_number=models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.first_name

    def save_uploader(self):
        self.save()

    def delete_uploader(self):
        self.delete()

    class Meta:
        ordering = ['first_name']


class Location(models.Model):
     name=models.CharField(max_length=50)
     def __str__(self):
         return self.name
 


class Image(models.Model):
    name=models.CharField(max_length=50)
    uploader=models.ForeignKey(Uploader, on_delete=models.CASCADE)
    location=models.ManyToManyField(Location)
    description=models.TextField()
    pub_date=models.DateTimeField(default=timezone.now)
    #image=models.ImageField(upload_to='',default='gallery-Home')


    def __str__(self):
        return self.name

    @classmethod
    def today_photos(cls):
        today=dt.date.today()
        image=cls.objects.filter(pub_date=today)
        return image
    
    @classmethod
    def days_photos(cls,date):
        image=cls.objects.filter(pub_date=date)
        return image

    @classmethod
    def search_by_name(cls,search_term):
        image=cls.objects.filter(name_icontains=search_term)
        return image

   






