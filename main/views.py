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
    def get_context_data(self,*args, **kwargs):
        context = super(MainView, self).get_context_data(*args,**kwargs)
        user_groups = self.request.user.groups.values_list('name',flat = True)
        context['group'] = list(user_groups) # self.request.user.groups.all()
        return context


class WrongView(generic.ListView):
    model = WrongFile
    template_name = 'main/wrong.html'
    context_object_name = 'files'
    paginate_by = 15
    ordering = ['-id']


def logout(request):
    out(request)
    return redirect('/accounts/login/')
    