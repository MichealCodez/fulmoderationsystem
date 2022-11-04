from django.urls import path
from .views import login, secret_code
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("login/", login, name="login"),
    path("go/", login_required(secret_code), name="secret")
]