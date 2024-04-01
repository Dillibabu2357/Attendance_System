from django.db import models            
# imported models form django.db


class Attendance(models.Model):
    student_name=models.CharField(max_length=30) 
    day=models.DateField() 
    percentage=models.FloatField()
    subject=models.CharField(max_length=20) 
    roll_no=models.IntegerField() 

    def __str__(self) -> str:
         return f"{self.student_name} --- {self.percentage}"


class Meta:
        unique_together = ('stud_name', 'subject')

class Teacher(models.Model):
    name=models.CharField(max_length=30)
    subject=models.CharField(max_length=20) 
    period=models.IntegerField() 
    cls=models.CharField(max_length=20) 
    id=models.IntegerField(primary_key=True)

    def __str__(self) -> str:
         return f"{self.name} --- {self.subject}"
    

    # def __str__(self) -> str:
    #      return f"{self.subject} && {self.marks}"


class Meta:
    unique_together = ('stud_name', 'subject')

# student table  
class Student(models.Model):              #table_name is Student, by using class keyword we can create table
    roll_no=models.AutoField(primary_key=True)           # roll_no column is unique,so it is primary key 
    attend_percent=models.IntegerField() 
    subject=models.CharField(max_length=20) 
    name=models.CharField(max_length=30)

    def __str__(self) -> str:
         return f"{self.name} --- {self.subject}"
    

class Marks(models.Model):
    student_rn=models.ForeignKey(Student, on_delete=models.CASCADE)
    subject=models.CharField(max_length=20) 
    marks=models.IntegerField() 
    teacher_id=models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self) -> str:
         return f"{self.student_rn} --- {self.marks}"