from django.shortcuts import render

# Create your views here.


def index(request):
    
    return render(request, 'control_user/pages/index.html')

def blog(request):
    
    return render(request, 'control_user/pages/blog.html')


def about(request):
    
    return render(request, 'control_user/pages/about.html')

def contact(request):
   
    return render(request, 'control_user/pages/contact.html')

def streamings(request):
   
    return render(request, 'control_user/pages/streamings.html')


def restaurant(request):
   
    return render(request, 'control_user/pages/restaurant.html')



def services(request):
    
    return render(request, 'control_user/pages/services.html')

def formation(request):
    
    return render(request, 'control_user/pages/formation.html')
