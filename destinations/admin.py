from django.contrib import admin

from destinations.models import *

class DestinationsAdmin(admin.ModelAdmin):
    list_display = ('id', 'destination_id', 'destination_name', 'country', 'popular_season')
    exclude = ('destination_id',)

admin.site.register(Destinations, DestinationsAdmin)
