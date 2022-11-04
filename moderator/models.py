from django.db import models


class Response(models.Model):
    course = models.CharField(max_length=50)
    session = models.CharField(max_length=12)
    semester = models.IntegerField()
    moderator = models.CharField(max_length=50)
    status = models.CharField(max_length=20)
    message = models.CharField(max_length=1000)
