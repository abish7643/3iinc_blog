from django.urls import path
from  . import views


urlpatterns = [
    path('', views.home, name="3iinc-home"),
    path('about/', views.about, name="3iinc-about"),        
]

