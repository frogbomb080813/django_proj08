from django.shortcuts import render

def index(request):
    return render(request, "videosite/home.html")

# Create your views here.
