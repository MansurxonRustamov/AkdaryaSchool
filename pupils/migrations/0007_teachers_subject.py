# Generated by Django 5.0 on 2024-01-01 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pupils', '0006_teachers'),
    ]

    operations = [
        migrations.AddField(
            model_name='teachers',
            name='subject',
            field=models.CharField(choices=[('0', 'Matematik'), ('1', 'Ingliz Tili'), ('2', 'Tarix'), ('3', 'Huquq')], default=1, max_length=120),
            preserve_default=False,
        ),
    ]
