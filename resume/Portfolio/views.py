from django.shortcuts import render

# Create your views here.

def Home(request):
    return render(request,"portfolio/index.html")

def Blog(request):
    return render(request,"portfolio/blog.html")

def Bloghm(request):
    return render(request,"portfolio/index-5.html")