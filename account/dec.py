from functools import wraps
from django.shortcuts import render, redirect
from lecturer.models import Secret
from django.http import HttpResponseRedirect

# def secret_required(function):
#   @wraps(function)
#   def wrap(request, *args, **kwargs):
#     try:
#       secret = Secret.objects.get(secret=request.POST['secret'])
#       print('here')
      
#       return redirect('/', secret=request.POST['secret'])
#     except:
#       if request.method == 'POST':
#         return redirect('/home/')
#       else:
#         return redirect('/accounts/go/')
#   return wrap
