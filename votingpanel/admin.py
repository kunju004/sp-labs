from django.contrib import admin

# Register your models here.
from .models import Voter
from .models import Candidate

admin.site.register(Voter)
admin.site.register(Candidate)
