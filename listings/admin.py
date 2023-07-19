from django.contrib import admin

# Register your models here.

from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'address') # Elementos a serem mostrados na lista
    list_display_links = ('id', 'title') # Elementos que quando clicados levam a página de edição
    list_filter = ('realtor',) # caixinha de filtro por elemento passado por parâmetro
    list_editable = ('is_published',) # transforma bool em checkbox
    search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode', 'price') # itens que podem ser pesquisados
    list_per_page = 25 # quantos elementos por página

admin.site.register(Listing, ListingAdmin) # agora admins podem criar novas listings no admin page