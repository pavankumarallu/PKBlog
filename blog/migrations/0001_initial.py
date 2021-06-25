# Generated by Django 3.2.4 on 2021-06-24 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('overview', models.TextField()),
                ('time_upload', models.DateTimeField(auto_now_add=True)),
                ('thumbnail', models.ImageField(upload_to='thumbnails')),
                ('categories', models.ManyToManyField(to='blog.Category')),
            ],
        ),
    ]