# Generated by Django 4.1.4 on 2023-03-05 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_faq_alter_writers_options_alter_writers_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='writers',
            name='back',
            field=models.ImageField(default='', upload_to='img/', verbose_name='фото'),
        ),
    ]