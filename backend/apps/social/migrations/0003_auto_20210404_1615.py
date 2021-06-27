# Generated by Django 3.1.7 on 2021-04-04 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0002_auto_20210330_1317'),
    ]

    operations = [
        migrations.AddField(
            model_name='social',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='social',
            name='title_en',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='social',
            name='title_ru',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='social',
            name='link',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Ссылка на соц.сеть'),
        ),
    ]
