from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # index
    path('about', views.about, name='about'), # about
    path('dashboard', views.dashboard, name='dashboard'), # dashboard
    path('login', views.login, name='login'), # login
    path('register', views.register, name='register'), # register
]