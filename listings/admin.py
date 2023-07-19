from django.contrib import admin

# Register your models here.

from .models import Listing

admin.site.register(Listing) # agora admins podem criar novas listings no admin page