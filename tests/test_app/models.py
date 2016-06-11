from django.db import models
from reversion.models import Revision


class TestModel(models.Model):

    name = models.CharField(
        max_length=191,
        default="v1",
    )

    related_instances = models.ManyToManyField(
        "self",
        blank=True,
    )


class TestModelParent(TestModel):

    parent_name = models.CharField(
        max_length=191,
        default="parent v1",
    )


class TestMeta(models.Model):

    revision = models.ForeignKey(
        Revision,
        on_delete=models.CASCADE,
    )

    name = models.CharField(
        max_length=191,
    )
