from django import forms
from django.core.exceptions import ValidationError

from .models import UserProfile
from django.contrib.auth.forms import PasswordChangeForm
class PatientRegistration(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['first_name','last_name','email','phone_number','age','gender','county','location']

class DoctorRegistration(forms.ModelForm):
    class Meta:
        model=UserProfile
        fields =['first_name','last_name','email','phone_number','age','gender','specialization','bio','qualifications']
class UserSetPassword(forms.ModelForm):
    password = forms.CharField(max_length=100,widget=forms.PasswordInput,required=True)
    password2 =forms.CharField(widget=forms.PasswordInput,max_length=100,required=True,label="Password Confirmation")
    class Meta:
        model =UserProfile
        fields =['password','password2']

    def clean_password2(self):
        passw1 = self.cleaned_data.get('password')
        passw2 = self.cleaned_data.get('password2')
        if passw1 != passw2:
            raise ValidationError("The two passwords must match!")
        return passw2
