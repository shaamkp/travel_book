from django.contrib import admin

from bookings.models import *

class BookingsAdmin(admin.ModelAdmin):
    list_display = ('id', 'booking_id', 'destination', 'costumer', 'booking_date', 'number_of_passenger', 'cost_per_passenger')
    exclude = ('booking_id',)

admin.site.register(Booking, BookingsAdmin)
