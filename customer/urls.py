from django.urls import path
from . import views

urlpatterns = [
    path('customers/', views.customer_form_list, name='customer_form_list'),
    path('customers/<int:pk>/', views.customer_form_detail, name='customer_form_detail'),
]
