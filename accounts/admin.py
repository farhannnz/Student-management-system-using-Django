from django.contrib import admin
from .models import Course,  Semester, Subject, Teacher, Student, Examination, ExaminationMark, Internal, Attendance,Monthyl_Attendance

class ExaminationMarkAdmin(admin.ModelAdmin):
  list_display = ('student', 'subject', 'examination', 'marks')
  list_filter = ('subject', 'examination')

  def get_queryset(self, request):
      qs = super().get_queryset(request)
      if request.user.is_superuser:
          return qs
      try:
          teacher = Teacher.objects.get(user=request.user)
          return qs.filter(subject__in=teacher.subjects.all())
      except Teacher.DoesNotExist:
          return qs.none()

  def has_change_permission(self, request, obj=None):
      if not obj:
          return True
      try:
          teacher = Teacher.objects.get(user=request.user)
          return obj.subject in teacher.subjects.all()
      except Teacher.DoesNotExist:
          return False

admin.site.register(Course)
admin.site.register(Semester)
admin.site.register(Subject)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Examination)
admin.site.register(ExaminationMark)
admin.site.register(Internal)
admin.site.register(Attendance)
admin.site.register(Monthyl_Attendance)
