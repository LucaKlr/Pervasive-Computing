from django.contrib import admin

# Register your models here.
from hftcheckin.models import *

admin.site.register(Student)
admin.site.register(Professor)
admin.site.register(Pruefung)
