from django.db import models

# Create your models here.
class Voter_details(models.Model):
    fullname = models.CharField(max_length=60)
    email=models.CharField(max_length=60)
    collegeid=models.CharField(max_length=10)
    registration_number=models.CharField(max_length=20)
    current_year=models.IntegerField()
    department=models.CharField(max_length=15)