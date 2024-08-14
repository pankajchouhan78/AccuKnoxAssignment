
from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone
from app.models import Person

@shared_task
def test():
    print("testing started ..")


@shared_task
def send_scheduled_email():

    today_date = timezone.now().date()
    old_users = Person.objects.filter(date_joined__lt=today_date)
    new_users = Person.objects.filter(date_joined__gte=today_date)
    if (len(old_users) > 0):
        old_users_list = [user.email for user in old_users]
        if len(new_users) > 0:
            new_users_list = [user.name for user in new_users]
            # print("old users :", old_users_list)
            # print("new users :", new_users_list)
            new_user =  "new users : " + ' '.join(new_users_list)
            # print("new user :", new_user)

            message = new_user
            send_mail(
                subject='User Added',
                message=message,
                from_email= "pankaj787975@gmail.com",
                recipient_list=old_users_list
            )

