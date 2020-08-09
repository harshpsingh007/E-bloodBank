from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('',views.mainapp_home,name='main_home'),
    path('contactus',views.contactus,name='contactus'),
    path('aboutus',views.aboutus,name='aboutus'),
    path('donors',views.donors,name='donors'),
    path('donorRegitration',views.donorRegistration,name='donorRegitration'),
    path('donordetails/<int:donorid>/',views.donordetails,name='donordetails'),
    path('search',views.search,name='search'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
