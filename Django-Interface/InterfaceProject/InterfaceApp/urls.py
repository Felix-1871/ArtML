from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('mondrian.html', views.mondrian, name='mondrian'),
    path('gogh.html', views.gogh, name='gogh'),
    path('munch.html', views.munch, name='munch'),
]