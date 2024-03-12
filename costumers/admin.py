from django.contrib import admin

from costumers.models import *

class CostumerAdmin(admin.ModelAdmin):
    list_display = ('id', 'costumer_id', 'first_name', 'last_name', 'email', 'phone')
    exclude = ('costumer_id',)

admin.site.register(Costumer, CostumerAdmin)
