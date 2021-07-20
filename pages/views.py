from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'pages/index.html')

def first(request):
    return render(request, 'pages/first.html')

def second(request):
    return render(request, 'pages/second.html')

def about(request):
    return render(request, 'pages/about.html')

def other(request):
    return render(request, 'pages/other.html')
