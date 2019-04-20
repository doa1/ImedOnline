from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError
from utils.doctors import DOCTORS
COUNTIES =(
              (1,'Mombasa'),(2,'Kwale'),(3,'Kilifi'),(4,'Tana River'),(5,'Lamu'),(6,'Taita Taveta'),(7,'Moyale'),
              (8,'Wajir'),(9,'Garissa'),(10,'Marsabit'),(11,'Isiolo'),(12,'Meru'),(13,'Tharaka Nithi'),(14,'Embu.'),(15,'Kitui'),(16,'Machakos'),
              (18,'Makueni'),(19,'Nyandarua'),
              (20,'Nyeri'),(21,'Kirinyaga'),(22,'Murang\'a'),(23,'Kiambu'),(24,'Turkana'),(25,'.West Pokot'),(26,'Samburu'),(27,'Trans Nzoia'),(28,'Uasin Gishu'),(29,'Elgeyo / Marakwet'),
              (30,'Nandi'),(31,'Baringo'),(32,'Laikipia'),(33,'Nakuru'),(34,'Narok'),(35,'Kajiado'),(36,'Kericho'),(37,'Bomet'),(38,'Kakamega'),(39,'Vihiga'),
              (40,'Bungoma'),(41,'Busia'),(42,'Siaya'),(43,'Kisumu'),(44,'Homa Bay'),(45,'Migori'),(46,'Kisii'),
              (47,'Nyamira'),(48,'Nairobi City')
)
GENDER =(
    (0,'MALE'),(1,'FEMALE')
)
# Create your models here.
class AccountsManager(BaseUserManager):
    def get_by_natural_key(self, email):
        try:
           return self.get(email=email)
        except self.model.DoesNotExist:
            return self.get(is_active=True,email=email)
    def create_user(self,email,password=None,**kwargs):
        '''override the default create user method to use in the create superuser'''
        if not email:
            raise ValidationError("Users are required to have email addresses")
        user = self.model(email=email,**kwargs)

        user.set_password(self.make_random_password(password))
        user.save(using=self._db) # just save the user without setting them active
        return user
    def create_superuser(self,email,password,username=None,**kwargs):
        user =self.create(email=email,username=username,gender=0,
                          **kwargs,)

        user.is_active=True
        user.is_staff=True
        user.is_superuser=True
        user.set_password(raw_password=password)
        user.save(using=self._db)
        return user


class UserProfile(AbstractUser):
    username = models.CharField(null=True,blank=True,max_length=150,unique=False)
    first_name = models.CharField(max_length=200,null=True)
    last_name = models.CharField(max_length=200,null=True)
    is_doctor=models.BooleanField(default=False)
    date_of_birth = models.DateTimeField(null=True,blank=True)
    phone_number = models.CharField(max_length=120,null=True,blank=True)
    county = models.IntegerField(choices=COUNTIES,null=True)
    location =models.CharField(max_length=120,verbose_name="Place of residence",null=True)
    last_visit= models.DateTimeField(null=True,blank=True)
    age = models.PositiveIntegerField(null=True,blank=True)
    gender = models.IntegerField(choices=GENDER)
    image = models.ImageField(upload_to='images/',null=True,blank=True) #seriously wants pillow,
    bio = models.TextField(null=True,blank=True,verbose_name='User Biography')
    qualifications = models.TextField(null=True,blank=True)
    email = models.EmailField(unique=True,max_length=200)
    share_email = models.BooleanField(default=False, verbose_name='Share Your Email?')
    share_address = models.BooleanField(default=False, verbose_name='Share Your Address')
    share_phone = models.BooleanField(default=False, verbose_name='Share Your Address')
    random_password = models.CharField(max_length=200,null=True,blank=True,verbose_name="User Autogen Keys")
    identity = models.CharField(max_length=50,null=True,blank=True)
    objects = AccountsManager()
    specialization = models.IntegerField(choices=DOCTORS,help_text="Your area of specialization",null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'auth_user'
        verbose_name = _("User")
        verbose_name_plural = _("Users")
        swappable = 'AUTH_USER_MODEL'
        ordering = ['email', 'first_name', 'last_name']