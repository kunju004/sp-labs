from django.urls import path,include
from django.conf.urls import url
from votingpanel import views

urlpatterns = [
  path('', views.index, name="HOME"),
  url(r'login/',views.ShowLoginPage),
  path('index/',views.index),
  path('voterDetails/',views.voterDetails),
  url(r'addVoter/',views.addVoter),
  url(r'addCandidate/',views.addCandidate),
  path('candidateDetails/',views.candidateDetails),
  url(r'addPosition/',views.addPosition),
  path('positionDetails/',views.positionDetails),
  url(r'admin/',views.admin),
  path('logout/',views.logout),
  path('validate/',views.validate),
  url(r'adminLogin/',views.adminLogin),
  path('check/',views.check),
  url(r'voting/',views.voting),
  url(r'displaycandidate/',views.displaycandidate),
  url(r'submit/',views.submit),
  url(r'displayPosition/',views.displayPosition)
  #path('submitvote/',views.submitvote)
  
  
]  