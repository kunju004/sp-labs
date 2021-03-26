"""votingSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
<<<<<<< HEAD:votingSystem/urls.py
from django.urls import path,include
from django.conf.urls import url
from votingSystem import settings
from votingpanel.views import index
from votingpanel import views 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('votingpanel/',include('votingpanel.urls')),
    path('',views.index),
    
]
=======
from django.urls import path
from votingpanel import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
     path('', views.homeView, name='home'),
    path('login/', views.loginView, name='login'),
    path('dashboard/', views.dashboardView, name='dashboard'),
    path('logout/', views.logoutView, name='logout'),
    path('position/', views.positionView, name='position'),
    path('candidate/<int:pos>/', views.candidateView, name='candidate'),
    path('candidate/detail/<int:id>/', views.candidateDetailView, name='detail'),
    path('result/', views.resultView, name='result'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



admin.site.site_header = "Online Voting System"
admin.site.index_title = "Welcome to online voting system admin panel"
admin.site.site_title = "OVS"
>>>>>>> ec5b5560b9f4e382ecf7bb1c3086f149fc196e9b:online_voting_system/urls.py
