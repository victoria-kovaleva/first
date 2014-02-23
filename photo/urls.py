#from django.conf.urls.defaults import *
from django.conf.urls import patterns, url, include
from photo.models import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('photo.views',
   (r"^(\d+)/$", "album"),
   (r"^(\d+)/(full|thumbnails|edit)/$", "album"),
   (r"^update/$", "update"),
   (r"^search/$", "search"),
   (r"^image/(\d+)/$", "image"),
   (r"", "main"),
   (r'^admin/', include(admin.site.urls)),
)
