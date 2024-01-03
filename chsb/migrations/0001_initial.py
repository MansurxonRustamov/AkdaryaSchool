# Generated by Django 5.0 on 2024-01-02 13:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CHSBlar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('time', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='InnerChsb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('grupIn', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='chsb.chsblar')),
            ],
        ),
        migrations.CreateModel(
            name='Marks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jamiBaho', models.FloatField()),
                ('algebra', models.FloatField()),
                ('geometriya', models.FloatField()),
                ('fizika', models.FloatField()),
                ('english', models.FloatField()),
                ('GroupIn', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='chsb.innerchsb')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]