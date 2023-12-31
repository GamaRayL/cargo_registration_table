from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.filters import OrderingFilter
from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView, ListAPIView
from rest_framework.response import Response

from shipments.filters import ShipmentContainsFilter
from shipments.models import Shipment
from shipments.paginations import ShipmentPagination
from shipments.serializers import ShipmentSerializer


class ShipmentCreateAPIView(CreateAPIView):
    """
        Добавление отгрузки.
    """
    serializer_class = ShipmentSerializer


class ShipmentUpdateAPIView(UpdateAPIView):
    """
        Обновление отгрузки по id.
    """
    serializer_class = ShipmentSerializer
    queryset = Shipment.objects.all()


class ShipmentDeleteAPIView(DestroyAPIView):
    """
        Удаление отгрузки по id.
    """
    queryset = Shipment.objects.all()

    def delete(self, request, *args, **kwargs):
        shipment = self.get_object()
        shipment.delete()
        return Response(
            {'message': 'Привычка удалена'},
            status=status.HTTP_204_NO_CONTENT
        )


class ShipmentListAPIView(ListAPIView):
    """
        Получение отсортированного списка отгрузок от крайнего id к первому.
        Также применены: пагинация, сортировка и фильтр.
    """
    serializer_class = ShipmentSerializer
    queryset = Shipment.objects.all().order_by('-id')
    filter_backends = [DjangoFilterBackend, OrderingFilter, ]
    filterset_class = ShipmentContainsFilter
    search_fields = ['date', 'time', 'label', 'document', 'vendor', 'declared', 'accepted', 'counted', 'driver']
    ordering_fields = ['date', 'time', 'label', 'document', 'vendor', 'declared', 'accepted', 'counted', 'driver']
    pagination_class = ShipmentPagination
