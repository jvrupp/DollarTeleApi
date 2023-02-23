from rest_framework.routers import SimpleRouter
from .views import inputDataModelView
router_input_data = SimpleRouter()
router_input_data.register('input',inputDataModelView,basename='output')