from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Appointment
from .forms import CreateAppointMentForm
from django.views.generic import DeleteView,DetailView,CreateView,ListView
from django.contrib.auth import get_user_model
from hospitals.models import Hospital
from django.contrib.messages.views import SuccessMessageMixin
Users = get_user_model()
# Create your views here.
class MakeAppointment(SuccessMessageMixin,CreateView):
    '''Allow patients to make appointment'''
    template_name = "main/appointment.html"
    form_class = CreateAppointMentForm
    success_message = "You appointment was placed successfully. We'll as contact as soon as we can. Thank Your."
    def get_form_kwargs(self):
        '''in a bid to customize how to render certain fields, we must pass some arguments affecting the form fields'''
        kwargs =super(MakeAppointment,self).get_form_kwargs()
        doctors= Users.objects.filter(is_doctor=True)
        '''by default, the form renders the doctor field  with only email columns so,
         i wanted to display the names and area of specs'''
        kwargs['doctors']=[(user.id,user.get_full_name()+'-'+user.get_specialization_display() if user.specialization is not None else user.get_full_name() ) for user in doctors]
        return kwargs
    def form_valid(self, form):
        instance = form.save(commit=False)
        option =self.request.POST.get('book_opt')
        hosp = Hospital.objects.get(name__iexact="Imed")
        if option == "yes":
            instance.hospital =hosp
        elif option =="no":
            instance.doctors = None
        instance.save()
        print(instance)
        return  super(MakeAppointment,self).form_valid(form)

    def get_success_url(self):
        return reverse('homepage:create-appointment')


