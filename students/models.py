from django.db import models

# Create your models here.

#creation of table 


# class SampleTable(models.Model):
#     age = models.IntegerField()
#     weight = models.FloatField(null=True)
#     price = models.DecimalField(max_digits=10, decimal_places=3)
#     name = models.CharField(max_length=150)
#     feedback = models.TextField()
#     date_of_birth = models.DateField(auto_now=True)

#     is_admin = models.BooleanField()


class Student(models.Model):
    name = models.CharField(max_length = 150)
    age =  models.IntegerField(default = 0)


    def __str__(self):
        return self.name


