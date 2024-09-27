from django.urls import path
from . import views

urlpatterns = [
    path('product-specification/', views.product_specification_view, name='product_specification'),
    path('product-image/', views.product_image_view, name='product_image'),
    path('enquiry-summary/', views.enquiry_summary_view, name='enquiry_summary'),
    path('visit-summary/', views.visit_summary_view, name='visit_summary'),
    path('quote-summary/', views.quote_summary_view, name='quote_summary'),
    path('employee-status/', views.employee_status_view, name='employee_status'),
    path('customer-information/', views.customer_information_view, name='customer_information'),
    path('commission-details/', views.commission_details_view, name='commission_details'),
    path('payment-details/', views.payment_details_view, name='payment_details'),
    path('customer-document/', views.customer_document_view, name='customer_document'),
    path('property-document/', views.property_document_view, name='property_document'),
]
