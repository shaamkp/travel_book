from django.db import models

from general.models import BaseModel

class Booking(BaseModel):
    booking_id = models.CharField(max_length=128, null=True, blank=True)
    destination = models.ForeignKey('destinations.Destinations', on_delete=models.CASCADE, null=True, blank=True)
    costumer = models.ForeignKey('costumers.Costumer', on_delete=models.CASCADE, null=True, blank=True)
    booking_date = models.DateField()
    number_of_passenger = models.PositiveIntegerField(null=True, blank=True)
    cost_per_passenger = models.PositiveIntegerField(null=True, blank=True)

    def save(self, *args, **kwargs):

        if not self.booking_id:
            prefix_1 = self.costumer.first_name[:3].upper()
            prefix_2 = self.destination.destination_name[:3].upper()
            suffix = str(self.id)[-4:].upper()
            self.booking_id = 'TB' + prefix_1 + prefix_2 + suffix

        super(Booking, self).save(*args, **kwargs)

    class Meta:
        db_table = 'bookings_booking'
        verbose_name = ('Booking')
        verbose_name_plural = ('Bookings')
        ordering = ('-created_at',)

    def __str__(self):
        return self.booking_id


