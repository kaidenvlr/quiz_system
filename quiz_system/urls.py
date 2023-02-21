from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, include

from exam import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/', include('student.urls')),

    path('', views.home_view, name=''),
    path('logout', LogoutView.as_view(template_name='exam/logout.html'), name='logout'),
    path('after-login', views.after_login_view, name='after-login'),
]
