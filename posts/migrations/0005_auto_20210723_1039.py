# Generated by Django 3.2.3 on 2021-07-23 05:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20210612_0836'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogmodel',
            name='content_ru',
        ),
        migrations.RemoveField(
            model_name='blogmodel',
            name='long_description_ru',
        ),
        migrations.RemoveField(
            model_name='blogmodel',
            name='title_ru',
        ),
    ]
