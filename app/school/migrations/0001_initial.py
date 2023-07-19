# Generated by Django 4.2.2 on 2023-06-29 18:48

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('identifier', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True, verbose_name='ID')),
                ('is_removed', models.BooleanField(default=False, verbose_name='Удалить?')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='дата создания')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='дата изменения')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Класс',
                'verbose_name_plural': 'Классы',
                'db_table': 'class',
            },
        ),
        migrations.CreateModel(
            name='TitleItem',
            fields=[
                ('identifier', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True, verbose_name='ID')),
                ('is_removed', models.BooleanField(default=False, verbose_name='Удалить?')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='дата создания')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='дата изменения')),
                ('title', models.CharField(max_length=255, verbose_name='Название предмета')),
            ],
            options={
                'verbose_name': 'Название предмета',
                'verbose_name_plural': 'Название предметов',
                'db_table': 'title_item',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('identifier', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True, verbose_name='ID')),
                ('is_removed', models.BooleanField(default=False, verbose_name='Удалить?')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='дата создания')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='дата изменения')),
                ('name', models.CharField(max_length=255, verbose_name='Имя ученика')),
                ('last_name', models.CharField(max_length=255, verbose_name='Фамилия ученика')),
                ('middle_name', models.CharField(max_length=255, verbose_name='Отчество ученика')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Почта ученика')),
                ('birth_date', models.DateField(verbose_name='Дата рождения')),
                ('address', models.CharField(max_length=255, unique=True, verbose_name='Адрес ученика')),
                ('gender', models.CharField(choices=[('M', 'Мужской'), ('F', 'Женский')], max_length=1, verbose_name='Пол')),
                ('photo', models.ImageField(blank=True, upload_to='back_media/%Y/%m/%d/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])], verbose_name='Изображение')),
                ('class_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='school.class', verbose_name='Класс')),
            ],
            options={
                'verbose_name': 'Ученик',
                'verbose_name_plural': 'Ученики',
                'db_table': 'student',
            },
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('identifier', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True, verbose_name='ID')),
                ('is_removed', models.BooleanField(default=False, verbose_name='Удалить?')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='дата создания')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='дата изменения')),
                ('title', models.CharField(max_length=255, verbose_name='Название школы')),
                ('classes', models.ManyToManyField(related_name='schools', to='school.class', verbose_name='Классы')),
            ],
            options={
                'verbose_name': 'Школа',
                'verbose_name_plural': 'Школы',
                'db_table': 'school',
            },
        ),
    ]
