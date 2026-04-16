#dadjokes/ urls.py reyam/CS412

from django.urls import path
from . import views, joke_api

#adding urls one by one

urlpatterns = [
    path('', views.random_view),
    path('random/', views.random_view),
    path('api', views.api_view),
    path('jokes/', views.jokes_list),
    path('api/', joke_api),
    
  path('joke/<int:pk>/', views.joke_detail),
    path('pictures/', views.pictures_list),
    path('picture/<int:pk>/', views.joke_detail),
]