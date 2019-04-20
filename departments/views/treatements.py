from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.shortcuts import get_object_or_404

from appointments.models import Appointment
from hospitals.models import Hospital
from django.contrib.auth import get_user_model

from django.views.generic import CreateView, FormView,UpdateView,ListView
from ..forms import TreatementForm,TreatementResultsForm
from django.utils import timezone
from departments.models import Consultation
from django.utils.timezone import now
Users = get_user_model()


# Create your views here.

class TreatementView(LoginRequiredMixin, SuccessMessageMixin,UpdateView):
    login_url = '/'
    success_message = "Treatement results successfully submitted!"
    form_class = TreatementResultsForm
    template_name = "dashboard/treatements/start_treatement.html"

    def dispatch(self, request, *args, **kwargs):
         self.appointment_id =kwargs['pk']
         self.appointment_ = get_object_or_404(Appointment,id=self.appointment_id)
         email = self.appointment_.email
         if Users.objects.filter(email=email).exists():
            self.mypatient = Users.objects.filter(email=email)[0]
            print(self.mypatient)
         else:
            self.mypatient =None
         return super(TreatementView,self).dispatch(request,*args,**kwargs)
    def get_object(self, queryset=None):
        try:
             consultation = Consultation.objects.get(appointment=self.appointment_)
        except Consultation.DoesNotExist:
            consultation =None
        return consultation
    '''def get_queryset(self):
        qs =Consultation.objects.filter(patient=self.patient)#.latest('id')
        print(qs)
        return qs'''
    def form_valid(self, form):
        '''get the consultation selected, update it with results from the doc'''
        instance = form.save(commit=False)
        hospital = Hospital.objects.get(name__iexact='imed')
        instance.hospital = hospital
        instance.doctor = self.request.user
        instance.is_cleared = True
        instance.date_cleared =now()
        patient_ = self.appointment_
        print('consult', self.get_object().sickness_period)
        if not patient_:
                messages.error(self.request,"Ooops!! Only registered patients can receive treatements. Kindly notify the patient for this")
        else:
            instance.appointement=patient_
        instance.save()
        #time to update our appointment list
        patient_.is_seen =True
        patient_.date_seen=now()
        patient_.save()
        return super(TreatementView,self).form_valid(form)

    def get_success_url(self):
        return reverse('dashboard:appointments-list')
    def get_context_data(self, **kwargs):
        context =super().get_context_data(**kwargs)
        context['patient'] =self.appointment_

        now = timezone.now()
        five_mins_ago = timezone.timedelta(minutes=5)
        context['consultation'] =self.get_object()
        context['online_status'] ='(Unregistered User)'
        if self.mypatient:
            context['mypatient'] =self.mypatient
            if self.mypatient.last_visit is not None:
                last_Active = self.mypatient.last_visit
                diff =now -last_Active
                days,seconds = diff.days, diff.seconds
                hours = days * 24 + seconds // 3600
                minutes = (seconds % 3600) // 60
                if days > 0 and days ==1:
                    context['online_status'] ="Last Active Yesterday!"
                elif days > 1:
                    context['online_status'] ='Active more than 1 day ago'
                elif hours >0:
                    context['online_status'] = 'Active {} hour(s) ago'.format(hours)
                elif hours == 0:
                    if minutes <5:
                        context['online_status'] ='Online'
                    elif minutes > 2:
                        context['online_status'] ="Active {} minutes ago".format(minutes)

            else:
                context['online_status']="Inactive"
        return context
class PatientSendFormView(LoginRequiredMixin,SuccessMessageMixin,FormView):
    login_url = '/'
    form_class = TreatementForm
    template_name = 'dashboard/treatements/treatement_form.html'

    success_message = 'You have successfully submitted your condition. Our proffessional doctor is working on it.Kinldy stay online and our doctor will engage in the next 2 minutes!!'
    #permission_denied_message = "You must be logged in to proceed"

    def dispatch(self, request, *args, **kwargs):
        self.appoint_id = kwargs['pk']
        self.appointment = Appointment.objects.get(id=self.appoint_id)
        return super(PatientSendFormView,self).dispatch(request,*args,**kwargs)
    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.doctor =self.appointment.doctors
        instance.hospital = self.appointment.hospital
        instance.patient =self.appointment
        instance.save()
        return super(PatientSendFormView,self).form_valid(form)
    def get_success_url(self):
        print(int(self.appoint_id))
        return reverse('dashboard:send-form',kwargs={'pk':int(self.appoint_id)})
    def get_context_data(self, **kwargs):
        context = super(PatientSendFormView,self).get_context_data(**kwargs)
        context['appointment'] =self.appointment

        doctor = self.appointment.doctors
        context['doctor'] =doctor
        now = timezone.now()
        if doctor.last_visit is not None:
            last_Active = doctor.last_visit
            diff = now - last_Active
            days, seconds = diff.days, diff.seconds
            hours = days * 24 + seconds // 3600
            minutes = (seconds % 3600) // 60
            if days > 0 and days == 1:
                context['online_status'] = "Last Active Yesterday!"
            elif days > 1:
                context['online_status'] = 'Active more than 1 day ago'
            elif hours > 0:
                context['online_status'] = 'Active {} hour(s) ago'.format(hours)
            elif hours == 0:
                if minutes < 5:
                    context['online_status'] = 'Online'
                elif minutes > 2:
                    context['online_status'] = "Active {} minutes ago".format(minutes)

        return context

class ViewDoneTreatements(LoginRequiredMixin,ListView):
    template_name = 'dashboard/treatements/treatements_list.html'
    login_url = reverse_lazy('homepage:index')
    def get_queryset(self):
        user = self.request.user
        qs =None
        if user.is_doctor:
            '''if the user is doctor , query with the doctor'''
            qs = Consultation.objects.filter(doctor=user,is_cleared=True)

        else:
            '''we,have a problem, patients were indirectly linked to the treatements via appointments,so we have to check'''
            #was this a new patient
            new_patient = Consultation.objects.filter(new_patient=user,is_cleared=True)
            if new_patient.exists():
                qs =new_patient
            else:
                #via appointment direct
                appointment =Appointment.objects.filter(email=user.email)
                if appointment.exists():
                    qs =Consultation.objects.filter(appointment=appointment[0])

        return qs

    def get_context_data(self, *args, object_list=None, **kwargs):
        context =super().get_context_data(object_list=None,**kwargs)
        context['treatements'] =self.get_queryset()
        return context
    