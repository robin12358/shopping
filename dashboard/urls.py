from django.urls import path
from . import views
urlpatterns = [
    path('', views.index,name="admin"),
    path('home', views.index,name="adhome"),
]