from django.shortcuts import render, redirect
from lecturer.models import SubmitFile, WrongFile
from django.views import generic
from django.contrib.auth import logout as out

class MainView(generic.ListView):
    model = SubmitFile
    template_name = 'main/main.html'
    context_object_name = 'files'
    paginate_by = 15
    ordering = ['-id']


class WrongView(generic.ListView):
    model = WrongFile
    template_name = 'main/wrong.html'
    context_object_name = 'files'
    paginate_by = 15
    ordering = ['-id']


def logout(request):
    out(request)
    return redirect('/accounts/login/')
    