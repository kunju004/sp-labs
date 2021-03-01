from django.contrib import admin
from regapp.models import Voter_details
# Register your models here.
class voterAdmin(admin.ModelAdmin):
    list_display = ['fullname','email', 'collegeid', 'registration_number','current_year','department']

admin.site.register(Voter_details,voterAdmin)