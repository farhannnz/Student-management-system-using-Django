from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Student, ExaminationMark, Attendance, Monthyl_Attendance, Internal, Subject, Teacher


# Login View
def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to the home page
        else:
            messages.error(request, "Invalid username or password")
    return render(request, 'login.html')


# Student's Home Page - Displays basic info about the student
@login_required
def home(request):
    student = get_object_or_404(Student, user=request.user)
    context = {
        'student': student
    }
    return render(request, 'home.html', context)


# Student's Marks Page - Displays student's examination marks
@login_required
def marks(request):
    student = get_object_or_404(Student, user=request.user)
    marks = ExaminationMark.objects.filter(student=student).select_related('subject', 'examination')

    examination_marks = {}
    total_marks = 0
    max_marks = 0

    for mark in marks:
        if mark.examination.name not in examination_marks:
            examination_marks[mark.examination.name] = []
        examination_marks[mark.examination.name].append(mark)
        total_marks += mark.marks
        max_marks += 100  # Assuming max marks is 100 for each subject

    percentage = (total_marks / max_marks) * 100 if max_marks > 0 else 0

    context = {
        'examination_marks': examination_marks,
        'total_marks': total_marks,
        'max_marks': max_marks,
        'percentage': percentage,
    }
    return render(request, 'mark.html', context)


# Student's Attendance Page
@login_required
def user_attendance(request):
    student = get_object_or_404(Student, user=request.user)
    user_attendance = Attendance.objects.filter(student=student)

    context = {
        'attendances': user_attendance
    }
    return render(request, 'user_attendance.html', context)


# Student's Monthly Attendance Page
@login_required
def monthly_user_attendance(request):
    student = get_object_or_404(Student, user=request.user)
    user_attendance = Monthyl_Attendance.objects.filter(student=student)

    context = {
        'attendances': user_attendance
    }
    return render(request, 'monthly_attendance.html', context)


# Teacher's Home Page - Displays students and subjects the teacher manages
@login_required
def teacher_homepage(request):
    teacher = get_object_or_404(Teacher, user=request.user)
    subjects = teacher.subjects.all()
    students = Student.objects.filter(semester__subjects__in=subjects).distinct()

    context = {
        'teacher': teacher,
        'students': students,
        'subjects': subjects,
    }
    return render(request, 'teacher_homepage.html', context)


# Add Marks View - Allows teacher to add marks for a student in a subject
@login_required
def add_marks(request, student_id, subject_id):
    teacher = get_object_or_404(Teacher, user=request.user)
    student = get_object_or_404(Student, id=student_id)
    subject = get_object_or_404(Subject, id=subject_id)

    if subject not in teacher.subjects.all():
        return HttpResponseForbidden("You don't have permission to add marks for this subject.")

    if request.method == 'POST':
        internal, created = Internal.objects.get_or_create(student=student, subject=subject)
        exam_marks, created = ExaminationMark.objects.get_or_create(student=student, subject=subject)

        # Updating internal marks
        internal.assignment_1 = request.POST.get('assignment_1', 0)
        internal.assignment_2 = request.POST.get('assignment_2', 0)
        internal.mid_1 = request.POST.get('mid_1', 0)
        internal.mid_2 = request.POST.get('mid_2', 0)
        internal.save()

        # Updating exam marks
        exam_marks.marks = request.POST.get('exam_marks', 0)
        exam_marks.save()

        messages.success(request, "Marks updated successfully!")
        return redirect('teacher_homepage')

    context = {
        'student': student,
        'subject': subject,
    }
    return render(request, 'add_marks.html', context)