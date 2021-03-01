from django import forms
from regapp.models import Voter_details

class VoterForm(forms.ModelForm):
    class Meta:
        model = Voter_details
        fields = '__all__'