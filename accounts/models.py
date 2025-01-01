from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Semester(models.Model):
    course = models.ForeignKey(Course, related_name='semesters', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.course.name} - {self.name}"

class Subject(models.Model):
    course = models.ForeignKey(Course, related_name='subjects', on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, related_name='subjects', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.course.name} - {self.semester.name})"

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    courses = models.ManyToManyField(Course, related_name='teachers')
    subjects = models.ManyToManyField(Subject, related_name='teachers')

    class Meta:
        permissions = [
            ("edit_marks", "Can edit marks for their subjects"),
        ]

    def __str__(self):
        return self.name

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    enrollment_number = models.CharField(max_length=20, unique=True)
    course = models.ForeignKey(Course, related_name='students', on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, related_name='students', on_delete=models.CASCADE)
    dob = models.DateField()

    def __str__(self):
        return self.name

class Examination(models.Model):
    name = models.CharField(max_length=100)
    course = models.ForeignKey(Course, related_name='examinations', on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, related_name='examinations', on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return f"{self.name} - {self.course.name} - {self.semester.name}"

class ExaminationMark(models.Model):
    student = models.ForeignKey(Student, related_name='examination_marks', on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, related_name='examination_marks', on_delete=models.CASCADE)
    examination = models.ForeignKey(Examination, related_name='examination_marks', on_delete=models.CASCADE)
    marks = models.IntegerField()

    def __str__(self):
        return f"{self.student.name} - {self.subject.name} - {self.examination.name}"

class Internal(models.Model):
    student = models.ForeignKey(Student, related_name='internals', on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, related_name='internals', on_delete=models.CASCADE)
    assignment_1 = models.CharField(max_length=2)
    assignment_2 = models.CharField(max_length=2)
    mid_1 = models.CharField(max_length=2)
    mid_2 = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.student.name} - {self.subject.name}"


from django.db import models
from django.contrib.auth.models import User

class Attendance(models.Model):

    student =  models. ForeignKey (Student, on_delete=models.CASCADE)
    
    date = models.DateField()
    status = models.CharField(max_length=10, choices=[('Present', 'Present'), ('Absent', 'Absent')])

    def __str__(self):
        return f"{self.student} - {self.date} - {self.status}"

class Monthyl_Attendance(models.Model):

      student =  models. ForeignKey (Student, on_delete=models.CASCADE)

      month = models.CharField(max_length=15)
      percentage = models.CharField(max_length=3)

def __str__(self):
        return f"{self.student} - {self.month}"
