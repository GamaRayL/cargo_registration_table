from django.urls import path

from shipments.apps import ShipmentsConfig
from shipments.views import (
    ShipmentCreateAPIView, ShipmentUpdateAPIView,
    ShipmentDeleteAPIView, ShipmentListAPIView
)

app_name = ShipmentsConfig.name

urlpatterns = [
    path('', ShipmentListAPIView.as_view(), name='shipments'),
    path('create/', ShipmentCreateAPIView.as_view(), name='shipment_create'),
    path('delete/<int:pk>/', ShipmentDeleteAPIView.as_view(), name='shipment_delete'),
    path('update/<int:pk>/', ShipmentUpdateAPIView.as_view(), name='shipment_update'),
]
