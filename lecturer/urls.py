from django.urls import path
from .views import submit_paige, ResponseView
from django.contrib.auth.decorators import login_required
# from account.dec import secret_required

urlpatterns = [
    path('', login_required(submit_paige), name='submit'),
]
