from django.contrib import admin
<<<<<<< HEAD

# Register your models here.
from .models import Voter , Candidate , Position , Admin
admin.site.register(Voter)
admin.site.register(Candidate)
admin.site.register(Position)
admin.site.register(Admin)
=======
from .models import Candidate, Position
from .models import Voter
@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)


@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ('name','position')
    list_filter = ('position',)
    search_fields = ('name','position')
    readonly_fields = ('total_vote',)


@admin.register(Voter)
class VotereAdmin(admin.ModelAdmin):
    search_fields = ('name','collegeid')
    
>>>>>>> ec5b5560b9f4e382ecf7bb1c3086f149fc196e9b
