from django.db import models

# Create your models here.
class Voter_details(models.Model):
    fullname = models.Charfield(max_length=60)
    email=models.Emailfield()
    collegeid=models.Charfield()
    registration_number=models.Charfield()
    current_year=models.Charfield(max_length=1)
    department=models.Charfield()
class Candidate_details(models.Model):
    fullname = models.Charfield(max_length=60)
    works_done=models.Textfieldfield()
     department=models.Charfield()
class polling_details(models.Model):
    total_voters_registered=models.Charfield()
    votes_for_cand1=models.Charfield()
    votes_for_cand2=models.Charfield()
    votes_for_cand3=models.Charfield()
class login_details(models.Model):
    total_logins=models.Charfield()
    email_of_user=models.Emailfield()