# Generated by Django 5.0 on 2024-01-03 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_newsschool_hashtag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsschool',
            name='hashtag',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
