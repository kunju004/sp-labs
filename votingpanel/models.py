from django.db import models

# Create your models here.
class Voter(models.Model):
    STATUS = (
            ('Pending', 'Pending'),
            ('Voted', 'Voted'),
            )
    college_id = models.CharField(max_length=8, null=True)
    voter_name = models.CharField(max_length=30, null=True)
    voter_department = models.CharField(max_length=20, null=True)
    academic_year = models.CharField(max_length=1, null=True)
    email = models.CharField(max_length=40, null=True)
    date_of_birth = models.DateField(null=True)
    voting_status = models.CharField(max_length=10, null=True, choices=STATUS)
    def __str__(self):
       return self.voter_name

class Tag(models.Model):
    voter_name = models.CharField(max_length=30, null=True)
    
    def __str__(self):
       return self.voter_name
         
class Candidate(models.Model):
    Candidate_name = models.CharField(max_length=20, null=True)
    Candidate_department = models.CharField(max_length=20, null=True)
    Candidate_party_name = models.CharField(max_length=20, null=True)
    Candidate_work = models.CharField(max_length=20, null=True) 

    def __str__(self):
       return self.Candidate_name

class Poll(models.Model):
    Voter = models.ForeignKey(Voter, null=True, on_delete= models.SET_NULL)
    Candidate = models.ForeignKey(Candidate, null=True, on_delete= models.SET_NULL)