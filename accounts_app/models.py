from secrets import choice
from django.db import models

# Create your models here.
from distutils.command.upload import upload

# Create your models here.

class Company(models.Model):
    cName = models.CharField(primary_key='true',max_length=50,unique='true')
    cEmail = models.EmailField()
    companyLogo = models.ImageField(upload_to="images",null=True)
    cUrl = models.CharField(max_length=50)
    class Meta:
        db_table = "company"

class Employee(models.Model):
    eFname = models.CharField(primary_key='true',max_length=50,unique='true')
    eLname = models.CharField(max_length=50)
    eCompany = models.ForeignKey(Company, on_delete=models.CASCADE)
    eEmail = models.EmailField()
    ePhone = models.CharField(max_length=50)
    class Meta:
        db_table = "employee"
    
class Login(models.Model):
    UserName = models.CharField(max_length=50)
    password = models.CharField(max_length=32)
    class Meta:
        db_table = "login"

PROJECT_CHOICE=(
    ('approved','approved'),
    ('on_progress','on_progress'),
    ('tested','tested'),
    ('completed','completed')
)
class Project(models.Model):
    project_title=models.CharField(primary_key='true',max_length=100,unique='true')
    project_value=models.CharField(max_length=50)
    contract_length=models.CharField(max_length=50)
    client_email=models.EmailField()
    client_phoneno=models.CharField(max_length=50)
    project_status=models.CharField(max_length=50,choices=PROJECT_CHOICE,default='status')

class Empregistraion(models.Model):
    First_name=models.CharField(primary_key='true',max_length=50,unique='true')
    Last_name=models.CharField(max_length=50)
    emp_email=models.EmailField()
    emp_phoneno=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    re_password=models.CharField(max_length=50)

