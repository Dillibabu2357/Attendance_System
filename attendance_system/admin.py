from django.contrib import admin
from .models import Attendance,Teacher,Student,Marks 

admin.site.register(Attendance)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Marks)