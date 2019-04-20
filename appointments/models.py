from django.db import models
APPOINTMENT_TYPES = ((0,'CONSULTATION'),(2,'DIAGNOSTICS'),
                    (3, 'ENT'), (4, 'DERMATOLOGY'), (6, 'GENERAL CHECKUP'), (7, 'DENTIST'),(8,'NUTRITIONIST')
                     )
SEVERITY = ((0,'MILD'),(1,'HIGH'),(2,'EMERGENCY'))
PERIODS =(
    (0,'08:00-9:30 am'),(1,'09:30-10:30 am'),(2,'10:30-11:30 am'),(3,'11:30-12:30 pm'),(4,'12:30-1:30 pm'),(5,'1:30-2:30 pm'),
    (6,'2:30-3:30 pm'),(7,'3:30-4:30 pm'),(8,'4:30-5:00 pm')
)
from utils.counties import COUNTIES
from hospitals.models import Hospital
from django.contrib.auth import get_user_model
from django.utils.timezone import now
Users = get_user_model()
HOSPITALS=((0,'OMBO MISSION HOSPITAL'),(1,'MIGORI COUNTY TEACHING AND REFERAL HOSPITAL'),(2,'OASIS MEDICAL CLINIC'))
# Create your models here.
class Appointment(models.Model):
    hospital = models.ForeignKey(Hospital,related_name='hospital_appointments',null=True, on_delete=models.CASCADE, help_text="Only if the patient prefers this facility")
    other_hospitals = models.IntegerField(choices=HOSPITALS,help_text="IF patient prefers linking to other facilitis",null=True,blank=True)
    patient_name = models.CharField(max_length=200,help_text="Enter patient full names")
    doctors = models.ForeignKey(Users,on_delete=models.CASCADE,related_name='appointment_docs',null=True,help_text="Our Proffessional Doctors")
    patient_phone = models.CharField(null=True, max_length=200,help_text="Patient Contacts")
    email = models.EmailField(help_text="Patient Email")
    county = models.IntegerField(help_text="From which county does the patient comes from",null=True,choices=COUNTIES,verbose_name="County of Residence")
    location = models.CharField(max_length=200, null=True, blank=True ,help_text="Current Location")
    appointment_type = models.IntegerField(choices=APPOINTMENT_TYPES,help_text="Appointment Speciality")
    severity_level = models.IntegerField(choices=SEVERITY, help_text="Appointment Severity/Urgench")
    book_date = models.DateField(verbose_name="Appointement Date", help_text="Date of Appointment")
    book_time = models.IntegerField(null=True,choices=PERIODS,verbose_name="Appointment Time", help_text="Time of the appointment")
    created = models.DateTimeField(auto_now_add=True)
    is_seen = models.BooleanField(default=False, help_text="Whether the patient has been attended to or not!!")
    date_seen = models.DateTimeField(null=True,blank=True)
    def __str__(self):
        return self.patient_name

    class Meta:
        verbose_name_plural="Appointments"
        verbose_name = "Appointment"
        ordering =['-created','patient_name']


