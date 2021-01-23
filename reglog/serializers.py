from rest_framework import serializers
from reglog.models import product








class ProductSerializer(serializers.ModelSerializer):


    class Meta:
        model=product
        fields=("id","name","price","image","description","makername","booking","type")



