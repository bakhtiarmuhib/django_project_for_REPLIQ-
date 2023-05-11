
from django.urls import path
from .views import *

urlpatterns = [
    path('company/', home_company , name= 'company'),
    path('employee/', home_employee , name= 'employee'),
    path('add_employee/', add_employee , name= 'add_employee'),
    path('add_employee_profile/<int:id>/', add_employee_profile , name= 'add_employee_profile'),
    path('user_activity/<int:id>/', user_activity_view , name= 'user_activity'),
]

