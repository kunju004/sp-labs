from django.db import models

# Create your models here.
class Voter(models.Model):
    STATUS = (
            ('Pending', 'Pending'),
            ('Voted', 'Voted'),
            )
    collegeId = models.CharField(max_length=8,unique=True, null=True)
    voterName = models.CharField(max_length=30, null=True)
    voterDepartment = models.CharField(max_length=20, null=True)
    academic_year = models.CharField(max_length=1, null=True)
    email = models.CharField(max_length=40, null=True)
    voting_status = models.CharField(max_length=10, null=True, choices=STATUS)
    def __str__(self):
       return self.voterName


class Position(models.Model):
    title = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.title


class Candidate(models.Model):
    candidateName = models.CharField(max_length=50, null=True)
    #total_vote = models.IntegerField(default=0, editable=False)
    position = models.ForeignKey(Position, on_delete=models.CASCADE, null=True)
    email = models.CharField(max_length=40, null=True)
    
    
    def __str__(self):
        return "{} - {}".format(self.candidateName, self.position.title)

class Admin(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username

class CountVote(models.Model):
    voterId = models.IntegerField(null=True)
    candidateId = models.IntegerField(null=True)
    positionId = models.IntegerField(null=True)

    def __str__(self):
        return self.voterId