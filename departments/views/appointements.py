from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from appointments.models import Appointment
from hospitals.models import Hospital,Emergency
class ViewAppointments(LoginRequiredMixin,ListView):
    login_url = '/'
    template_name = "dashboard/appointments/list.html"
    def get_queryset(self):
        user = self.request.user
        appointments =Appointment.objects.filter(doctors=user,is_seen=False) if user.is_doctor else Appointment.objects.filter(email=user.email,is_seen=False)
        return appointments

class SeenAppointments(LoginRequiredMixin,ListView):
    login_url = '/'
    template_name = 'dashboard/appointments/seen.html'

    def get_queryset(self):
        user = self.request.user
        appointments = Appointment.objects.filter(doctors=user,is_seen=True) if user.is_doctor else Appointment.objects.filter(email=user.email,is_seen=True)
        return appointments
