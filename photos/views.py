from django.shortcuts import render,redirect
from django.http import HttpResponse
import datetime as dt
from django.http import Http404
from .models import Image


# Create your views here.
def photos_today(request):
    date=dt.date.today()
    photos=Image.today_images()
    return render(request, 'all_photos/index.html',{"date":date, "photos":photos})

def past_days_photos(request,past_date):
    try:
        date=dy.datetime.strptime(past_date,'%Y-%m-%d').date()

    except ValueError:
        raise Http404()
        assert False
    if date==dt.date.today():
        return redirect(photos_today)

    photos=Image.days_photos(date)
    return render(request,'all_photos/past-photos.html',{"date":date},{"photos",photos})

def search_results(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term=request.GET.get("image")
        searched_photos=Image.search_by_name(search_term)
        message=f"{search_term}"

        return render(request,'all_photos/search.html',{"message":message},{"image":searched_photos})
    else:
        message="sorry! you haven't searched for any item"
        return render(request,'all_photos/search.html',{"message":message})

def image(request,image_id):
    try:
        image=Image.objects.get(id=image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all_photos/index.html")

