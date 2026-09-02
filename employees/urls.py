from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),

    path(
        'employees/',
        views.employee_list,
        name='employee_list'
    ),

    path(
        'employees/add/',
        views.add_employee,
        name='add_employee'
    ),

    path(
        'employees/edit/<int:id>/',
        views.edit_employee,
        name='edit_employee'
    ),

    path(
        'employees/delete/<int:id>/',
        views.delete_employee,
        name='delete_employee'
    ),
]