from django.contrib import admin
from django.urls import path, include
from Sub_Projects import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    
    path('product_details_handler/', views.product_details_handler, name='product_details_handler'),
    path('raise_cost_handler/', views.raise_cost_handler, name='raise_cost_handler '),
    path('product_cost_handler/', views.product_cost_handler, name='product_cost_handler'),
    path('product_inventories_handler/', views.product_inventories_handler, name='product_inventories_handler'),
    path('sub_product_images_handler/', views.sub_product_images_handler, name='sub_product_images_handler'),
    path('payment_slab_handler/', views.payment_slab_handler, name='payment_slab_handler'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)