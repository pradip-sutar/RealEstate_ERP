from django.urls import path
from .views import *

urlpatterns = [
    path('subproject_details_handler/', project_subproject_details_handler, name='subproject_details_handler'),
    path('commission_handler/', project_commission_handler, name='commission_handler'),
    path('payment_slab_handler/', project_payment_slab_handler, name='payment_slab_handler'),
    path('tax_handler/', project_tax_handler, name='tax_handler'),
    path('amenity_handler/', project_amenity_handler, name='amenity_handler'),
    path('paid_amenity_handler/', project_paid_amenity_handler, name='paid_amenity_handler'),
    path('project_nearby_handler/', nearby_handler, name='paid_amenity_handler'),
    path('project_specification_handler/', project_specification_handler, name='project_specification_handler'),
    path('project_images_handler/', project_images_handler, name='project_images_handler'),
    path('generate_pdf/', generate_pdf, name='generate_pdf'),
]
