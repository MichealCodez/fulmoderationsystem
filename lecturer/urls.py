from django.urls import path
from .views import submit_paige
from django.contrib.auth.decorators import login_required
from account.dec import secret_required

urlpatterns = [
    path('', secret_required(login_required(submit_paige)), name='submit'),
]
