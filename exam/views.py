from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render


def is_student(user):
    return user.groups.filter(name='STUDENT').exists()


def home_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('after-login')
    return render(request, 'exam/index.html')


@user_passes_test(is_student)
def after_login_view(request):
    if is_student(request.user):
        return HttpResponseRedirect('student/student-dashboard')
