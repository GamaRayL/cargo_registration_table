from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView, ListAPIView, RetrieveAPIView

from shipments.filters import ShipmentContainsFilter
from shipments.models import Shipment
from shipments.serializers import ShipmentSerializer


class ShipmentCreateAPIView(CreateAPIView):
    serializer_class = ShipmentSerializer


class ShipmentUpdateAPIView(UpdateAPIView):
    pass


class ShipmentDeleteAPIView(DestroyAPIView):
    pass


class ShipmentListAPIView(ListAPIView):
    serializer_class = ShipmentSerializer
    queryset = Shipment.objects.all()
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_class = ShipmentContainsFilter
    ordering_fields = ['date', 'time', 'category', 'in_stock', 'vendor', 'counted', 'driver']


class ShipmentDetailsAPIView(RetrieveAPIView):
    pass
