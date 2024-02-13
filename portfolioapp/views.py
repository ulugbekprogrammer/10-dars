from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html', context={})

def about(request):
    return render(request, 'about.html', context={})

def resume(request):
    return render(request, 'resume.html', context={})

def portfolio(request):
    return render(request, 'portfolio.html', context={})

def blog(request):
    return render(request, 'blog.html', context={})

def contact(request):
    return render(request, 'contact.html', context={})