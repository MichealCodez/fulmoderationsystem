from functools import wraps
from django.shortcuts import redirect

def secret_required(function):
  @wraps(function)
  def wrap(request, *args, **kwargs):
        try:
            request.META['HTTP_REFERER']
        except:
            return redirect('/logout/')

        return function(request, *args, **kwargs)

  return wrap
