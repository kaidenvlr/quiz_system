from django.contrib.auth.views import LoginView
from django.urls import path

from student import views

urlpatterns = [
    path('student-click', views.student_click_view),
    path('student-login', LoginView.as_view(template_name='student/student_login.html'), name='student-login'),
    path('student-signup', views.student_signup_view, name='student-signup'),
    path('student-dashboard', views.student_dashboard_view, name='student-dashboard'),
    path('student-exam', views.student_exam_view, name='student-exam'),
    path('take-exam/<int:pk>', views.take_exam_view, name='take-exam'),
    path('start-exam/<int:pk>', views.start_exam_view, name='start-exam'),

    path('calculate-marks', views.calculate_marks_view, name='calculate-marks'),
    path('view-result', views.view_result_view, name='view-result'),
    path('check-marks/<int:pk>', views.check_marks_view, name='check-marks'),
    path('student-marks', views.student_marks_view, name='student-marks'),
    path('result_pupil/<int:pk>', views.pupil_result, name='view_result_pupil'),
]
