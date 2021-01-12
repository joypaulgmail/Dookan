from rest_framework.serializers import ModelSerializer
from reglog.models import product
class ProductSerializer(ModelSerializer):
    class Meta:
        model=product
        fields="__all__"
