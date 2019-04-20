from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from appointments.models import Appointment
from hospitals.models import Hospital,Emergency
class Home(LoginRequiredMixin,TemplateView):
    login_url = '/'
    template_name = 'dashboard/index.html'

    def get_context_data(self, **kwargs):
        context  = super(Home,self).get_context_data(**kwargs)
        user = self.request.user

        context['appointments']=Appointment.objects.filter(doctors=user).count()
        hospital = Hospital.objects.get(name__iexact='imed')
        myAppointments = Appointment.objects.filter(hospital=hospital).filter(email=user.email).count()
        context['myappoints'] = myAppointments
        context['emergencies'] =Emergency.objects.count()
        return context
class ViewEmergencies(LoginRequiredMixin,ListView):
    login_url = '/'
    template_name = 'dashboard/emergency/list.html'

    def get_queryset(self):
        return Emergency.objects.all()


