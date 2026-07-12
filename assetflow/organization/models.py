# pyrefly: ignore [missing-import]
from django.db import models
# pyrefly: ignore [missing-import]
from django.conf import settings

# Create your models here.

class Department(models.Model):
    department_name = models.CharField(max_length=100)

    def __str__(self):
        return self.department_name

class EmployeeProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    employee_id=models.CharField(max_length=20,unique=True)
    
    department = models.ForeignKey(Department,on_delete=models.SET_NULL,null=True,blank=True)
    role = models.CharField(max_length=20,default="Employee")
    status = models.CharField(max_length=10,default="Active")

    def __str__(self):
        return self.employee_id
    
    
