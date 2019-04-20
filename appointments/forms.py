from django.utils.timezone import now

from .models import Appointment
from django import forms
import datetime
import re
import datetime
from django.contrib.auth import get_user_model
Users = get_user_model()
def tommorow():
    tomm = datetime.date.today() + datetime.timedelta(days=1)
    return tomm
class CreateAppointMentForm(forms.ModelForm):
    def __init__(self,**kwargs):
        '''here is where we can customize form fields,actions and other methods,the order matters when passing args from the request data '''
        doct_list = kwargs.pop('doctors')
        #print(doct_list)
        super(CreateAppointMentForm, self).__init__(**kwargs)
        self.fields['doctors'].choices =doct_list
        #kwargs['doctors'].choices =d
    book_date=forms.DateField(widget=forms.SelectDateWidget,label='Appointment Date',initial=tommorow())
    #doctors = forms.ModelChoiceField(queryset=Users.objects.filter(is_doctor=True))
    class Meta:
        model = Appointment
        fields =['patient_name','patient_phone','email','appointment_type','severity_level','other_hospitals','doctors','book_date','book_time','county']