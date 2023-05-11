
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages



# Create your views here.

#login
def signin(request):
    if request.method == 'POST':
        email = request.POST['email']
        pass1 = request.POST['pass1']
        
        user = authenticate(username=email, password=pass1)
        
        if user is not None:
            login(request, user)
            # fname = user.first_name
            # messages.success(request, "Logged In Sucessfully!!")
            # print(user.is_company)
            if user.is_company == True:
                return redirect('company')
            else:
                return redirect('employee')

        else:
            messages.error(request, "The email or password is incorrect.")
            
    
    return render(request, "login.html")

#singout

def signout(request):
    logout(request)
    
    return redirect('login')
