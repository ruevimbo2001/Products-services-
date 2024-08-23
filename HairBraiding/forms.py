from django import forms
from .models import *

class HairbraidingServiceForm(forms.ModelForm):
    class Meta:
        model = HairbraidingService
        fields = '_all_'