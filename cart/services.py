from cart.serializers import ProductSerializer, DiscountSerializer
from cart.models import Product, Discount

class Pack:
    discount_manager = None
    product_name = ""
    quantity = 0
    discounts = []
    total = 0.0
    current_price = 0.0

    def __init__(self, data):
        self.product_name = data['product_name']
        self.quantity = data['quantity']
        self.discounts = data['discounts']
        self.discount_manager = DiscountManager()
    
    def validate(self):
        if Product.objects.filter(name__contains=self.product_name) == None:
            return False
        for discount in self.discounts:
            if Discount.objects.filter(category__contains=discount['name']) == None:
                return False
        return True
    
    def calculate(self):
        serializer = ProductSerializer(Product.objects.filter(name__contains=self.product_name))
        self.current_price = serializer.data['price']
        self.total = current_price * self.quantity
        if len(self.discounts) != 0:
            self.total = self.discount_manager.calculate_discount(self)

class DiscountManager:
    def calculate_discount(self, pack):
        for discount in pack.discounts:
            if discount == '50 percent':
                pack.total /= 2
            if discount == 'one plus one':
                for i in range(pack.quantity):
                    if (i + 1) % 3 == 0:
                        pack.total -= pack.current_price
        return pack.total