from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request,'votingpanel/home.html')
def voters(request):
    return render(request,'votingpanel/voters.html')
def candidates(request):
    return render(request,'votingpanel/candidates.html')