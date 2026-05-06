from rest_framework.routers import DefaultRouter
from .views import AirlineViewSet, FlightViewSet

router = DefaultRouter()
router.register(r'airlines', AirlineViewSet)
router.register(r'flights', FlightViewSet)

urlpatterns = router.urls