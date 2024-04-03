from django.contrib import admin
from .models import Attendance,Teacher,Student,Marks,Subject,Teacher_has_subject

admin.site.register(Attendance)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Marks)
