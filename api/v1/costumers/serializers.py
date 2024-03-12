from rest_framework import serializers

from costumers.models import Costumer


class ListCostumerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Costumer
        fields = ('costumer_id', 'first_name', 'email', 'phone')