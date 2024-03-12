from django.db import models

from general.models import BaseModel

class Costumer(BaseModel):
    costumer_id = models.CharField(max_length=128, null=True, blank=True)
    first_name = models.CharField(max_length=128, null=True, blank=True)
    last_name = models.CharField(max_length=128, null=True, blank=True)
    email = models.CharField(max_length=128, null=True, blank=True)
    phone = models.CharField(max_length=128, null=True, blank=True)

    def save(self, *args, **kwargs):

        if not self.costumer_id:
            prefix = self.first_name[:3].upper()
            suffix = str(self.id)[-4:].upper()
            self.costumer_id = 'TB' + prefix + suffix

        super(Costumer, self).save(*args, **kwargs)

    
    class Meta:
        db_table = 'costumers_costumer'
        verbose_name = ('Costumer')
        verbose_name_plural = ('Costumers')
        ordering = ('-created_at',)

    def __str__(self):
        return self.costumer_id
