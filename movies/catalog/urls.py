from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name= 'index'),
        path('interstellar', views.interstellar, name= 'interstellar'),
]