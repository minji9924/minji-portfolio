# Generated by Django 4.2.6 on 2023-10-31 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('subject_id', models.IntegerField(db_comment='Subject id', primary_key=True, serialize=False)),
                ('subject_name', models.CharField(blank=True, db_comment='Subject name\n', max_length=45, null=True)),
                ('subject_grade', models.CharField(blank=True, db_comment='Grade of the subject\\n', max_length=45, null=True)),
                ('major', models.CharField(blank=True, db_comment='True if major false if else', max_length=45, null=True)),
                ('credit', models.IntegerField(blank=True, null=True)),
                ('year', models.IntegerField(blank=True, db_comment='Year of the subject\n', null=True)),
                ('semester', models.IntegerField(blank=True, db_comment='Semester of the subject\n', null=True)),
            ],
            options={
                'db_table': 'grade',
                'managed': False,
            },
        ),
    ]
