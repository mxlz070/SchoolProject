from rest_framework import viewsets
from rest_framework import filters
from app.school import models, serializers


class StudentViewSet(viewsets.ModelViewSet):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


class TitleItemViewSet(viewsets.ModelViewSet):
    queryset = models.TitleItem.objects.all()
    serializer_class = serializers.TitleItemSerializer


class SchoolViewSet(viewsets.ModelViewSet):
    queryset = models.School.objects.all()
    serializer_class = serializers.SchoolSerializer


class ClassViewSet(viewsets.ModelViewSet):
    queryset = models.Class.objects.all()
    serializer_class = serializers.ClassSerializer
