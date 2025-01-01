from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('', views.home, name='home'),  # Student's home page
    path('marks/', views.marks, name='marks'),  # Student's marks page
    path('attendance/', views.user_attendance, name='user_attendance'),  # Student's attendance page
    path('monthly-attendance/', views.monthly_user_attendance, name='monthly_attendance'),  # Student's monthly attendance
    path('teacher/', views.teacher_homepage, name='teacher_homepage'),  # Teacher's homepage
    path('teacher/add-marks/<int:student_id>/<int:subject_id>/', views.add_marks, name='add_marks'),  # Add marks by teacher
]
