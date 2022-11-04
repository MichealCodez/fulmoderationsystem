from django.shortcuts import render, redirect
from .models import SubmitFile, WrongFile
from django.contrib import messages
from moderator.models import Response
from django.views import generic


def submit_paige(request):
    if request.method == 'POST':
        course = request.POST['course']
        session = request.POST['session']
        semester = request.POST['semester']
        lecturer = request.POST['lecturer']
        lecturer = lecturer.split(" ")
        lecli = []
        for i in lecturer:
            i = i.capitalize()
            lecli.append(i)
        lecturer = " ".join(lecli)
        file = request.FILES['file']
        b = WrongFile(course=course, session=session, semester=semester, lecturer=lecturer)
        b.save()
        a = SubmitFile(course=course, session=session, semester=semester, lecturer=lecturer, uploaded_file=file)
        a.save()
        messages.success(request, 'File Uploaded Successfully!')
        return redirect('/')
    else:
        return render(request, 'lecturer/form.html')


class ResponseView(generic.ListView):
    model = Response
    template_name = 'lecturer/response.html'
    context_object_name = 'response'
    paginate_by = 15
    ordering = ['-id']
