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
from django.db.models import  Count

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
            pos = Position.objects.all()
            return render(request,'displayPosition.html',{'positions': pos})
        else:
            error = 'Inavlid Username/Password'
            messages.info(request, error)
            return render(request,'login.html')

def displayPosition(request):
    pos = Position.objects.all()
    return render(request,'displayPosition.html',{'positions': pos})

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
                messages.error(request, 'you have already been voted for this position.')
                return render(request,'displayPosition.html')
            else:
                voter = CountVote.objects.create(voterId = u , positionId = position_id)
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

def result(request):  
    candidates = Candidate.objects.all()
    results = []
    
    for candidate in candidates:
        result = {}
    
        countvote = CountVote.objects.filter(positionId = candidate.position_id , candidateId = candidate.id).count()
        result['can'] = candidate
        result['count'] = countvote
        results.append(result)
    return render(request,'result.html',{ 'results' : results })

    # can = Candidate.objects.all()
    # for i in can:
    #     countvote = CountVote.objects.filter(positionId = i.position_id , candidateId = i.id).count()
    #     candidate = Candidate.objects.filter(position_id = i.position_id , id = i.id).update(total_vote = countvote)
    # return render(request,'result.html',{ 'candidates' : can })

            
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
        user = User.objects.create_user(username = username , password = password)
        user.save()
        messages.success(request, 'Voter added successfully!!')
        return render(request,'addVoter.html')

def deleteVoter(request):
    voter = Voter.objects.all()
    return render(request,'deleteVoter.html',{'voters': voter})

def removeVoter(request):
    if request.method == 'POST':
        voterName=request.POST.get('voterName','')
        collegeId=request.POST.get('collegeId','')
        email =request.POST.get('email','') 
        voter = Voter.objects.filter(collegeId = collegeId , email = email)
        user = User.objects.filter( username = email)

        if voter.exists() and user.exists():
            voter.delete()
            user.delete()
            messages.success(request, 'Voter deleted successfully!!')
        else:
            messages.success(request, 'Enter appropriate details!!')
    return render(request,'deleteVoter.html')

def deleteCandidate(request):
    pos = Position.objects.all()
    return render(request,'deleteCandidate.html',{'positions': pos})

def removeCandidate(request):
    if request.method == 'POST':
        candidateName=request.POST.get('candidateName','')
        position_id=request.POST.get('position','')
        position = Position.objects.get(id = position_id)
        email=request.POST.get('email','')
        can = Candidate.objects.filter(candidateName = candidateName  , position_id = position_id , email=email)

        if can.exists() :
            can.delete()
            messages.success(request, 'Candidate deleted successfully!!')
        else:
            messages.success(request, 'Enter appropriate details!!')
    return render(request,'deleteCandidate.html')
