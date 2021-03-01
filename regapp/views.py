from django.shortcuts import render
from django.shortcuts import redirect
from regapp.models import Voter_details
from regapp.forms import VoterForm


# Create your views here.
def form_view(request):
    form = VoterForm()
    if request.method == "POST":
        form = VoterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request,'regapp/home.html',{'form':form})