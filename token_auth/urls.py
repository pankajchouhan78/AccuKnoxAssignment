from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register),
    path('varify_user/', views.varify_user),
    path('login/', views.send_otp),
    path('varify_otp/',views.varify_otp)
]
