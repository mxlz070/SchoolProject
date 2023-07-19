from django.contrib import admin
from teacher import models


@admin.register(models.Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ["phone", "class_title"]
    list_display_links = ["phone", "class_title"]
    search_fields = ["phone", "class_title", "title_item__name"]
    fields = ["phone", "class_title", "title_item"]



