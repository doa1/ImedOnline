from django.db import models
from django.contrib.auth import get_user_model
EMERGENCIES = (
    (0,'ACCIDENT'),(1,'POISONING'),(2,'CHILD BIRTH'),(3,'OTHER')
)
UserModel = get_user_model()
# Create your models here.
class Hospital(models.Model):
    '''Creates facility/clinic model, allow creation of the hospital w/ members or head'''
    name = models.CharField(unique=True,max_length=100)
    head = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='hospital_head', null=True)
    members = models.ForeignKey(UserModel,on_delete=models.CASCADE, related_name='hospital_members', null=True)
    created = models.DateTimeField(auto_created=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Clinic"
        verbose_name_plural = "Clinics"

class Emergency(models.Model):
    emergency = models.IntegerField(choices=EMERGENCIES,verbose_name="Emergency Type",help_text="Kindly indicate the emergency")
    full_names = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=250,null=True)
    location = models.CharField(max_length=200)
    nearest_clinic= models.CharField(max_length=200,null=True,blank=True,verbose_name="Nearest Health Center")
    description = models.TextField(null=True,verbose_name="Brief Description",help_text="Kindly give a brief description of this emergency")
    timestamp = models.DateTimeField(auto_now_add=True)
    is_seen = models.BooleanField(default=False,help_text="Whether the emergency has been cleared or not")

    def __str__(self):
        return '{} -{}'.format(self.full_names,self.get_emergency_display())

    class Meta:
        verbose_name ="Emergency"
        verbose_name_plural ="Emergencies"
        ordering =['-timestamp']