from django.test import TestCase
from attendance_system.models import Attendance, Teacher, Student, Marks  # Import models directly from models.py
from datetime import date




class ModelTests(TestCase):
    def setUp(self):
        self.attendance = Attendance.objects.create(
            student_name='John Doe',
            day=date.today(),
            percentage=80.0,
            subject='Mathematics',
            roll_no=1
        )
        self.teacher = Teacher.objects.create(
            name='Mr. Smith',
            subject='Mathematics',
            period=1,
            cls='Class A',
            id=1
        )
        self.student = Student.objects.create(
            roll_no=1,
            attend_percent=80,
            subject='Mathematics',
            name='Alice'
        )
        self.marks = Marks.objects.create(
            student_rn=self.student,
            subject='Mathematics',
            marks=90,
            teacher_id=self.teacher
        )

    def test_attendance_table(self):
        # Test if attendance is created properly.
        self.assertEqual(self.attendance.student_name, 'John Doe')
        self.assertEqual(self.attendance.day, date.today())
        self.assertEqual(self.attendance.percentage, 80.0)
        self.assertEqual(self.attendance.subject, 'Mathematics')
        self.assertEqual(self.attendance.roll_no, 1)

    def test_teacher_table(self):
        # Test if teacher is created properly.
        self.assertEqual(self.teacher.name, 'Mr. Smith')
        self.assertEqual(self.teacher.subject, 'Mathematics')
        self.assertEqual(self.teacher.period, 1)
        self.assertEqual(self.teacher.cls, 'Class A')
        self.assertEqual(self.teacher.id, 1)

    def test_student_table(self):
        # Test if student is created properly.
        self.assertEqual(self.student.roll_no, 1)
        self.assertEqual(self.student.attend_percent, 80)
        self.assertEqual(self.student.subject, 'Mathematics')
        self.assertEqual(self.student.name, 'Alice')

    def test_marks_table(self):
        # Test if marks are created properly.
        self.assertEqual(self.marks.student_rn, self.student)
        self.assertEqual(self.marks.subject, 'Mathematics')
        self.assertEqual(self.marks.marks, 90)
        self.assertEqual(self.marks.teacher_id, self.teacher)



# class ModelTests(TestCase):
#     def setUp(self):
#         self.attendance = Attendance.objects.create(
#             student_name='John Doe',
#             day=date.today(),
#             percentage=80.0,
#             subject='Mathematics',
#             roll_no=1
#         )
#         self.teacher = Teacher.objects.create(
#             name='Mr. Smith',
#             subject='Mathematics',
#             period=1,
#             cls='Class A',
#             id=1
#         )
#         self.student = Student.objects.create(
#             roll_no=1,
#             attend_percent=80,
#             subject='Mathematics',
#             name='Alice'
#         )
#         self.marks = Marks.objects.create(
#             student_rn=self.student,
#             subject='Mathematics',
#             marks=90,
#             teacher_id=self.teacher
#         )

    def test_attendance_name(self):
        attendance = Attendance.objects.get(id=self.attendance.id)
        self.assertEqual(attendance.student_name, 'John Doe')
        # Add more assertions as needed

    def test_teacher_name(self):
        teacher = Teacher.objects.get(id=self.teacher.id)
        self.assertEqual(teacher.name, 'Mr. Smith')
        # Add more assertions as needed

    def test_student_name(self):
        student = Student.objects.get(roll_no=self.student.roll_no)
        self.assertEqual(student.name, 'Alice')
        # Add more assertions as needed

    def test_marks_marks(self):
        marks = Marks.objects.get(id=self.marks.id)
        self.assertEqual(marks.marks, 90)
