from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def index(request):
    return render(request,'votingpanel/index.html')
    
def castvote(request):
    return HttpResponse("Vote here")
def results(request):
    return HttpResponse("show results")
def voters(request):
    return HttpResponse("see voters")
def candidates(request):
    return HttpResponse("see candidates")