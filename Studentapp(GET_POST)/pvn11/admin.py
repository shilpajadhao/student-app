from django.contrib import admin
from .models import StudentApp


# Register your models here.
class StudentAppAdmin(admin.ModelAdmin):
    list_display=["name","rollno","marks",]
admin.site.register(StudentApp,StudentAppAdmin)
