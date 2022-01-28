from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from cart import views

urlpatterns = [
    path('products/', views.product_list),
    path('products/<int:pk>/', views.product_detail),
    path('discounts/', views.DiscountList.as_view()),
    path('discounts/<int:pk>/', views.DiscountDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)