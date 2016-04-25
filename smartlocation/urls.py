from django.conf.urls import include, url
from rest_framework import routers


from location.api import ProviderViewSet, ServiceAreaViewSet, find_service_areas

router = routers.DefaultRouter()
router.register(r'providers', ProviderViewSet)
router.register(r'serviceareas', ServiceAreaViewSet)


urlpatterns = [
    url(r'^api/v1/find_service_areas', find_service_areas, name='find_service_areas'),
    url(r'^api/v1/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
