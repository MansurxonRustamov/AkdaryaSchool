# Generated by Django 5.0 on 2024-01-01 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pupils', '0010_students'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='image',
            field=models.ImageField(upload_to='pupils/'),
        ),
    ]
