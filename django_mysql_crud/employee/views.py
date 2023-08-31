from django.shortcuts import render, redirect
from employee.forms import EmployeeForm
from employee.models import Employees

# Create your views here.
def emp(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
                form = EmployeeForm()
    return render(request, 'index.html', {'form':form})

def show(request):
    employees = Employees.objects.all()
    return render(request, 'show.html', {'contacts': employees})

# def edit(request, id):
#     employee = Employees.objects.get(emp_id=id)
#     return render(request, 'edit.html', {'contacts':employee})

def update(request, id):
    employee = Employees.objects.get(emp_id=id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('/show')
    else:
        form = EmployeeForm(instance=employee)

    return render(request, 'edit.html', {'form': form, 'employee': employee})


def destroy(request, id):
    employee = Employees.objects.get(emp_id = id)
    employee.delete()
    return redirect('/show')

def search(request):
    ename = request.GET.get('ename')
    if ename:
        employee = Employees.objects.filter(emp_name__icontains=ename)
    else:
        employee = Employees.objects.none()
    return render(request, 'search.html', {'employee' : employee})
