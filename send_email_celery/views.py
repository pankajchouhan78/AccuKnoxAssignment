from django.shortcuts import render
from django.http import HttpResponse
from app.models import Person
from django.utils import timezone


# Create your views here.
def test(request):
    today_date = timezone.now().date()
    print("today :", today_date)
    old_users = Person.objects.filter(date_joined__lt=today_date)
    new_users = Person.objects.filter(date_joined__gte=today_date)
    if (len(old_users) > 0):
        old_users_list = [user.email for user in old_users]
        if len(new_users) > 0:
            new_users_list = [user.email for user in new_users]
            print("old users :", old_users_list)
            print("new users :", new_users_list)
            new_user =  "new users : " + ' '.join(old_users_list)
            print("new user :", new_user)
    return HttpResponse("test")