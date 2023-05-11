from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user
from .models import *
from .froms import *
from accounts.models import user_activity

# Create your views here.


@login_required(login_url='login')
def home_company(request):
    print(get_user(request))
    all_employee = Employee.objects.filter(company_name__user = get_user(request))
    print(all_employee)

    return render(request, 'home_company.html',{
                                                'all_employee':all_employee,
                                            })


@login_required(login_url='login')
def home_employee(request):
    
    return render(request, 'home_employee.html')



@login_required(login_url='login')
def add_employee(request):
    fm=CustomUserCreationForm(request.POST)
    if request.method =="POST":
        if fm.is_valid():
            print('fm.valid data')
            fm.save()
            user_id = MyUser.objects.get(email=fm.cleaned_data['email'])
            return redirect('add_employee_profile' ,user_id.id)
            
            
    else:
         fm=  CustomUserCreationForm()    
    context={
        'form':fm
     }
    return render(request,'add_user.html',context)


@login_required(login_url='login')
def add_employee_profile(request,id):
    fm=Employee_add(request.POST)
    if request.method =="POST":
        if fm.is_valid():
            company = Company.objects.get(user =get_user(request))
            form_save = Employee(company_name =company,
                                    user =MyUser.objects.get(pk=id),
                                    employee_name =fm.cleaned_data['employee_name'],
                                    employee_department_name =fm.cleaned_data['employee_department_name'],
                                    employee_age =fm.cleaned_data['employee_age'],
                                    gender =fm.cleaned_data['gender']
                                    )
            form_save.save()
            return redirect('company' )
            
            
    else:
         fm=  Employee_add()    
    context={
        'form':fm
     }
    return render(request,'add_employee_profile.html',context)


@login_required(login_url='login')
def user_activity_view(request,id):
    all_activity = user_activity.objects.filter(user_id = id)

    return render(request,'user_activity.html',{'all_activity':all_activity})