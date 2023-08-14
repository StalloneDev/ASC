from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='streaming'),
    path('blog/', blog, name='blog'),
    path('contact/', contact, name='contact'),
    path('category/', category, name='category'),
    path('artist/', artist, name='artist'),
    path('playlist/', playlist, name='playlist'),
    
   
]