from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="home"),
    path("castvote/",views.castvote,name="CastVote"),
    path("results/",views.results,name="ShowResults"),
    path("voters/",views.voters,name="VoterDetails"),
    path("candidates/",views.candidates,name="CandidateDetails")
 ]
