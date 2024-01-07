from django_filters import rest_framework as filters

from shipments.models import Shipment


class ShipmentContainsFilter(filters.FilterSet):
    date = filters.CharFilter(field_name='date', lookup_expr='exact')
    date__ct = filters.CharFilter(field_name='date', lookup_expr='icontains')
    date__lt = filters.DateFilter(field_name='date', lookup_expr='lt')
    date__gt = filters.DateFilter(field_name='date', lookup_expr='gt')
    time = filters.CharFilter(field_name='time', lookup_expr='exact')
    time__ct = filters.CharFilter(field_name='time', lookup_expr='icontains')
    time__lt = filters.TimeFilter(field_name='time', lookup_expr='lt')
    time__gt = filters.TimeFilter(field_name='time', lookup_expr='gt')
    declared = filters.NumberFilter(field_name='declared', lookup_expr='exact')
    declared__ct = filters.NumberFilter(field_name='declared', lookup_expr='icontains')
    declared__lt = filters.NumberFilter(field_name='declared', lookup_expr='lt')
    declared__gt = filters.NumberFilter(field_name='declared', lookup_expr='gt')
    accepted = filters.NumberFilter(field_name='accepted', lookup_expr='exact')
    accepted__ct = filters.NumberFilter(field_name='accepted', lookup_expr='icontains')
    accepted__lt = filters.NumberFilter(field_name='accepted', lookup_expr='lt')
    accepted__gt = filters.NumberFilter(field_name='accepted', lookup_expr='gt')
    
    vendor = filters.CharFilter(field_name='vendor', lookup_expr='exact')
    vendor__ct = filters.CharFilter(field_name='vendor', lookup_expr='icontains')
    label = filters.CharFilter(field_name='label', lookup_expr='exact')
    label__ct = filters.CharFilter(field_name='label', lookup_expr='icontains')
    document = filters.CharFilter(field_name='document', lookup_expr='exact')
    document__ct = filters.CharFilter(field_name='document', lookup_expr='icontains')
    counted = filters.CharFilter(field_name='counted', lookup_expr='exact')
    counted__ct = filters.CharFilter(field_name='counted', lookup_expr='icontains')
    driver = filters.CharFilter(field_name='driver', lookup_expr='exact')
    driver__ct = filters.CharFilter(field_name='driver', lookup_expr='icontains')

    class Meta:
        model = Shipment
        fields = ['vendor', 'date', 'time',
                  'label', 'document', 'counted',
                  'driver', 'accepted', 'declared',
                  'date__ct', 'time__ct', 'declared__ct',
                  'accepted__ct', 'vendor__ct', 'label__ct',
                  'document__ct', 'counted__ct', 'driver__ct',
                  'declared__lt', 'accepted__lt', 'declared__gt',
                  'accepted__gt', 'date__lt', 'date__gt',
                  'time__lt', 'time__gt']
