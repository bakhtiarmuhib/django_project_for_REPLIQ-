from django.contrib.auth import user_logged_in,user_logged_out
from django.dispatch import receiver
from .models import user_activity
from datetime import datetime

@receiver(user_logged_in)
def user_log_in(sender,request,user,**kwargs):
    print(user)
    print('user log in')
    ip  = request.META.get('REMOTE_ADDR')
    print(ip)
    now = datetime.now()
    data = user_activity(user=user,login_time=now.strftime("%d/%m/%Y %H:%M:%S"),login_ip=ip)
    data.save()


@receiver(user_logged_out)
def user_logg_out(sender,request,user,**kwargs):
    print(user)
    ip  = request.META.get('REMOTE_ADDR')
    print(ip)
    try:
        now = datetime.now()
        get_login_user = user_activity.objects.get( user=user,login_ip=ip)
        get_login_user.logout_time = now.strftime("%d/%m/%Y %H:%M:%S")
        get_login_user.save()

    except:
        print('no track')