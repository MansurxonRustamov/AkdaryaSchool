# Generated by Django 5.0 on 2024-01-01 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=120)),
                ('telefon_raqam', models.BigIntegerField()),
                ('xabar', models.TextField()),
            ],
        ),
    ]
