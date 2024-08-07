# Generated by Django 4.1.4 on 2023-02-15 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Writers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, verbose_name='имя и фимилия')),
                ('surname', models.CharField(max_length=20, verbose_name='фамилия на английском')),
                ('photo', models.ImageField(upload_to='', verbose_name='фото')),
                ('description', models.CharField(max_length=100, verbose_name='краткое описание')),
                ('full_description', models.TextField(verbose_name='полное описание')),
            ],
        ),
    ]