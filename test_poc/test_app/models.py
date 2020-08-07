from django.db import models
from django_mysql.models import ListCharField

# Create your models here.

class Empdetails(models.Model):
    emp_id = models.CharField(max_length=100);
    emp_name = models.CharField(max_length=100);
    grade = models.CharField(max_length=100);    
    sub_grade = models.CharField(max_length=100);    
    skills = ListCharField(
        base_field=models.CharField(max_length=10),
        size=6,
        max_length=(6 * 11)
    );

    def __str__(self):
        return self.emp_name;
