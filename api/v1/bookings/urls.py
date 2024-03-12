from django.urls import re_path

from api.v1.bookings import views

app_name = 'api_v1_bookings'

urlpatterns = [
    re_path(r'^csv-list-bookings/$', views.csv_list_bookings,name="csv-list-bookings"),
    re_path(r'^total-bookings-per-destination/$', views.total_bookings_per_destinations,name="total-bookings-per-destination"),
    
]

# After the deployment the project total-bookings-per-destination api will implement to the lambda function and
# configure the event and trigger the function the periodicaly . We can add the time interval there in the trigger page.
# by giving this api we can get the reponse in 
