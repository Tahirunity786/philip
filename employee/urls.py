from django.urls import path
from employee.views import *
urlpatterns = [
    path('', index, name="Ehome"),
    path('e-insight', insight, name="Insight"),
    
    
    # Authentication
    path('e-login-view', login_view, name="Login"),
    path('e-register', register, name="Register"),
    path('e-logout', logout_view, name="Logout"),
    path('e-profile', profile, name="Profile"),
    path('e-attendance', attendance, name="Attendance"),
    path('e-attendance-summary', attendance_summary, name="Attendance Summary"),
    path('e-settings', settings, name="Settings"),
    path('e-help', support, name="Support"),
    path('e-announcement', announcement, name="Announcement"),
    path('e-news', news, name="News"),
    path('e-newsletter', newsletter, name="Newsletter"),
    path('e-payslip', payslip, name="Payslip"),
    path('e-giudeline', giudeline, name="Guidelines"),
    path('e-birthday', birthday, name="Birthday"),
    path('e-holiday', holiday, name="Holiday"),
    path('e-lock-profile', lock_view, name="Lock"),

    # API AREA

    # path('e-login-verify', LoginAPIView.as_view(), name="LoginAPI"),
]