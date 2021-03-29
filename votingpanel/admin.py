from django.contrib import admin

# Register your models here.
from .models import Voter , Candidate , Position , Admin
admin.site.register(Voter)
admin.site.register(Candidate)
admin.site.register(Position)
admin.site.register(Admin)