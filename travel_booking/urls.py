
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/bookings/', include('api.v1.bookings.urls', namespace='api_v1_bookings')),
    path('api/v1/costumers/', include('api.v1.costumers.urls', namespace='api_v1_costumers')),
    path('api/v1/destinations/', include('api.v1.destinations.urls', namespace='api_v1_destinations')),
]
