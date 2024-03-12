from django.core.management.base import BaseCommand
from django.db import models

from bookings.models import Booking


class Command(BaseCommand):

    def handle(self, *args, **options):
        bookings_per_destination = Booking.objects.values('destination').annotate(total_bookings=models.Count('id'))

        for booking in bookings_per_destination:
            destination = booking['destination']
            total_bookings = booking['total_bookings']
            
            self.stdout.write(self.style.SUCCESS(f"Destination: {destination}, Total Bookings: {total_bookings}"))