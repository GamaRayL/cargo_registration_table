from django_filters import rest_framework as filters

from shipments.models import Shipment


class ShipmentContainsFilter(filters.FilterSet):
    date = filters.CharFilter(field_name='date', lookup_expr='icontains')
    time = filters.CharFilter(field_name='time', lookup_expr='icontains')

    declared = filters.NumberFilter(field_name='declared', lookup_expr='icontains')
    accepted = filters.NumberFilter(field_name='accepted', lookup_expr='icontains')

    declared__lt = filters.NumberFilter(field_name='declared', lookup_expr='lt')
    accepted__lt = filters.NumberFilter(field_name='accepted', lookup_expr='lt')

    declared__gt = filters.NumberFilter(field_name='declared', lookup_expr='gt')
    accepted__gt = filters.NumberFilter(field_name='accepted', lookup_expr='gt')

    vendor = filters.CharFilter(field_name='vendor', lookup_expr='icontains')
    label = filters.CharFilter(field_name='label', lookup_expr='icontains')
    document = filters.CharFilter(field_name='document', lookup_expr='icontains')
    counted = filters.CharFilter(field_name='counted', lookup_expr='icontains')
    driver = filters.CharFilter(field_name='driver', lookup_expr='icontains')

    class Meta:
        model = Shipment
        fields = ['date', 'time', 'declared', 'accepted', 'vendor', 'label', 'document', 'counted', 'driver',
                  'declared__lt', 'accepted__lt',
                  'declared__gt', 'accepted__gt', ]
