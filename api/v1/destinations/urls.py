from django.urls import re_path

from api.v1.destinations import views


app_name = 'api_v1_destinations'

urlpatterns = [
    re_path(r'^add-destinations/$', views.add_destinations,name="add-destinations"),
    re_path(r'^csv-list-destination/$', views.csv_list_destinations,name="csv-list-destination"),
]