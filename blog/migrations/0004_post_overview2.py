# Generated by Django 3.2.4 on 2021-06-26 03:41

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210626_0847'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='overview2',
            field=ckeditor.fields.RichTextField(null=True),
        ),
    ]
