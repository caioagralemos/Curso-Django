from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # index
    path('about', views.about, name='about'), # about
    path('listings', views.listings, name='listings'), # listings
    path('listing', views.listing, name='listing'), # listing
    path('dashboard', views.dashboard, name='dashboard'), # dashboard
    path('login', views.login, name='login'), # login
    path('register', views.register, name='register'), # register
    path('search', views.search, name='search'), # search
]