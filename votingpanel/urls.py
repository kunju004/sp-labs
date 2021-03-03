from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path("voters/",views.voters,name="VoterDetails"),
    path("candidates/",views.candidates,name="CandidateDetails")
 ]
