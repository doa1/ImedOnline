from django.shortcuts import render
from .forms import ReportEmergencyForm
from .models import Emergency
from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import reverse
# Create your views here.

class ReportEmergency(SuccessMessageMixin,CreateView):
    template_name = 'main/emergency.html'
    form_class = ReportEmergencyForm
    success_message = "Your Case was successfully reported. You'll be notified as soon as possible."

    def get_success_url(self):
        return reverse('homepage:emergency')