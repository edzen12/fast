from django.db import models


class LinkPrice(models.Model):
    linkprice = models.TextField(verbose_name="Ссылка")
    
    def __str__(self):
        return self.linkprice

    class Meta:
        verbose_name_plural = "Ссылка на Скачивание Прайслиста"
