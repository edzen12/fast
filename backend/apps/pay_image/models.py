from django.db import models


class PayImage(models.Model):
    title = models.CharField(verbose_name="Заголовок", max_length=250)
    image = models.ImageField(
        verbose_name="Фото", 
        upload_to="pay_image/", 
        help_text="можно взять из сайта  https://www.flaticon.com/"
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Оплата(фото)"
    
