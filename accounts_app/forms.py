from django import forms
from . models import Employee
from . models import Company
from . models import Project
from . models import Empregistraion
# This is for employee
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"

#this is for company
class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = "__all__"

#class loginForm(forms.ModelForm):
    #class Meta:
        #model = Login
        #fields = "__all__"

class projectForm(forms.ModelForm):
    class Meta:
        model=Project
        fields = "__all__"

class EmpRegForm(forms.ModelForm):
    class Meta:
        model=Empregistraion
        fields = "__all__"

# class Emplogin(forms.ModelForm):
#     class Meta:
#         model=Emplogin
#         fields = "__all__"