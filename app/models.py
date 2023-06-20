from django.db import models

# Create your models here.
class Department(models.Model):
    dep_no=models.IntegerField(primary_key=True)
    dname=models.CharField(max_length=100)
    location=models.CharField(max_length=100)

    def __str__(self):
        return str(self.dep_no)

class EMP(models.Model):
    Emp_no=models.IntegerField(primary_key=True)
    Ename=models.CharField(max_length=100)
    Job=models.CharField(max_length=100)
    Dept_id=models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.Ename

class Capital(models.Model):
    capi=models.CharField(max_length=100)

    def __str__(self):
        return self.capi
        
class Country(models.Model):
    country_name=models.CharField(max_length=100)
    capital_name=models.OneToOneField(Capital,on_delete=models.CASCADE,primary_key=True,default=False)

    def __str__(self):
        return self.country_name

