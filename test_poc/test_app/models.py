from django.db import models
from django_mysql.models import ListCharField

# Create your models here.

class Empdetails(models.Model):
    emp_id = models.CharField(max_length=100);
    emp_name = models.CharField(max_length=100);
    grade = models.CharField(max_length=100);    
    sub_grade = models.CharField(max_length=100);   
    skills = models.CharField(max_length=100);
    # skills = ListCharField(
    #     base_field=models.CharField(max_length=10),
    #     size=6,
    #     max_length=(6 * 11)
    # );

    def __str__(self):
        return self.emp_name;


class CustomerDetails(models.Model):    
    register_as = models.CharField(max_length = 100);    
    first_name = models.CharField(max_length = 100);    
    last_name = models.CharField(max_length = 100,blank=True,null=True);    
    mail_id = models.CharField(max_length = 100);
    contact_number = models.CharField(max_length = 100);    
    country = models.CharField(max_length = 100);
    state = models.CharField(max_length = 100);    
    city = models.CharField(max_length = 100);
    street = models.CharField(max_length = 100);    
    gender = models.CharField(max_length = 100,blank=True,null=True);
    marital_status = models.CharField(max_length = 100,blank=True,null=True);    
    date_of_birth = models.DateField(blank=True,null=True);
    id_proof_type = models.CharField(max_length = 100);    
    id_proof_detail = models.CharField(max_length = 100);


    def __str__(self):
        return self.first_name;
