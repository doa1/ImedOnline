from django.db import models
from django.contrib.auth import get_user_model
Users =get_user_model()
# Create your models here.
class Messages(models.Model):
    sender =models.ForeignKey(Users,on_delete=models.CASCADE,related_name='message_sender')
    receiver = models.ForeignKey(Users,on_delete=models.CASCADE,related_name='message_receiver')
    message = models.CharField(max_length=500,verbose_name="User Message")
    created = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.message