# Generated by Django 5.0 on 2024-01-01 07:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pupils', '0004_remove_teacher_user_teacherregistr_delete_student_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TeacherRegistr',
        ),
    ]
