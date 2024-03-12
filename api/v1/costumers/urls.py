from django.urls import re_path

from api.v1.costumers import views


app_name = 'api_v1_costumers'

urlpatterns = [
    re_path(r'^csv-list-costumers/$', views.csv_list_costumers,name="csv-list-costumers"),
]