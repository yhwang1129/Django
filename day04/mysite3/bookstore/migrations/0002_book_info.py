# Generated by Django 2.2.12 on 2024-09-29 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='info',
            field=models.CharField(default='', max_length=100, verbose_name='描述'),
        ),
    ]
