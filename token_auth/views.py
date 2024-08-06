from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.mail import send_mail
from django.conf import settings
import random

from .serializer import RegisterSerializer, VarifyUserSerializer, LoginSerializer, VarifySerializer
from app.models import Person

def send_email(email, otp):
    # email = "harshitsh409@gmail.com"
    message = f"""
    Please use the verification code below to sign in.

    {otp}

    If you didn’t request this, you can ignore this email.

    Thanks,
    The Accuknox team
    """
    try:
        send_mail(
            subject='Verification code',
            message=message,
            from_email= "pankaj787975@gmail.com",  #settings.EMAIL_HOST_USER,
            recipient_list=[email]
        )
    except Exception as e:
        return False
    return True

@api_view(['POST'])
def register(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        otp = random.randint(100000, 999999)
        email = serializer.data.get('email')
        person = Person.objects.get(email=email)
        person.otp = otp
        if not send_email(serializer.data.get('email'), otp):
            return Response("Something went wrong", status=400)
        person.save()
        return Response("your otp is sent", status=200)
        # return Response(serializer.data, status=201)
    else:
        return Response(serializer.errors, status=400)


@api_view(['POST'])
def varify_user(request):
    serializer = VarifyUserSerializer(data=request.data)
    if serializer.is_valid():
        return Response(f"User is varified", status=200)
    else:
        return Response(serializer.errors, status=400)

@api_view(['POST'])
def send_otp(request):
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        otp = random.randint(100000, 999999)
        email = serializer.data.get('email')
        person = Person.objects.get(email=email)
        person.otp = otp
        if not send_email(serializer.data.get('email'), otp):
            return Response("Something went wrong", status=400)
        person.save()
        return Response("your otp is sent", status=200)
    else:
        return Response(serializer.errors, status=400)


@api_view(['POST'])
def varify_otp(request):
    serializer = VarifySerializer(data=request.data)
    if serializer.is_valid():
        email = serializer.data.get('email')
        return Response(f"Welcome: {email} ", status=200)
    else:
        return Response(serializer.errors, status=400)

