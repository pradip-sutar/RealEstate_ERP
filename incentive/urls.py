from django.urls import path
from . import views

urlpatterns = [
    path('goals/', views.goal_list, name='goal_list'),
    path('goals/<int:pk>/', views.goal_detail, name='goal_detail'),
]
