from rest_framework import routers
from .api import crudApiOtpViewSet

router=routers.DefaultRouter()

router.register('api/crudApiOtp',crudApiOtpViewSet,'crudApiOtp')

urlpatterns = router.urls
    

