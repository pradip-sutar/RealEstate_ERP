from django.urls import path
from .views import *

urlpatterns = [
    path('product-details/', product_detail_view, name='product-details'),
    path('raise-cost/', raise_cost_view, name='raise-cost'),
    path('product-cost/', product_cost_view, name='product-cost'),
    path('product-cost/', product_cost_view, name='product-cost'),
    path('amenity-cost/', amenity_cost_view, name='amenity-cost')
]
