from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView, ListAPIView, RetrieveAPIView

from shipments.filters import ShipmentContainsFilter
from shipments.models import Shipment
from shipments.paginations import ShipmentPagination
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
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter, ]
    filterset_class = ShipmentContainsFilter
    search_fields = ['date', 'time', 'label', 'document', 'vendor', 'declared', 'accepted', 'counted', 'driver']
    ordering_fields = ['date', 'time', 'label', 'document', 'vendor', 'declared', 'accepted', 'counted', 'driver']
    pagination_class = ShipmentPagination


class ShipmentDetailsAPIView(RetrieveAPIView):
    pass
