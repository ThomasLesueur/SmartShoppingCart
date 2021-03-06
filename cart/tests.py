import json
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from cart.models import Product, Discount
from cart.services import Pack

class ProductTestCase(APITestCase):
    def setUp(self):
        Product.objects.create(name='tomato', price=1.0)
        Product.objects.create(name='ps5', price=500.0)

    def test_get_product_list(self):
        response = self.client.get("/products/")
        expected = [
            {
                "name": "ps5",
                "price": 500.0
            },
            {
                "name": "tomato",
                "price": 1.0
            }
        ]
        result = response.data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(result, expected)
    
    def test_post_product_list(self):
        expected = {
            'name' : 'coco pops',
            'price' : 3.5
        }

        response = self.client.post("/products/", {'name': 'coco pops', 'price': 3.5})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        result = response.data
        self.assertEqual(result, expected)


class DiscountTestCase(APITestCase):
    def setUp(self):
        Discount.objects.create(category='one plus one')
        Discount.objects.create(category='50 percent')

    def test_get_discount_list(self):
        response = self.client.get("/discounts/")
        expected = [
            {
                "category": "50 percent"
            },
            {
                "category": "one plus one"
            }
        ]
        result = response.data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(result, expected)
    
    def test_post_discount_list(self):
        expected = {
            'category' : '25 percent',
        }

        response = self.client.post("/discounts/", {'category' : '25 percent'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        result = response.data
        self.assertEqual(result, expected)

class PackTestCase(APITestCase):
    def setUp(self):
        Product.objects.create(name='ps5', price=500)
        Discount.objects.create(category='one plus one')
        Discount.objects.create(category='50 percent')

    def test_validate(self):
        data = {
            "product_name" : "ps5",
            "quantity" : 3,
            "discounts" : ["one plus one", "50 percent"]
        }
        pack = Pack(data)
        self.assertEqual(pack.validate(), True)

    def test_calculate(self):
        data = {
            "product_name" : "ps5",
            "quantity" : 3,
            "discounts" : ["one plus one", "50 percent"]
        }
        pack = Pack(data)
        self.assertEqual(pack.calculate(), 500)
