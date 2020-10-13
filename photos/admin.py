from django.contrib import admin
from .models import Uploader,Image,Location

# Register your models here.
    
admin.site.register(Uploader)
admin.site.register(Image)
admin.site.register(Location)