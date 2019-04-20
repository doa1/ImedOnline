from django.urls import path
from departments.views import generals,treatements,appointements
from departments.rest import apis
from .view import *
app_name = 'dashboard'
urlpatterns =[
    path('',Home.as_view(),name='home'),
    path('appointments/',appointements.ViewAppointments.as_view(),name="appointments-list"),
    path('emergencies/',generals.ViewEmergencies.as_view(),name="emergencies_list"),
    path('appointments/see/',appointements.SeenAppointments.as_view(),name="seen-appointement"),
    path('treatement/<int:pk>/',treatements.TreatementView.as_view(),name="init-treatement"),
    path('send/treatement/<int:pk>/',treatements.PatientSendFormView.as_view(),name='send-form'),
    path('treatemesnt/cleared/',treatements.ViewDoneTreatements.as_view(),name='cleared_treatements'),
    path('treatement/detail/api/<int:pk>/',apis.TreatementDetailApi.as_view(),name="treatement-detail-api")

]