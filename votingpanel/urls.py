from django.urls import path,include
from django.conf.urls import url
from votingpanel import views

urlpatterns = [
<<<<<<< HEAD
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
  url(r'displayPosition/',views.displayPosition),
  url(r'result/',views.result)
  
  
]  
=======
    path('',views.index, name="home"),
    path('login',views.loginUser, name="login"),
    path('logout',views.logoutUser, name="logout"),
 ]
>>>>>>> ec5b5560b9f4e382ecf7bb1c3086f149fc196e9b
