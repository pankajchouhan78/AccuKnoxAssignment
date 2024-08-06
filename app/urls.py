from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import views

urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path(
        "person/", views.PersonView.as_view()
    ),  # It shows the list of persons excluding itself
    path("register/", views.RegisterView.as_view()),
    path("search/", views.SearchView.as_view()),  # search by name or email
    path("send_request/", views.SendFriendRequest.as_view()),
    path("receive_request/", views.AcceptRequestView.as_view()),
    path("friend_list/", views.FriendListView.as_view()),
]
