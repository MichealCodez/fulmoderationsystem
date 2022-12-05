from django.shortcuts import render, redirect
from .models import Response
from django.contrib import messages


def response(request):
    if request.method == 'POST':
        course = request.POST['course']
        session = request.POST['session']
        semester = request.POST['semester']
        moderator = request.POST['moderator']
        status = request.POST['status']
        message = request.POST['message']
        moderator = moderator.split(" ")
        modli = []
        for i in moderator:
            i = i.capitalize()
            modli.append(i)
        moderator = " ".join(modli)
        b = Response(course=course, session=session, semester=semester,
                     moderator=moderator, status=status, message=message)
        b.save()
        messages.success(request, 'Response Submitted Successfully!')
        return redirect('/result/')
    else:
        return render(request, 'moderator/moderator.html')
