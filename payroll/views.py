from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ProfileUpdateForm
from .models import *
from django.contrib.auth.models import User

def home(request): #handles traffic from home page
    a = announcements.objects.all()
    context = {
        'announcements' : a
    }
    return render(request, 'payroll/home.html', context)

def about(request): #handles traffic from home page
    a = announcements.objects.all()
    context = {
        'announcements' : a
    }
    return render(request, 'payroll/about.html', context)

@login_required
def profile(request):   #profile page
    a = announcements.objects.all()
    emp = Employee_details.objects.filter(user=request.user).first()
    schedule = Duty_Schedule.objects.filter(user=emp.user).first()
    print(request.user)
    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)#request.FILES is used to get the file uploaded by thr user in order to update
        
        if p_form.is_valid():
            p_form.save()
            messages.success(request, f'Your profile picture has been updated!')
            return redirect('profile') # to stop the message from the browser
    else:
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'announcements' : a,
        'p_form': p_form,
        'name': emp.name,
        'phone': emp.PhoneNo,
	    'designation': emp.Designation,
	    'username': emp.user.username,
        'email': emp.user.email,
	    'empid': emp.Emp_id,
        'schedule_month': schedule.Month,
        'schedule_time_in': schedule.Time_in,
        'schedule_time_out': schedule.Time_out

    }
    return render(request, 'payroll/profile.html', context)

@login_required
def attendance_leave(request): 
    a = announcements.objects.all()
    emp = Employee_details.objects.filter(user=request.user).first()
    attendance = Attendance.objects.filter(user=emp.user).first()
    leave = Leave.objects.filter(user=emp.user).first()
    print(request.user)
    context = {
        'announcements' : a,
        'name': emp.user.username,
        'email': emp.user.email,
        'empid': emp.Emp_id,
        'attendance': attendance.No_of_Days_Punched_in,
        'workingdays': attendance.No_of_Duty_Days,
        'myleave' : leave.No_of_days,
        'leavereason' : leave.Reason
    }
    return render(request, 'payroll/attendance.html', context)

@login_required
def salary(request): #handles traffic from home page
    a = announcements.objects.all()
    emp = Employee_details.objects.filter(user=request.user).first()
    leave = Leave.objects.filter(user=emp.user).first()
    salary = Salary_mgmt.objects.filter(user=emp.user).first()

    print(request.user)
    context = {
        'announcements' : a,
        'name': emp.user.username,
        'email': emp.user.email,
        'gross_salary' : salary.Gross_Sal,
        'deduction' : salary.Ded_amt,
        'deduction_reason' : salary.Desc,
        'accountno' : salary.AC_No,
        'ifsc' : salary.IFSC,
        'bankname' : salary.Bank_name,
        'netsal' : salary.netsalary()

    }
    return render(request, 'payroll/salary.html', context)

def deletetrigger(request):
    return render(request, 'payroll/confirmdelete.html')
    
def delete(request):
    user =  User.objects.get(username=request.user.username)
    employee = Employee_details.objects.get(user=request.user)
    ex = ex_employee.objects.create(name = employee.name, PhoneNo = employee.PhoneNo)
    ex.save()
    user.delete()
    return render(request, 'payroll/deleted.html')