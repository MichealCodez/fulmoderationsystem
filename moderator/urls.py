from django.urls import path
from .views import response
from django.contrib.auth.decorators import login_required
from account.dec import secret_required


urlpatterns = [
    path('', secret_required(login_required(response)), name='respond'),
]
