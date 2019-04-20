from django.core.exceptions import ValidationError

from .models import Consultation
from django import forms
from .utility import get_selected_diseases,DISEASES
class TreatementForm(forms.ModelForm):
   class Meta:
        model =Consultation
        fields =['sickness_category','sickness_period','symptoms','other_info','previous_medication','image','audio_clip','video_clip']
class TreatementResultsForm(forms.ModelForm):

    disease = forms.MultipleChoiceField(widget=forms.SelectMultiple,choices=DISEASES)
    class Meta:
        model =Consultation
        fields =['disease','results','drugs','prescription','diatery_advice','medical_advice']

    def clean_disease(self):
        choices = self.cleaned_data['disease']
        choices = filter(None,choices)
        if not choices:
            raise ValidationError(self.error_message['Disease field is required.'])
        diseases =get_selected_diseases(tuple_list=DISEASES,selected_keys=choices)

        return diseases

