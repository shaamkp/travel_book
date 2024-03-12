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
from django.db import models

from api.v1.bookings.serializers import *
from bookings.models import Booking
from destinations.models import Destinations


@api_view(['GET'])
@permission_classes([AllowAny])
def csv_list_bookings(request):
    try:
        if (bookings := Booking.objects.filter(is_deleted=False)).exists():

            serialized_data = ListBookingSerializer(
                bookings,
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
                Key='booking_data.csv',
                ContentType='text/csv'  # Set appropriate content type
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


@api_view(['GET'])
@permission_classes([AllowAny])
def total_bookings_per_destinations(request):
    try:
        serialized_array = []
        if (destinations := Destinations.objects.filter(is_deleted=False)).exists():

            for destination in destinations:
                total_bookings = Booking.objects.filter(is_deleted=False, destination=destination)

                serialized_data = BookingsPerDestinationSerializer(
                    total_bookings,
                    context = {
                        "request" : request,   
                    },
                    many = True
                ).data

                serialized_array.append(serialized_data[0])

            response_data = {
                "StatusCode": 6000,
                "data": serialized_array
            }

            return Response({'app_data': response_data}, status=status.HTTP_200_OK)
        else:
            response_data = {
                "StatusCode": 6001,
                "message": "Destinations not found"
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
