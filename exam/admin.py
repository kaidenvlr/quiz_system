from django.contrib import admin

from exam.models import Course, Question, Result


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'max_points']


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['course.name', 'points', 'name', 'answer']


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ['student.get_name', 'course.name', 'points', 'date']
