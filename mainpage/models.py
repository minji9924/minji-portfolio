from django.db import models


# Create your models here.
class Grade(models.Model):
    subject_id = models.IntegerField(primary_key=True, db_comment='Subject id')
    subject_name = models.CharField(max_length=45, blank=True, null=True, db_comment='Subject name\n')
    subject_grade = models.CharField(max_length=45, blank=True, null=True, db_comment='Grade of the subject\\n')
    major = models.CharField(max_length=45, blank=True, null=True, db_comment='True if major false if else')
    credit = models.IntegerField(blank=True, null=True)
    semester = models.IntegerField(blank=True, null=True, db_comment='Semester of the subject\n')
    gpa = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'grade'
