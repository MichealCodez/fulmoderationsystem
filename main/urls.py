from django.urls import path
from .views import MainView, WrongView, logout
from django.contrib.auth.decorators import login_required
# from account.dec import secret_required

urlpatterns = [
    path('', login_required(MainView.as_view()),),
    path('home/', login_required(WrongView.as_view()),),
    path('logout/', login_required(logout), name="logout")
]
