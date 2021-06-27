from django.db import models


class DataTarif(models.Model):
    name = models.CharField(verbose_name="Название", max_length=255)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Тариф"


class Tarif(models.Model):
    name = models.CharField(verbose_name="Название", max_length=255)
    price = models.CharField(
        verbose_name="Цена", max_length=250,
        blank=True, null=True,
        help_text="$25.00, от $370.00, комиссия х2, Бесплатно, от $35.00 в час, 5.00 %, от $0.30 - до $0.60"
    )
    cause_time = models.CharField(
        verbose_name="На кол-во/Время", 
        max_length=255,
        blank=True, null=True,
        help_text="за коробку, на поддон / мес, по звонку, на единицу"
    )

    data_tarif = models.ForeignKey(
        DataTarif, verbose_name="Тариф", 
        related_name='data_tarifs',
        blank=True, null=True, on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Данные Тарифа"