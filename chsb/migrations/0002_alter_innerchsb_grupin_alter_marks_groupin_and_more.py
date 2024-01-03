# Generated by Django 5.0 on 2024-01-02 14:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chsb', '0001_initial'),
        ('pupils', '0012_students_full_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='innerchsb',
            name='grupIn',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chsb.chsblar'),
        ),
        migrations.AlterField(
            model_name='marks',
            name='GroupIn',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chsb.innerchsb'),
        ),
        migrations.AlterField(
            model_name='marks',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='pupils.students'),
        ),
    ]
