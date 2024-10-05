from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('agent_type_handler/', agent_type_handler, name='agent_type_handler'),
    path('agent_management_handler/', agent_management_handler, name='agent_management_handler'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)