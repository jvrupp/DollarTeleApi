
from rest_framework.response import Response
# Create your views here.
from rest_framework.viewsets import ViewSet
import ProcessData.AlgoModels.Logistic 
###################################################################ALGORITIMO#######################################
class OutputDataViewSet(ViewSet):
    def list(self,request):
        result=ProcessData.AlgoModels.Logistic.logistic()
        return Response({'response':result})


