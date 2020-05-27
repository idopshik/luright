from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='luapp-home'),
    path('about/', views.about, name='luapp-about'),
]
