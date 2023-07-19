from rest_framework import serializers
from app.school.models import (
    Student,
    TitleItem,
    School,
    Class
)


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"
        read_only_fields = fields


class TitleItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TitleItem
        fields = "__all__"
        read_only_fields = fields


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = "__all__"
        read_only_fields = fields


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = "__all__"
        read_only_fields = fields
