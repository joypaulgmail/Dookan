from client.models import ClientInformation
from rest_framework import serializers
class ClientSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=60)
    primary_contact = serializers.CharField(max_length=15)
    secondary_contact = serializers.CharField(max_length=15)
    email = serializers.EmailField()
    address = serializers.CharField(max_length=100)
    pin = serializers.CharField(max_length=15)
    password = serializers.CharField(max_length=50)
    unique_id = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return ClientInformation.objects.create(**validated_data)




class ClientSerialize(serializers.ModelSerializer):
    class Meta:
        model=ClientInformation
        exclude = ('idproof',)

