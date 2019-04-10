from django.urls import path
from . import views
urlpatterns = [
    path('', views.dashboard,name="dashboard"),
    path('login',views.adlogin,name="adlogin"),
    path('logout',views.adlogout,name="adlogout"),
    path('home', views.index,name="adhome"),
    path('profile',views.profile,name="profile"),
]