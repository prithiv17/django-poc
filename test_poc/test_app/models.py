from django.db import models

# Create your models here.

class Empdetails(models.Model):
    emp_id = models.CharField(max_length=100);
    emp_name = models.CharField(max_length=100);
    grade = models.CharField(max_length=100);    
    sub_grade = models.CharField(max_length=100);    
    skills = models.CharField(max_length=100);

    def __str__(self):
        return self.emp_name;
