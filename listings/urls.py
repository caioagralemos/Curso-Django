from django.urls import path
from . import views

# aqui o padrão é /listings

urlpatterns = [
    path('', views.index, name='listings'), # listings
    path('<int:listing_id>', views.listing, name='listing'), # listing
    path('search', views.search, name='search'), # search
]