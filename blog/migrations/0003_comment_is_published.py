# Generated by Django 3.2.7 on 2021-10-13 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20211013_0058'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='is_published',
            field=models.BooleanField(default=False, verbose_name='Опубликовано'),
        ),
    ]
