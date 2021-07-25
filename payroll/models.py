from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.
class Employee_details(models.Model):
    
    Emp_id = models.CharField(max_length=20, primary_key=True, default = 'None')
    name = models.CharField(max_length=100, default = 'Enter name')
    PhoneNo = models.CharField(max_length=100, default = 'Enter phone number')
    Designation = models.CharField(max_length=100, default = 'None')
    Dept = models.CharField(max_length=100, default = 'None')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.user)
        
class Attendance(models.Model):
    No_of_Days_Punched_in = models.IntegerField(default=0)
    No_of_Duty_Days = models.IntegerField(default=0)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
 
    def __str__(self):
        return str(self.user)
    
class Leave(models.Model):
    Reason = models.CharField(max_length=20, default = 'None')
    No_of_days = models.IntegerField(default=0)
    From = models.DateTimeField(default=timezone.now)
    To = models.DateTimeField(default=timezone.now)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
 
    def __str__(self):
        return str(self.user)

        
class Duty_Schedule(models.Model):
    
    Month = models.CharField(max_length=20, default = 'None')
    Time_in = models.TimeField(default='00:00')
    Time_out = models.TimeField(default='00:00')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
 
    def __str__(self):
        return str(self.user)
 
class Salary_mgmt(models.Model):
    
    AC_No = models.CharField(max_length=200, primary_key=True, default = 'None')
    IFSC = models.CharField(max_length=200, default = 'None')
    Bank_name = models.CharField(max_length=200, default = 'None')
    Gross_Sal = models.IntegerField(default=0)
    Ded_amt = models.IntegerField(default=0)
    Desc = models.CharField(max_length=200, default = 'None')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def netsalary(self): #stored procedure
        return self.Gross_Sal-self.Ded_amt

    def __str__(self):
        return str(self.user)
 
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='user.png', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'    
        
    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height>300 or img.width>300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class announcements(models.Model):
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    @property
    def getdate(self):
        date = self.date_posted
        return date.strftime('%A %d %B %Y')

    def __str__(self):
        return str(self.date_posted)

class ex_employee(models.Model):
    
    name = models.CharField(max_length=100, default = 'None')
    PhoneNo = models.CharField(max_length=100, default = 'None')

    def __str__(self):
        return str(self.name)

