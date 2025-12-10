from django.contrib import admin

from listings.models import Band, Listing

# Class for displaying the fields of the Band model directly in the list of objects in the Django Admin interface
class BandAdmin(admin.ModelAdmin):
    list_display = ['name', 'year_formed', 'genre']


# Class for displaying the fields of the Listing model directly in the list of objects in the Django Admin interface
class ListingAdmin(admin.ModelAdmin):
    list_display = ['title', 'sold', 'type']


admin.site.register(Band, BandAdmin)
admin.site.register(Listing, ListingAdmin)