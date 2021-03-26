from django.db import models
from django.contrib.auth.models import User

class Position(models.Model):
    title = models.CharField(max_length=50, unique=True)

<<<<<<< HEAD
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
=======
    def __str__(self):
        return self.title


class Candidate(models.Model):
    name = models.CharField(max_length=50, null=True)
    total_vote = models.IntegerField(default=0, editable=False)
    position = models.ForeignKey(Position, on_delete=models.CASCADE, null=True)
    
    
    def __str__(self):
        return "{} - {}".format(self.name, self.position.title)
>>>>>>> ec5b5560b9f4e382ecf7bb1c3086f149fc196e9b


class Voter(models.Model):
    name = models.CharField(max_length=50, null=True)
    branch = models.CharField(max_length=50, null=True)
    faculty = models.CharField(max_length=50, null=True)
    collegeid = models.CharField(max_length=50, unique=True, null=True)
    academicyear = models.CharField(max_length=50, null=True)
    def __str__(self):
<<<<<<< HEAD
        return self.username

class CountVote(models.Model):
    voterId = models.IntegerField(null=True)
    candidateId = models.IntegerField(null=True)
    positionId = models.IntegerField(null=True)

    def __str__(self):
        return self.voterId
=======
        return self.name


class ControlVote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

    def __str__(self):
        return "{} - {} - {}".format(self.user, self.position, self.status)
>>>>>>> ec5b5560b9f4e382ecf7bb1c3086f149fc196e9b
