from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password

from .models import Teacher


class TeacherSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    confirm_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Teacher
        fields = ('username', 'password', 'confirm_password', 'phone', 'class_title', 'title_item')

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        password = validated_data.pop('password')
        confirm_password = validated_data.pop('confirm_password')
        title_item = validated_data.pop('title_item')
        if password != confirm_password:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        teacher = Teacher.objects.create(**validated_data)
        teacher.set_password(password)
        teacher.save()
        teacher.title_item.set(title_item)
        return teacher
