# Generated by Django 5.0 on 2024-01-03 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pupils', '0012_students_full_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='grade',
            field=models.CharField(choices=[('501', 501), ('501', 502), ('501', 503), ('601', 601), ('601', 602), ('601', 603), ('701', 701), ('701', 702), ('701', 703), ('801', 801), ('801', 802), ('801', 803), ('901', 901), ('901', 902), ('901', 903), ('1001', 1001), ('1001', 1002), ('1001', 1003), ('11', 11)], max_length=120),
        ),
    ]
