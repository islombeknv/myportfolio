# Generated by Django 3.2.3 on 2021-06-12 03:36

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_commentmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogmodel',
            name='content_en',
            field=models.TextField(null=True, verbose_name='content'),
        ),
        migrations.AddField(
            model_name='blogmodel',
            name='content_ru',
            field=models.TextField(null=True, verbose_name='content'),
        ),
        migrations.AddField(
            model_name='blogmodel',
            name='content_uz',
            field=models.TextField(null=True, verbose_name='content'),
        ),
        migrations.AddField(
            model_name='blogmodel',
            name='long_description_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='long_description'),
        ),
        migrations.AddField(
            model_name='blogmodel',
            name='long_description_ru',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='long_description'),
        ),
        migrations.AddField(
            model_name='blogmodel',
            name='long_description_uz',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='long_description'),
        ),
        migrations.AddField(
            model_name='blogmodel',
            name='title_en',
            field=models.CharField(max_length=255, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='blogmodel',
            name='title_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='blogmodel',
            name='title_uz',
            field=models.CharField(max_length=255, null=True, verbose_name='title'),
        ),
    ]
