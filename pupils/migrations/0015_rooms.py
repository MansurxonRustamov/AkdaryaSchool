# Generated by Django 5.0 on 2024-01-03 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pupils', '0014_alter_students_grade'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('image', models.ImageField(upload_to='rooms/')),
            ],
        ),
    ]
