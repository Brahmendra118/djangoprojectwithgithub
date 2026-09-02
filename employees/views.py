from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee


def home(request):
    employees = Employee.objects.all()

    return render(request, 'employees/home.html', {
        'employees': employees
    })


def employee_list(request):
    employees = Employee.objects.all()

    search = request.GET.get('search')

    if search:
        employees = employees.filter(
            name__icontains=search
        )

    return render(request, 'employees/employee_list.html', {
        'employees': employees
    })


def add_employee(request):
    if request.method == 'POST':

        Employee.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            department=request.POST['department'],
            designation=request.POST['designation'],
            salary=request.POST['salary'],
            joining_date=request.POST['joining_date']
        )

        return redirect('employee_list')

    return render(request, 'employees/employee_form.html')


def edit_employee(request, id):
    employee = get_object_or_404(Employee, id=id)

    if request.method == 'POST':

        employee.name = request.POST['name']
        employee.email = request.POST['email']
        employee.phone = request.POST['phone']
        employee.department = request.POST['department']
        employee.designation = request.POST['designation']
        employee.salary = request.POST['salary']
        employee.joining_date = request.POST['joining_date']

        employee.save()

        return redirect('employee_list')

    return render(request, 'employees/employee_form.html', {
        'employee': employee
    })


def delete_employee(request, id):
    employee = get_object_or_404(Employee, id=id)

    if request.method == 'POST':
        employee.delete()
        return redirect('employee_list')

    return render(request, 'employees/employee_confirm_delete.html', {
        'employee': employee
    })