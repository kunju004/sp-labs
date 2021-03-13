from django.views.generic import TemplateView
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import redirect, render
from django.contrib import auth
from django.contrib.auth.models import User,auth
from django.template.context_processors import csrf
from django.shortcuts import redirect, render
from votingpanel.models import Voter,Candidate,Position,Admin,CountVote
from django.views import generic
from django.contrib import messages
from django.contrib.auth import get_user_model

#Create your views here.

def ShowLoginPage(request):
    return render(request,"login.html")

def index(request):
    return render(request,"index.html")

def validate(request):
    if request.method == "POST":
        username = request.POST.get('email')
        password = request.POST.get('password')
        flag=0
        User = get_user_model()
        users = User.objects.all()
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            user = User.objects.get(username = username)
            u = user.id
            us = CountVote.objects.create(voterId = u)
            us.save()
            pos = Position.objects.all()
            return render(request,'displayPosition.html',{'positions': pos})
        else:
            error = 'Inavlid Username/Password'
            messages.info(request, error)
            return render(request,'login.html')

def displayPosition(request):
    return render(request,'displayPosition.html')

def logout(request):
    auth.logout(request)
    return render(request,'login.html')

def voting(request):
    return render(request,'voting.html')


def displaycandidate(request):
        if request.method == "POST":
            position = request.POST.get('position')
            us = request.user
            u = us.id
            p=Position.objects.get(id =position)
            position_id=p.id
            can = Candidate.objects.filter(position_id = position_id)
            check = CountVote.objects.filter(voterId = u, positionId = position_id)
            
            if check.exists():
                messages.error(request, 'Already voted')
                return render(request,'displayPosition.html')
            else:
                voter = CountVote.objects.filter(voterId = u).update(positionId = position_id)
            if can.exists():
                return render(request,'displayCandidate.html',{'candidates':can})
            else:
                messages.error(request, 'Candidates are not available for this position.')
                return render(request,'displayCandidate.html')

def submit(request):
    if request.method == "POST":
        can = request.POST.get('canname')
        c = Candidate.objects.get(candidateName = can)
        pos = c.position_id
        us = request.user
        u = us.id
        c = Candidate.objects.get(candidateName = can)
        candidate_id = c.id
        voter = CountVote.objects.filter(voterId = u , positionId = pos).update(candidateId = candidate_id)
        return render(request,'submit.html')

            
def adminLogin(request):
    return render(request,"adminLogin.html")

def check(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        flag=0
        ad = Admin.objects.all()
        for i in ad:
            if i.username==username and i.password==password:
                flag = 1
                return render(request,'admin.html')
                break
        if flag==0:
            error = 'Inavlid Username/Password'
            messages.info(request, error)
            return render(request,'adminLogin.html')
        
def admin(request):
    return render(request,"admin.html")

def addPosition(request):
    return render(request, "addPosition.html")

def positionDetails(request):
    if request.method == 'POST':
        title = request.POST.get('name','')
        Position.objects.create(title=title)
        messages.success(request, 'Position added successfully!!')
        return render(request,'addPosition.html')

def addCandidate(request):
    pos = Position.objects.all()
    #pos = Position.objects.raw('SELECT * FROM votingpanel_position where id =2 ')
    #pos = Position.objects.filter(id = 4)
    return render(request,'addCandidate.html',{'positions': pos})

def candidateDetails(request):
    if request.method == 'POST':
        candidateName=request.POST.get('candidateName','')
        position_id=request.POST.get('position','')
        position = Position.objects.get(id = position_id)
        email=request.POST.get('email','')
        Candidate.objects.create(candidateName = candidateName  , position = position , email=email)
        messages.success(request, 'Candidate added successfully!!')
        return addCandidate(request)

def addVoter(request):
    return render(request,"addVoter.html")

def voterDetails(request):
    if request.method == 'POST':
        voterName=request.POST.get('voterName','')
        collegeId=request.POST.get('id','')
        voterDepartment=request.POST.get('dept','')
        academic_year = request.POST.get('year','')
        email =request.POST.get('email','') 
        voting_status=request.POST.get('status','')
        voter = Voter(voterName=voterName,collegeId=collegeId,voterDepartment=voterDepartment,academic_year =academic_year ,email =email ,voting_status=voting_status)
        voter.save()
        username = request.POST.get('email','') 
        password = request.POST.get('id','')
        #user = User(username = username , password = password)
        user = User.objects.create_user(username = username , password = password)
        user.save()
        messages.success(request, 'Voter added successfully!!')
        return render(request,'addVoter.html')
        #return checking(request)

def checking(request):
    if request.method == 'POST':
        collegeId=request.POST.get('id','')
        for voter in Voter.objects.all():
            if voter.collegeId == collegeId:
                messages.error(request, 'college Id must be unique!!')
                return render(request,"addVoter.html")
        return render(request,"addVoter.html")
 
 



