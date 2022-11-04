from django.contrib import admin
from .models import SubmitFile, Secret

# Register your models here.
admin.site.register([SubmitFile, Secret])
