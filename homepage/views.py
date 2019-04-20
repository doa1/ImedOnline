from django.views.generic import TemplateView, ListView,CreateView
from appointments.forms import CreateAppointMentForm
class ContactView(TemplateView):
    template_name = 'main/contact.html'
