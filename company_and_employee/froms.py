
from django.contrib.auth.forms import UserCreationForm  
from django import forms  
from accounts.models import MyUser 
from .models import Employee
from django.contrib.auth import get_user_model  
from django.db import models
  
User = get_user_model() 

class CustomUserCreationForm(UserCreationForm):  
  
    password1 = forms.CharField(widget=forms.PasswordInput)  
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)  
  
    class Meta:  
        model = MyUser  
        fields = ('email', )  
      
    def clean_email(self):  
        email = self.cleaned_data.get('email')  
        qs = User.objects.filter(email=email)  
        if qs.exists():  
            raise forms.ValidationError("Email is taken")  
        return email  
  
    def clean(self):  
        '''  
        Verify both passwords match.  
        '''  
        cleaned_data = super().clean()  
        password1 = cleaned_data.get("password1")  
        password2 = cleaned_data.get("password2")  
          
        if password1 is not None and password1 != password2:  
            self.add_error("password2", "Your passwords must match")  
        return cleaned_data  
  
    def save(self, commit=True):  
        # Save the provided password in hashed format  
        user = super().save(commit=False)  
        user.set_password(self.cleaned_data["password1"])  
        if commit:  
            user.save()  
        return user  




class Employee_add(forms.ModelForm):
    class Meta:
        model = Employee
        fields =['employee_name','employee_department_name','employee_age','gender']  