from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
# Create your views here.
from .models import DataBet
from .serializers import InputDataModelSerializer
from rest_framework.response import Response
class inputDataModelView(ModelViewSet):
    queryset=DataBet.objects.all()
    serializer_class= InputDataModelSerializer
    http_method_names=['post']


    def create(self, request):
        serializado_data=InputDataModelSerializer(request.data)
        db=DataBet(digit=serializado_data.data['digit'],color=serializado_data.data['color'],timestamp=serializado_data.data['timestamp'])
        db.save()
        return Response({'retorno':serializado_data.data})






