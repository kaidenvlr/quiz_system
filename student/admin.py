from django.contrib import admin

from student.models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['user.first_name', 'user.last_name', 'mobile']
