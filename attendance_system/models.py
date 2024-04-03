from django.db import models

class Teacher(models.Model):
    teacher_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.EmailField(max_length=45)
    phone_no = models.IntegerField()
    experience = models.IntegerField()

    def _str_(self):
        return f"{self.first_name} {self.last_name}"

class Students(models.Model):
    roll_no = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    phone_no = models.BigIntegerField()  # Changed to BigIntegerField to handle larger numbers
    gender = models.CharField(max_length=45)
    email = models.EmailField(max_length=45)
    class_field = models.IntegerField()  # Changed to class_field to avoid conflict with Python keyword

    def _str_(self):
        return f"{self.first_name} {self.last_name}"

class Subject(models.Model):
    subject_id = models.AutoField(primary_key=True)
    subject_name = models.CharField(max_length=45)

    def _str_(self):
        return self.subject_name

class Teacher_has_Subject(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('teacher', 'subject'),)

    def _str_(self):
        return f"{self.teacher.first_name} {self.teacher.last_name} - {self.subject.subject_name}"

class Attendance(models.Model):
    id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    attendance_date = models.DateField()
    status = models.CharField(max_length=10)

    def _str_(self):
        return f"{self.student.first_name} {self.student.last_name} - {self.subject.subject_name} - {self.attendance_date}"

class Marks(models.Model):
    id = models.AutoField(primary_key=True)
    marks = models.IntegerField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def _str_(self):
        return f"{self.student.first_name} {self.student.last_name} - {self.subject.subject_name} - {self.marks}"
