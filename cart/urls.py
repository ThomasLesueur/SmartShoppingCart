from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from cart import views

urlpatterns = [
    path('products/', views.ProductList.as_view()),
    path('products/<int:pk>/', views.ProductDetail.as_view()),
    path('discounts/', views.DiscountList.as_view()),
    path('discounts/<int:pk>/', views.DiscountDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)