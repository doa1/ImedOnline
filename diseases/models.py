from django.db import models
from utils.diseases import DISEASES
# Create your models here.
SEGEMENTS = (
        (0,'PEDIATRIC'),(1,'GYNECOLOGY'),(2,'SEXUAL HEALTH'),(3,'COUGH & ALLERGY'),
         (4,'SKIN & RASHES'),(5,'CHRONIC'),(6,'OTHER')
        )
class Diseases(models.Model) :
    '''diseases list model with disease name and its category with the effects on the body'''
    category = models.IntegerField(choices=SEGEMENTS)
    name = models.CharField(max_length=250,choices=DISEASES)
    effects = models.TextField(help_text="States the effects of every disease on the human body",null=True,blank=True)
    def __str__(self):
        return self.get_name_display()

