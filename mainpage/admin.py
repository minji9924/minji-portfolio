from django.contrib import admin
from mainpage.models import Grade


# Register your models here.
class GradeAdmin(admin.ModelAdmin):
    list_display = ('subject_id', 'subject_name', 'subject_grade',
                    'major', 'credit', 'semester')


admin.site.register(Grade, GradeAdmin)
