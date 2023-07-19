from django.contrib import admin
from .models import Class, Student, TitleItem, School


@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_date', 'updated_date', 'is_removed')
    list_filter = ('is_removed',)
    search_fields = ('title',)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'email', 'class_item', 'created_date', 'updated_date', 'is_removed')
    list_filter = ('class_item', 'is_removed')
    search_fields = ('name', 'last_name', 'email')


@admin.register(TitleItem)
class TitleItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_date', 'updated_date', 'is_removed')
    list_filter = ('is_removed',)
    search_fields = ('title',)


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_date', 'updated_date', 'is_removed')
    list_filter = ('is_removed',)
    search_fields = ('title', 'classes__title')
