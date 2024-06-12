from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/<int:mob>/', views.admin_view),
    path('admin-login/', views.admin_login),
    path('department_name_handler/', views.department_name_handler, name='create_department'),
    path('department_name_handler/<int:departmentid>/', views.department_name_handler, name='get_department'),
    path('department_label_handler/', views.department_label_handler, name='create_label'),
    path('department_label_handler/<int:labelid>/', views.department_label_handler, name='get_label'),
    path('department_grade_handler/', views.department_grade_handler, name='create_grade'),
    path('department_grade_handler/<int:gradeid>/', views.department_grade_handler, name='get_grade'),
    path('department_designation_handler/', views.department_designation_handler, name='create_designation'),
    path('department_designation_handler/<int:designationid>/', views.department_designation_handler, name='get_designation'),
]
