from django.urls import path
from . import views

urlpatterns = [
    path('project_type_handler/', views.project_type_handler, name='project_type_handler'),
    path('project_payment_schedules_handler/', views.project_payment_schedules_handler, name='project_payment_schedules_handler'),
    path('project_product_types_handler/', views.project_product_types_handler, name='project_product_types_handler'),
    path('project_raisecost_types_handler/', views.project_raisecost_types_handler, name='project_raisecost_types_handler'),
    path('project_amenity_masters_handler/', views.project_amenity_master_list, name='project_amenity_master_list_handler'),
    path('project_nearby_segments_handler/', views.project_nearby_segment_list, name='project_nearby_segment_list_handler'),
    path('project_facing_masters_handler/', views.project_facing_master_list, name='project_facing_master_list_handler'),
    path('project_commissions_handler/', views.project_commission_list, name='project_commission_list_handler'),
    path('product_ownerships_handler/', views.product_ownership_list, name='product_ownership_list_handler'),
    path('product_approval_bodies_handler/', views.product_approval_body_list, name='product_approval_body_list_handler'),
    path('project_taxes_handler/', views.project_tax_list, name='project_tax_list_handler'),
    path('project_products_handler/', views.project_product_list, name='project_product_list_handler'),
    path('project_add_payments_handler/', views.project_add_payment_list_handler, name='project_add_payment_list_handler'),
    path('project_add_amenities_handler/', views.project_add_amenity_list_handler, name='project_add_amenity_list_handler'),
    path('project_add_commission_handler/', views.project_add_commission_handler, name='project_add_commission_handler'),
    path('project_add_tax_handler/', views.project_add_tax_handler, name='project_add_tax_handler'),
    path('project_add_paid_amenity_handler/', views.project_add_paid_amenity_handler, name='project_add_paid_amenity_handler'),
    path('project_add_price_handler/', views.project_add_price_handler, name='project_add_price_handler'),
    path('project_add_inventory_handler/', views.project_add_inventory_handler, name='project_add_inventory_handler'),

]
