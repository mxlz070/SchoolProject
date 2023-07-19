from django.urls import path
from app.school import views


urlpatterns = [
    path('api/v1/students/', views.StudentViewSet.as_view(), name="students-list"),
    path('api/v1/class/', views.ClassViewSet.as_view(), name="class-list"),
    path('api/v1/title_item/', views.TitleItemViewSet.as_view(), name="title-item-list"),
    path('api/v1/school/', views.SchoolViewSet.as_view(), name="school-list"),
]
