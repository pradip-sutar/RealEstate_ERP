from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('payment-receipts/', views.payment_receipt_list, name='payment-receipt-list'),
    path('payment-receipts/<str:sales_id>/', views.payment_receipt_detail, name='payment-receipt-detail'),
    
    path('payment-schedules/', views.payment_schedule_list, name='payment-schedule-list'),
    path('payment-schedules/<str:sales_id>/', views.payment_schedule_detail, name='payment-schedule-detail'),
    
    path('sales-agreements/', views.sales_agreement_list, name='sales-agreement-list'),
    path('sales-agreements/<str:sales_id>/', views.sales_agreement_detail, name='sales-agreement-detail'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)