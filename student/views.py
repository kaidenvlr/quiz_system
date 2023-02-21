from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.shortcuts import render

from exam.models import Question, Course, Result
from student.forms import StudentUserForm, StudentForm
from student.models import Student


def student_click_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('after-login')
    return render(request, 'student/student_click.html')


def student_signup_view(request):
    user_form = StudentUserForm()
    student_form = StudentForm()
    res = {
        'userForm': user_form,
        'studentForm': student_form,
    }
    if request.method == 'POST':
        user_form = StudentUserForm(request.POST)
        student_form = StudentForm(request.POST)
        if user_form.is_valid() and student_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            student = student_form.save(commit=False)
            student.user = user
            student.save()

            my_student_group = Group.objects.get_or_create(name='STUDENT')
            my_student_group[0].user_set.add(user)
        return HttpResponseRedirect('student-login')
    return render(request, 'student/student_signup.html', context=res)


def is_student(user):
    return user.groups.filter(name='STUDENT').exists()


@login_required
@user_passes_test(is_student)
def student_dashboard_view(request):
    res = {
        'total_course': Course.objects.all().count(),
        'total_question': Question.objects.all().count(),
    }
    return render(request, 'student/student_dashboard.html', context=res)


@login_required
@user_passes_test(is_student)
def student_exam_view(request):
    courses = Course.objects.all()
    return render(request, 'student/student_exam.html', {'courses': courses})


@login_required
@user_passes_test(is_student)
def take_exam_view(request, pk):
    course = Course.objects.get(id=pk)
    total_questions = Question.objects.all().filter(course=course).count()
    questions = Question.objects.all().filter(course=course)
    total_marks = 0
    for q in questions:
        total_marks = total_marks + q.marks

    return render(request, 'student/take_exam.html',
                  {'course': course, 'total_questions': total_questions, 'total_marks': total_marks})


@login_required
@user_passes_test(is_student)
def start_exam_view(request, pk):
    course = Course.objects.get(id=pk)
    questions = Question.objects.all().filter(course=course)
    if request.method == 'POST':
        pass
    response = render(request, 'student/start_exam.html', {'course': course, 'questions': questions})
    response.set_cookie('course_id', course.id)
    return response


@login_required
@user_passes_test(is_student)
def calculate_marks_view(request):
    if request.COOKIES.get('course_id') is not None:
        course_id = request.COOKIES.get('course_id')
        course = Course.objects.get(id=course_id)

        total_marks = 0
        questions = Question.objects.all().filter(course=course)
        for i in range(len(questions)):

            selected_ans = request.COOKIES.get(str(i + 1))
            actual_answer = questions[i].answer
            if selected_ans == actual_answer:
                total_marks = total_marks + questions[i].marks
        student = Student.objects.get(user_id=request.user.id)
        result = Result()
        result.marks = total_marks
        result.exam = course
        result.student = student
        result.save()

        return HttpResponseRedirect('view-result')


@login_required
@user_passes_test(is_student)
def view_result_view(request):
    courses = Course.objects.all()
    return render(request, 'student/view_result.html', {'courses': courses})


@login_required
@user_passes_test(is_student)
def check_marks_view(request, pk):
    course = Course.objects.get(id=pk)
    student = Student.objects.get(user_id=request.user.id)
    results = Result.objects.all().filter(exam=course).filter(student=student)
    return render(request, 'student/check_marks.html', {'results': results})


@login_required
@user_passes_test(is_student)
def student_marks_view(request):
    courses = Course.objects.all()
    return render(request, 'student/student_marks.html', {'courses': courses})


@login_required
@user_passes_test(is_student)
def pupil_result(request, pk):
    result_pupil = Result.objects.all().filter(exam_id=pk)
    return render(request, 'student/result_pupil.html', {'result_pupil': result_pupil})
