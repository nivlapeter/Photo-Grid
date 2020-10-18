from django.conf.urls.static import static
from django.conf.urls import url
from django.urls import path
from django.conf import settings
from . import views


urlpatterns = [
    path('',views.photos_today, name = 'gallery-Home'),
    path('search/',views.search_results, name='search_results'),
    path('archives/<past_date>/',views.past_days_photos, name = 'past-Photos')
]