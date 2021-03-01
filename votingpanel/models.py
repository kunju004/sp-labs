from django.db import models

# Create your models here.
class Voter(models.Model):
    voter_id = models.CharField(max_length=8)
    voter_name = models.CharField(max_length=30)
    voter_department = models.CharField(max_length=20)
    academic_year = models.CharField(max_length=1)
    
    