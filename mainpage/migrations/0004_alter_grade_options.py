# Generated by Django 4.2.6 on 2023-11-02 03:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0003_remove_grade_year_grade_gpa_alter_grade_table'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='grade',
            options={'managed': False},
        ),
    ]
