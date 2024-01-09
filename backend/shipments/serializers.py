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
        """Новое поле, которое получается из двух полей declared и accepted"""
        declared = obj.declared
        accepted = obj.accepted

        if accepted and declared:
            return None if declared - accepted == 0 else declared - accepted
        elif declared:
            return declared
        elif accepted:
            return -accepted
        else:
            return None
