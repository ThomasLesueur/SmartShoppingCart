from django.urls import path
from cart import views

urlpatterns = [
    path('products/', views.product_list),
]