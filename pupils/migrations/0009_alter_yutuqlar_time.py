# Generated by Django 5.0 on 2024-01-01 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pupils', '0008_yutuqlar_alter_teachers_image_alter_teachers_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yutuqlar',
            name='time',
            field=models.DateField(),
        ),
    ]