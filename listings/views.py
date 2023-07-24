from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

from .models import Listing

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    
    context = {
        'listings': paged_listings,
    }

    return render (request, 'pages/listings/listings.html', context)

def listing(request, listing_id):
    return render (request, 'pages/listings/listing.html')

def search(request):
    return render (request, 'pages/listings/search.html')
