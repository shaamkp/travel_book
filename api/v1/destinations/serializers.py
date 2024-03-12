from rest_framework import serializers

from destinations.models import Destinations


class AddDestinationSerializer(serializers.Serializer):
    destination_name = serializers.CharField()
    country = serializers.CharField()
    popular_season = serializers.CharField()
    

class ListDestinationsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Destinations
        fields = ('destination_id', 'destination_name', 'country', 'popular_season')

