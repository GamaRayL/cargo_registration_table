from django_filters import rest_framework as filters

from shipments.models import Shipment


class ShipmentContainsFilter(filters.FilterSet):
    date = filters.CharFilter(field_name='date', lookup_expr='icontains')
    time = filters.CharFilter(field_name='time', lookup_expr='icontains')

    declared = filters.NumberFilter(field_name='declared', lookup_expr='icontains')
    accepted = filters.NumberFilter(field_name='accepted', lookup_expr='icontains')
    left__icontains = filters.NumberFilter(
        method='filter_left', label='Left Field', required=False
    )

    vendor = filters.CharFilter(field_name='vendor', lookup_expr='icontains')
    label = filters.CharFilter(field_name='label', lookup_expr='icontains')
    document = filters.CharFilter(field_name='document', lookup_expr='icontains')
    counted = filters.CharFilter(field_name='counted', lookup_expr='icontains')
    driver = filters.CharFilter(field_name='driver', lookup_expr='icontains')

    class Meta:
        model = Shipment
        fields = '__all__'

    @staticmethod
    def filter_left(queryset, name, value):
        # Ваша логика фильтрации по полю left из сериализатора
        return queryset.filter(left__icontains=value)

# - [ ] Дата (DATE)
# - [ ] Время (TIME)
# - [ ] Маркировка (STRING)
# - [ ] Документ поступления (STRING)
# - [ ] Поставщик (STRING)
# - [ ] Заявлено (NUMBER)
# - [ ] Принято (NUMBER)
# - [ ] Считал (STRING)
# - [ ] Водитель (STRING)

# 3. Таблица должна иметь сортировку по всем полям кроме даты.
#       Фильтрация должна быть в виде двух выпадающих списков и текстового поля:
#     1. Выбор колонки, по которой будет фильтрация
#     2. Выбор условия (равно, содержит, больше, меньше)
#     3. Поле для ввода значения для фильтрации
