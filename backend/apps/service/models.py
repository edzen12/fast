from django.db import models


class Service(models.Model):
    title = models.CharField(verbose_name="Название", max_length=255)
    image_icon = models.ImageField(
        verbose_name="Фото иконка", 
        upload_to="service/", 
        blank=True, null=True,
        help_text="можно взять из сайта  https://www.flaticon.com/"
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Услуги"

    
     

