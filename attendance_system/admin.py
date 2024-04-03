from django.contrib import admin
from .models import Attendance,Teacher,Student,Marks,subject,Teacher_has_subject

admin.site.register(Attendance)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Marks)
