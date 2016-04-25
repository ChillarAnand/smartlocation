from django.contrib.gis.geos import Point, Polygon
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response


from .models import Provider, ServiceArea
from .serializers import ProviderSerializer, ServiceAreaSerializer


class ProviderViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows providers to be viewed or edited.
    """
    queryset = Provider.objects.all().order_by('name')
    serializer_class = ProviderSerializer


class ServiceAreaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows service areas to be viewed or edited.
    """
    queryset = ServiceArea.objects.all().order_by('name')
    serializer_class = ServiceAreaSerializer


@api_view(['GET'])
def find_service_areas(request):
    latitude = request.GET.get('latitude')
    longitude = request.GET.get('longitude')
    if not (latitude and longitude):
        return Response(
            {"error":
             "Query with latitude and longitude"}
        )
    p = Point(float(longitude), float(latitude))
    sa = []
    for area in ServiceArea.objects.all():
        poly = Polygon(eval(area.polygon)[0])
        if p.within(poly):
            sa.append({
                'name': area.name,
                'provider': area.provider.name,
                'price': area.price
            })
    return Response(sa)
