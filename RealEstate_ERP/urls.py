from django.contrib import admin
from django.urls import path, include
from app1 import views
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', obtain_auth_token, name='api_token_auth'),
    path('user_creation/', views.user_creation, name='api_token_auth'),
    path('api/',include('app1.urls')),
    path('api/',include('Employee_Management.urls')),
    path('api/',include('Team_Management.urls')),
    path('api/',include('Pre_Project.urls')),
    path('api/',include('Projects.urls')),
    path('api/',include('Department.urls')),
    path('api/',include('Enquiry_Bucket.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)