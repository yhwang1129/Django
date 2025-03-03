# Generated by Django 4.2.16 on 2024-10-21 02:11

from django.db import migrations, models
import user.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('username', models.CharField(max_length=11, primary_key=True, serialize=False, verbose_name='用户名')),
                ('nickname', models.CharField(max_length=30, verbose_name='昵称')),
                ('password', models.CharField(max_length=32)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=11)),
                ('avatar', models.ImageField(null=True, upload_to='avatar')),
                ('sign', models.CharField(default=user.models.default_sign, max_length=50, verbose_name='个人签名')),
                ('info', models.CharField(default='', max_length=150, verbose_name='个人简介')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'user_user_profile',
            },
        ),
    ]
