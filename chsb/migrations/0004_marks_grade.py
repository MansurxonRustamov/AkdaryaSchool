# Generated by Django 5.0 on 2024-01-02 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chsb', '0003_alter_marks_fizika_alter_marks_geometriya'),
    ]

    operations = [
        migrations.AddField(
            model_name='marks',
            name='grade',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
