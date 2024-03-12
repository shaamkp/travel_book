import traceback
import csv
import boto3
import io

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

from django.db import transaction
from django.http import HttpResponse
from django.conf import settings as SETTINGS


from api.v1.destinations.serializers import *
from general.functions import generate_serializer_errors
from destinations.models import Destinations


@api_view(['POST'])
@permission_classes([AllowAny])
def add_destinations(request):
    try:
        transaction.set_autocommit(False)
        serialized_data = AddDestinationSerializer(data=request.data)

        if serialized_data.is_valid():
            destination_name = request.data["destination_name"]
            country = request.data["country"]
            popular_season = request.data["popular_season"]

            if not Destinations.objects.filter(destination_name=destination_name, country=country, popular_season=popular_season).exists():
                destinations = Destinations.objects.create(
                    destination_name = destination_name,
                    country = country,
                    popular_season = popular_season
                )

                transaction.commit()
                response_data = {
                    "StatusCode": 6000,
                    "data": {
                        "title": "Success",
                        "message": "Destination added successfully"
                    }
                }
            else:
                transaction.rollback()
                response_data = {
                    "StatusCode": 6001,
                    "data": {
                        "title": "Failed",
                        "message": "Destination already exists"
                    }
                }
        else:
            response_data = {
                "StatusCode" : 6001,
                "data" : {
                    "title" : "Failed",
                    "message" : generate_serializer_errors(serialized_data._errors)
                }
            }
    except Exception as e:
        transaction.rollback()
        errType = e.__class__.__name__
        errors = {
            errType: traceback.format_exc()
        }
        response_data = {
            "StatusCode": 6001,
            "title": "Failed",
            "api": request.get_full_path(),
            "request": request.data,
            "message": str(e),
            "response": errors
        }

    return Response({'app_data': response_data}, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([AllowAny])
def csv_list_destinations(request):
    try:
        if (destinations := Destinations.objects.filter(is_deleted=False)).exists():

            serialized_data = ListDestinationsSerializer(
                destinations,
                context = {
                    "request" : request
                },
                many = True
            ).data

            headers = serialized_data[0].keys() if serialized_data else []
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="destination_data.csv"'
            csv_buffer = io.StringIO()
            writer = csv.DictWriter(response, fieldnames=headers)
            writer.writeheader()
            writer.writerows(serialized_data)

            s3_client = boto3.client(
                's3',
                aws_access_key_id=SETTINGS.AWS_ACCESS_KEY_ID,
                aws_secret_access_key=SETTINGS.AWS_SECRET_ACCESS_KEY,
                region_name=SETTINGS.AWS_S3_REGION_NAME
            )

            s3_client.put_object(
                Body=csv_buffer.getvalue(),
                Bucket='csv-data-task',
                Key='destination_data.csv',
                ContentType='text/csv'  
            )

            return response

    except Exception as e:
        transaction.rollback()
        errType = e.__class__.__name__
        errors = {
            errType: traceback.format_exc()
        }
        response_data = {
            "StatusCode": 6001,
            "title": "Failed",
            "api": request.get_full_path(),
            "request": request.data,
            "message": str(e),
            "response": errors
        }

    return Response({'app_data': response_data}, status=status.HTTP_200_OK)




