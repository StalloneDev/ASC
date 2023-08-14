from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('blog/', blog, name='blog'),
    path('streamings/', streamings, name='streamings'),
    path('restaurant/', restaurant, name='restaurant'),
    path('services/', services, name='services'),
    path('formation/', formation, name='formation'),
    
   
]



