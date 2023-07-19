from django.db import models
import uuid
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    identifier = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True,
        verbose_name=_("ID")
    )
    is_removed = models.BooleanField(
        default=False,
        verbose_name=_('Удалить?')
    )
    created_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('дата создания')
    )
    updated_date = models.DateTimeField(
        auto_now=True,
        verbose_name=_('дата изменения')
    )

    class Meta:
        abstract = True
