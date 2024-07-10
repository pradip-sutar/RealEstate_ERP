from django.contrib import admin
from django.urls import path, include
from Department import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    
    path('department_name_handler/', views.department_name_handler, name='department_handler'),
    path('department_designation_handler/', views.department_designation_handler, name='department_designation_handler '),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)