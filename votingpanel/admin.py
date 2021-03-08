from django.contrib import admin
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
    