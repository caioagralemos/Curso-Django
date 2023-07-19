from django.contrib import admin

# Register your models here.

from .models import Realtor

admin.site.register(Realtor) # agora admins podem criar novas listings no admin page