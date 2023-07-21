from django.shortcuts import render

# Create your views here.

from .models import Listing

def index(request):
    listings = Listing.objects.all()
    
    context = {
        'listings': listings,
    }

    return render (request, 'pages/listings/listings.html', context)

def listing(request, listing_id):
    return render (request, 'pages/listings/listing.html')

def search(request):
    return render (request, 'pages/listings/search.html')
