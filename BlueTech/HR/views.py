from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from Users.models import Employee


# # Create your views here.
# def recruit(request, dept_name):
#     # members =
#     return render(request, 'HR/recruitment.html', context={'department': request.user.employee.dept, })


@login_required
def departments(request):
    department = request.user.employee.dept
    members = []
    members += Employee.objects.filter(dept='CEO')
    members += Employee.objects.filter(position='CHRO')
    members += Employee.objects.filter(position='CFO')
    members += Employee.objects.filter(position='DS')
    return render(request, 'HR/recruitment.html',
                  context={'department': department, 'user': request.user.employee, 'members': members})


@login_required
def depart(request, dept_name):
    department = request.user.employee.dept
    members = Employee.objects.filter(dept=dept_name)
    return render(request, 'HR/recruitment.html',
                  context={'department': department, 'user': request.user.employee, 'members': members})


@login_required
def job_vacancy(request):
    department = request.user.employee.dept
    return render(request, 'HR/job_posted.html',
                  context={'department': department, 'user': request.user.employee, })


@login_required
def job_applications(request):
    department = request.user.employee.dept
    return render(request, 'HR/job_applications.html',
                  context={'department': department, 'user': request.user.employee, })
