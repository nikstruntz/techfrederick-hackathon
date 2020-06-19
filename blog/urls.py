from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.blog, name="blog-home"),
    path('about/', views.about, name="blog-about"),
    path('', views.home, name="home-page")
]
