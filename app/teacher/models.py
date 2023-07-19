from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from school.models import Class, TitleItem


class Teacher(AbstractUser):
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message=_("Номер телефона должен быть в формате: '+999999999'. Максимальное количество цифр - 15."),
    )
    phone = models.CharField(
        max_length=15,
        validators=[phone_regex],
        blank=False,
        null=False,
        verbose_name=_("Номер телефона"),
    )
    class_title = models.ForeignKey(
        Class,
        on_delete=models.CASCADE,
        verbose_name=_("Название класса"),
        related_name="teachers",
        blank=False,
        null=True,
    )
    title_item = models.ManyToManyField(
        TitleItem,
        verbose_name=_("Предметы, которые ведёт учитель"),
        related_name="teachers",
        blank=False,
        null=True,
    )

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['phone']

    def __str__(self):
        return str(self.phone)

    class Meta:
        db_table = "teacher"
        verbose_name = _("Учитель")
        verbose_name_plural = _("Учителя")
