from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from recurring.models import BaseModel


class Class(BaseModel):
    title = models.CharField(max_length=255, blank=False, null=False, verbose_name=_("Название"))

    def __str__(self) -> str:
        return str(self.title)

    class Meta:
        db_table = "class"
        verbose_name = _("Класс")
        verbose_name_plural = _("Классы")


class Student(BaseModel):
    GENDER_CHOICES = [
        ('M', 'Мужской'),
        ('F', 'Женский'),
    ]
    name = models.CharField(max_length=255, blank=False, null=False, verbose_name=_("Имя ученика"))
    last_name = models.CharField(max_length=255, blank=False, null=False, verbose_name=_("Фамилия ученика"))
    middle_name = models.CharField(max_length=255, blank=False, null=False, verbose_name=_("Отчество ученика"))
    email = models.EmailField(max_length=255, unique=True, blank=False, null=False, verbose_name=_("Почта ученика"))
    birth_date = models.DateField(blank=False, null=False, verbose_name=_("Дата рождения"))
    address = models.CharField(max_length=255, unique=True, blank=False, null=False, verbose_name=_("Адрес ученика"))
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=False, null=False, verbose_name=_("Пол"))
    photo = models.ImageField(upload_to="back_media/%Y/%m/%d/", blank=True, null=False,
                              verbose_name=_("Изображение"),
                              validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])])
    class_item = models.ForeignKey(
        Class,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        verbose_name=_("Класс"),
        related_name="students"
    )

    def __str__(self) -> str:
        return str(self.name)

    class Meta:
        db_table = "student"
        verbose_name = _("Ученик")
        verbose_name_plural = _("Ученики")


class TitleItem(BaseModel):
    title = models.CharField(max_length=255, blank=False, null=False, verbose_name=_("Название предмета"))

    def __str__(self) -> str:
        return str(self.title)

    class Meta:
        db_table = "title_item"
        verbose_name = _("Название предмета")
        verbose_name_plural = _("Название предметов")


class School(BaseModel):
    title = models.CharField(max_length=255, blank=False, null=False, verbose_name=_("Название школы"))
    classes = models.ManyToManyField(
        Class,
        blank=False,
        related_name="schools",
        verbose_name=_("Классы")
    )

    def __str__(self) -> str:
        return str(self.title)

    class Meta:
        db_table = "school"
        verbose_name = _("Школа")
        verbose_name_plural = _("Школы")
