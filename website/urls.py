from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name="home"),
  #path('post-single.html', views.post_single, name="post-single"),
  #path('typography.html', views.typography, name="typography"),
  
]