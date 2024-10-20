from django.urls import path
from .views import *

urlpatterns = [
    path('subproject_details_handler/', project_subproject_details_handler, name='product-details'),
    # path('raise-cost/', raise_cost_view, name='raise-cost'),
    # path('product-cost/', product_cost_view, name='product-cost'),
    # path('product-cost/', product_cost_view, name='product-cost'),
    # path('amenity-cost/', amenity_cost_view, name='amenity-cost')
]
