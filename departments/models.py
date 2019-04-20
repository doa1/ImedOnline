from django.db import models
from hospitals.models import Hospital
from django.contrib.auth import get_user_model
from diseases.models import Diseases,DISEASES,SEGEMENTS
from appointments.models import Appointment
Users = get_user_model()
EMERGENCIES = ((0,'ACCIDENT'),(1,'POISONING'),(2,'CHILD BIRTH'),(3,'OTHER'))
SICKNESS_PERIOD = (
    (0,'12-24 HOURS'),(1,'24-48 HOURS'),(2,'2-4 DAYS'),(3,'1-2 WEEKS'),(4 ,'2-3 WEEKS'),
    (5,'LESS THAN A MONTH'),(6,'1-2 MONTHS'),(7,'2-3 MONTHS'),(8,'3-4 MONTHS'),(9,'4-5 MONTHS'),
    (10,'5-7 MONTHS'),(11,'8-10 MONTHS'),(12,'LESS THAN A YEAR'),(13,'LESS THAN 2 YEARS'),(14,'MORE THAN 2 YEARS')
)
QA_TEMPLATES=()
# Create your models here.

class Consultation(models.Model):
    '''Consultation service for doing treatment and offer post-advice '''
    doctor = models.ForeignKey(Users,on_delete=models.CASCADE, related_name='doctors')
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, related_name='patients')
    new_patient = models.ForeignKey(Users,null=True,blank=True,on_delete=models.CASCADE,help_text="If patient never booked an appointment and has to be treated directly, consider new patient but has to register")
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name='consultations')
    disease = models.CharField(verbose_name="Confirmed Sickness",null=True,max_length=500)
    sickness_category =models.IntegerField(choices=SEGEMENTS,verbose_name="Select Sickness Category",null=True)
    sickness_period = models.IntegerField(choices=SICKNESS_PERIOD,verbose_name="For how long have you been sick?")
    symptoms = models.TextField(verbose_name="What symptoms are you experiencing?")
    other_info = models.TextField(verbose_name="Any Other revelant information?",null=True,blank=True)
    previous_medication = models.CharField(max_length=250, null=True,verbose_name="Have you taken any medication? If yes, kindly name the medication" )
    results = models.TextField(null=True, help_text="Result of the diagnosis given as a feedback to the patient")
    prescription = models.TextField(null=True)
    diatery_advice = models.TextField(null=True)
    medical_advice = models.TextField(null=True)
    audio_clip = models.FileField(verbose_name="Assisting Audio Clip",null=True,blank=True,upload_to='treatements/audio/')
    video_clip =models.FileField(verbose_name="Assisting Video Clip",null=True,blank=True,upload_to='treatements/video/')
    image = models.ImageField(verbose_name="Assisting Picture",null=True,blank=True,upload_to='treatements/images/')
    created = models.DateTimeField(auto_now_add=True)
    is_cleared= models.BooleanField(default=False,help_text="Designates whether treatement has been administered or not")
    drugs = models.TextField(verbose_name="Recommend Drugs",null=True,help_text="Drugs recommended for the patient")
    date_cleared =models.DateTimeField(null=True,blank=True)
    def __str__(self):
        return self.appointment.patient_name
    class Meta:
        verbose_name ="Consultation Desk"
        verbose_name_plural = "Consultations Desk"