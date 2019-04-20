from django.urls import path, include
from .views import *
from hospitals.views import ReportEmergency
app_name = 'homepage'

urlpatterns =[
    path('',TemplateView.as_view(template_name="main/index.html"),name='index'),
    path('about/',TemplateView.as_view(template_name='main/about.html'),name='about'),
    path('contact/',ContactView.as_view(),name="contact"),
    path('appointment/',include('appointments.urls')),
    path('emergencies/',ReportEmergency.as_view(),name="emergency"),
]