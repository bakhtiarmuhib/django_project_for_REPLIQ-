from django.db import models

from django.conf import settings
User = settings.AUTH_USER_MODEL
# Create your models here.

class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    company_address = models.CharField(max_length=255,blank=True,null=True)
    company_email = models.EmailField()

    def __str__(self):
        return self.company_name
    
class Employee(models.Model):
    gender_choices = [
        ('Male', 'Male'),
        ('Female', 'Female')
    ]
    company_name = models.ForeignKey(Company , on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    employee_name = models.CharField(max_length=255)
    employee_department_name = models.CharField(max_length=100,blank=True,null=True)
    employee_age = models.IntegerField()
    gender = models.CharField(max_length=20 , choices=gender_choices )

