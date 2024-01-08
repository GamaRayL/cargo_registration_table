import json

from rest_framework import status
from rest_framework.test import APITestCase

from shipments.constants import EXPECTED_CREATE_DATA, EXPECTED_DATA, UPDATED_EXPECTED_DATA
from shipments.models import Shipment


class ShipmentTestCase(APITestCase):
    def setUp(self) -> None:
        self.shipment = Shipment.objects.create(
            date="2022-01-05",
            time="16:33:00",
            label="3000",
            document="0000-3333",
            vendor="Пронет",
        )

    def test_create_shipment(self):
        """ Тестирование создания отгрузки """
        data = {
            "date": "2024-01-05",
            "time": "16:25:00",
            "label": "29769",
            "document": "0000-016166, 0000-016139 0000-000017 0000-016139",
            "vendor": "Мерлион",
            "counted": "Гамид",
            "driver": "Газель ТК"
        }

        response = self.client.post('/shipments/create/', data=data)

        self.assertEqual(response.json(), EXPECTED_CREATE_DATA)
        self.assertTrue(Shipment.objects.all().exists())

    def test_list_shipment(self):
        """ Тестирование получения списка отгрузок """

        response = self.client.get('/shipments/')

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {
                "count": 1,
                "next": None,
                "previous": None,
                "results": [
                    EXPECTED_DATA
                ]
            }
        )

    def test_update_shipment(self):
        """ Тестирование обновления урока """

        data = {
            "date": "2023-01-05",
            "time": "16:25:00",
            "label": "29769",
            "document": "0000-016133",
            "vendor": "Мерлион",
            "declared": 22,
            "accepted": 22,
            "left": None,
            "counted": "Гамид",
            "driver": "Газель ТК"
        }

        response = self.client.patch(f'/shipments/update/{self.shipment.id}/',
                                     data=json.dumps(data), content_type='application/json')

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            UPDATED_EXPECTED_DATA
        )

    def test_shipment_detele(self):
        """ Тестирование удаления отгрузки """
        response = self.client.delete(f'/shipments/delete/{self.shipment.id}/')

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
