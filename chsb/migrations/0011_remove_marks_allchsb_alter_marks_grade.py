# Generated by Django 5.0 on 2024-01-03 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chsb', '0010_marks_allchsb'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='marks',
            name='allChsb',
        ),
        migrations.AlterField(
            model_name='marks',
            name='grade',
            field=models.CharField(choices=[('501', 501), ('502', 502), ('503', 503), ('601', 601), ('602', 602), ('603', 603), ('701', 701), ('702', 702), ('703', 703), ('801', 801), ('802', 802), ('803', 803), ('901', 901), ('902', 902), ('903', 903), ('1001', 1001), ('1002', 1002), ('1003', 1003), ('11', 11)], max_length=120),
        ),
    ]
