# Generated by Django 5.0 on 2024-01-03 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chsb', '0007_remove_chsblar_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='chsblar',
            name='coun',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]
