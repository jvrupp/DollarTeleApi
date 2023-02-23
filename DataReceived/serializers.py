from rest_framework.serializers import ModelSerializer
from .models import DataBet


class InputDataModelSerializer(ModelSerializer):
    class Meta:
        model=DataBet
        fields ='__all__'