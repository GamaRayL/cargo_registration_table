from rest_framework.serializers import ModelSerializer, SerializerMethodField

from shipments.models import Shipment


class ShipmentSerializer(ModelSerializer):
    left = SerializerMethodField()

    class Meta:
        model = Shipment
        fields = ['id', 'date', 'time', 'label',
                  'document', 'vendor', 'declared', 'accepted',
                  'left', 'counted', 'driver']

    @staticmethod
    def get_left(obj):
        declared = obj.declared
        accepted = obj.accepted

        if accepted and declared:
            return declared - accepted
        elif declared:
            return declared
