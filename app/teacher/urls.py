from django.urls import path

from .views import TeacherRegistrationView, TeacherLoginView

urlpatterns = [
    path('api/v1/register/', TeacherRegistrationView.as_view(), name='teacher-register'),
    path('api/v1/login/', TeacherLoginView.as_view(), name='teacher-login'),
]