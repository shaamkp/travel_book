import uuid
from django.db import models

from general.models import BaseModel


TRAVEL_BOOKING_DESTTINATION_SEASON = (
    ('winter', 'Winter'),
    ('summer', 'Summer'),
    ('autumn', 'Autumn'),
    ('spring', 'Spring'),
)

class Destinations(BaseModel):
    destination_id = models.CharField(max_length=128, null=True, blank=True)
    destination_name = models.CharField(max_length=128, null=True, blank=True)
    country = models.CharField(max_length=128, null=True, blank=True)
    popular_season = models.CharField(choices=TRAVEL_BOOKING_DESTTINATION_SEASON, max_length=128, null=True, blank=True)

    def save(self, *args, **kwargs):

        if not self.destination_id:
            prefix = self.destination_name[:3].upper()
            suffix = str(self.id)[-4:].upper()
            self.destination_id = 'TB' + prefix + suffix

        super(Destinations, self).save(*args, **kwargs)

    
    class Meta:
        db_table = 'destinations_destination'
        verbose_name = ('Destination')
        verbose_name_plural = ('Destinations')
        ordering = ('-created_at',)

    def __str__(self):
        return self.destination_id