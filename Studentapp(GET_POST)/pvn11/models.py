from django.db import models

# Create your models here.
class StudentApp(models.Model):
    name=models.CharField(max_length=30)
    rollno=models.IntegerField()
    marks=models.IntegerField()
    def __str__(self):
        return self.name
