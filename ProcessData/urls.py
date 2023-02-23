from rest_framework.routers import SimpleRouter
from .views import OutputDataViewSet
router_output_data = SimpleRouter()
router_output_data.register('output',OutputDataViewSet,basename='output')