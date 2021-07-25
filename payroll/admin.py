from django.contrib import admin

# Register your models here.
from .models import Employee_details, Attendance, Leave, Duty_Schedule, Salary_mgmt, Profile, announcements, ex_employee

admin.site.register(Employee_details)
admin.site.register(Attendance)
admin.site.register(Leave)
admin.site.register(Duty_Schedule)
admin.site.register(Salary_mgmt)
admin.site.register(Profile)
admin.site.register(announcements)
admin.site.register(ex_employee)
