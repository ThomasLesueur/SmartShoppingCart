from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from cart.models import Product, Discount
from cart.serializers import ProductSerializer, DiscountSerializer
from cart.services import Pack

class DiscountList(generics.ListCreateAPIView):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer


class DiscountDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

@api_view(['POST'])
def product_list(request, format=None):
    if request.method == 'POST':
        pack = Pack(request.data)
        if pack.validate() == False:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        body = {
            'amount': pack.calculate()
        }
        return Response(body)


