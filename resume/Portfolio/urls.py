from django.urls import path
from . import views

urlpatterns = [
    path("", views.Home),
    path("blog.html/", views.Blog),
    path("blog.html/index-5.html/",views.Bloghm),
    path("blog.html/index-5.html/blog.html/",views.Bloghm),
    path("blog.html/index-5.html/blog.html/blog.html",views.Blog),
    path("blog.html/index-5.html/blog.html/index-5.html",views.Bloghm),
    path("blog.html/index-5.html/blog.html/index-5.html#",views.Bloghm),
]