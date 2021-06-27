from django.db import models


class FormEmail(models.Model):
    fullname = models.CharField(
        verbose_name="ФИО", max_length=255, db_index=True, blank=True, null=True
    )
    number = models.CharField(
        verbose_name="Номер телефона", max_length=21
    )

    def __str__(self):
        return f"{self.fullname}, {self.number}"

    class Meta:
        ordering = ('-id',)
    