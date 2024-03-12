from rest_framework import serializers

from bookings.models import Booking

class ListBookingSerializer(serializers.ModelSerializer):
    destination = serializers.SerializerMethodField()
    costumer = serializers.SerializerMethodField()

    class Meta:
        model = Booking
        fields = (
            'booking_id',
            'destination',
            'costumer',
            'booking_date',
            'number_of_passenger',
            'cost_per_passenger'
        )

    def get_destination(self, instance):
        if instance.destination:
            return instance.destination.destination_name
        else:
            None

    def get_costumer(self, instance):
        if instance.costumer:
            return instance.costumer.first_name
        else:
            None


class BookingsPerDestinationSerializer(serializers.ModelSerializer):
    destination = serializers.SerializerMethodField()
    total_count = serializers.SerializerMethodField()

    class Meta:
        model = Booking
        fields = (
            'destination',
            'total_count'
        )

    def get_destination(self, instance):
        if instance.destination:
            return instance.destination.destination_name
        else:
            return None

    def get_total_count(self, instance):
        return Booking.objects.filter(destination=instance.destination).count()

