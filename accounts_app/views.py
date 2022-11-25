from multiprocessing import context
from django.conf import settings
from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth
from django.contrib import messages
from . models import PROJECT_CHOICE, Company,Employee, Empregistraion,Project
from . forms import CompanyForm, EmpRegForm,EmployeeForm,projectForm
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

# Create your views here.
def index(request):
    return render(request,'home.html')

# To create Company
@login_required
def comp(request):
    if request.method == "POST":

        form = CompanyForm(request.POST,request.FILES)
        if form.is_valid():
            try:
                form.save()
                return redirect("/show")
            except:
                pass
    else:
        form = CompanyForm()
    return render(request, "index.html", {'form':form})

# To retrieve Company details
@login_required
def show(request):
    companies = Company.objects.all()
    return render(request, "show.html", {'companies':companies})

# To Edit Company details
def edit(request, cName):
    company = Company.objects.get(cName=cName)
    return render(request, "edit.html", {'company':company})

# To Update Company
def update(request, cName):
    company = Company.objects.get(cName=cName)
    form = CompanyForm(request.POST,request.FILES, instance= company)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, "edit.html", {'company': company})

# To Delete Company details
def delete(request, cName):
    company = Company.objects.get(cName=cName)
    company.delete()
    return redirect("/show")


# To create employee
def emp(request):
    if request.method == "POST":

        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/showemp")
            except:
                pass
    else:
        form = EmployeeForm()
    return render(request, "addemp.html", {'form':form})

# To show employee details
@login_required()
def showemp(request):
    employees = Employee.objects.all()
    context={
        'employees':employees,
    }
    return render(request, "showemp.html", context)

# To delete employee details
def deleteEmp(request, eFname):
    employee = Employee.objects.get(eFname=eFname)
    employee.delete()
    return redirect("/showemp")

# To edit employee details
def editemp(request, eFname):
    employee = Employee.objects.get(eFname=eFname)
    return render(request, "editemployee.html", {'employee':employee})

# To update employee details
def updateEmp(request, eFname):
    employee = Employee.objects.get(eFname=eFname)
    form = EmployeeForm(request.POST, instance= employee)
    print('Hello1')
    if form.is_valid():
        
        form.save()
        return redirect("/showemp")
    return render(request, "editemployee.html", {'employee': employee})


# def loginCheck(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']

#         user = auth.authenticate(username = username, password = password)
#         if user is not None:
#             auth.login(request, user)
#             return redirect("/emp")
#         else:
#             messages.info(request, 'invalid credentials')
#             return redirect



#     else:
#         form = loginForm()
#         return render(request, "regsitration/login.html")

# project details__________________

@login_required()
def project(request):
    if request.method == "POST":

        form = projectForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/showstatus")
            except:
                pass
    else:
        form = projectForm()
    return render(request, "project.html", {'form':form})

@login_required()
def showstatus(request):
    projects = Project.objects.all() 
    projects_count= Project.objects.filter(project_status='on_progress').count()
    projects_count2=Project.objects.filter(project_status='approved').count()
    projects_count3=Project.objects.filter(project_status='tested').count()
    projects_count4=Project.objects.filter(project_status='completed').count()

    print('no of',projects_count)
    context={
        'projects':projects,
        'projects_count':projects_count,
        'projects_count2':projects_count2,
        'projects_count3':projects_count3,
        'projects_count4':projects_count4
    }
    return render(request, "show projects.html", context)

def deleteStatus(request,pk):
    project = Project.objects.filter(project_status=pk)
    project.delete()
    return redirect("/showstatus")

# # To edit project details
# def editeStatus(request, pk):
#     project = Project.objects.filter(project_title=pk)
#     return render(request, "editeproject.html",{'project':project})

# # To update project details
# def updateStatus(request, pk):
#     projects = Project.objects.filter(project_title=pk)
#     form = projectForm(request.POST)
#     print('Hello1')
#     if form.is_valid():
        
#         form.save()
#         return redirect("/showstatus")
#     return render(request, "editeproject.html", {'projects': projects})



#emp profile

@login_required()
def empProf(request):
    profile=Employee.objects.filter()
    context={
        'profile':profile
        }
    return render(request,'employeepro.html',context)

@login_required()
def empProf1(request):
    profile1=Employee.objects.filter(eCompany='turbolab')
    context={
        'profile1':profile1
        }
    return render(request,'employeepro2.html',context)


@login_required()
def empProf2(request):
    profile2=Employee.objects.filter(eCompany='tcs')
    context={
        'profile2':profile2
        }
    return render(request,'employeepro3.html',context)


# empolyee registeration
# 

def empReg(request):
      if request.method == "POST":
       form = EmpRegForm(request.POST)
       if form.is_valid():

            try:
                request.session["ema"]= emp.emp_email
                form.save()
                return redirect("emplogin/")
            except:
                pass
      else:
        form = EmpRegForm()
      return render(request,'emplyee_reg.html',{'form':form})

def emplogin(request):
    # user=Empregistraion.objects.all()
    if request.method=="POST":
        emailE=request.POST["email"]
        password=request.POST["pwd"]
        if Empregistraion.objects.filter(emp_email=emailE).exists():
            emp=Empregistraion.objects.get(emp_email=emailE)
            request.session["ema"]= emp.emp_email
            return redirect('ViewEmpProfile')
        else:
            messages.info(request,"Incorrect username and password")
    return render(request,'emp_login.html')

def ViewEmpProfile(request):  
    if request.method=="POST":
        emailE=request.POST["email"]
        password=request.POST["pwd"]
    if Empregistraion.objects.filter(emp_email=emailE).exists():
            emp=Empregistraion.objects.filter(emp_email=emailE)
    return render(request,'viewprofile.html',{'emp':emp})
