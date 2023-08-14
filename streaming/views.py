from django.shortcuts import render

# Create your views here.


def index(request):
   
    return render(request, 'streaming/pages/index.html')

def blog(request):
    
    return render(request, 'streaming/pages/blog.html')


def category(request):
    
    return render(request, 'streaming/pages/category.html')


def about(request):
    
    return render(request, 'streaming/pages/about.html')

def contact(request):
    
    return render(request, 'streaming/pages/contact.html')

def playlist(request):
    
    return render(request, 'streaming/pages/playlist.html')

def artist(request):
    
    return render(request, 'streaming/pages/artist.html')
