from django.db import models


class SubmitFile(models.Model):
    course = models.CharField(max_length=50)
    session = models.CharField(max_length=12)
    semester = models.IntegerField()
    lecturer = models.CharField(max_length=50)
    uploaded_file = models.FileField(upload_to='')


class WrongFile(models.Model):
    course = models.CharField(max_length=50)
    session = models.CharField(max_length=12)
    semester = models.IntegerField()
    lecturer = models.CharField(max_length=50)


class Secret(models.Model):
    secret = models.CharField(max_length=500)