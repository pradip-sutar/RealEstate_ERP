from django.urls import path
from .views import manage_data

urlpatterns = [
    path('api/<str:model_name>/', manage_data, name='list-create'),
    path('api/<str:model_name>/<str:obj_id>/', manage_data, name='retrieve-update-delete'),
]
