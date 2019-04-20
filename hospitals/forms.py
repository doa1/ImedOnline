from .models import Hospital,Emergency
from django import forms
class ReportEmergencyForm(forms.ModelForm):
    class Meta:
        model =Emergency
        exclude=['timestamp']