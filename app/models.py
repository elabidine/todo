from django.contrib.auth.models import AbstractUser
from django.db import models
from phone_field import PhoneNumber,PhoneField
from oauth2_provider.models import AbstractApplication

class CustomApplication(AbstractApplication):
    # Other fields of your custom application model
    post_logout_redirect_uris = models.TextField(default="", blank=True)

class CustomUser(AbstractUser,models.Model):
   
    email = models.EmailField(unique=True)
    birthday=models.DateField(null=True, blank=True)
    phone = PhoneField(unique=True,blank=True, help_text='Contact phone number')

    def __str__(self) :
        return self.username
    
    
class Product(models.Model):
    prodname = models.CharField(max_length=255)
