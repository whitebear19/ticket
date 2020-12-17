from django.db import models
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile

class Tickets(models.Model):
    id=models.AutoField(primary_key=True)
    date_of_incident = models.CharField(default='',max_length=255, null=True)    
    contact_name = models.CharField(default='',max_length=255, null=True)
    contact_number = models.CharField(default='',max_length=255, null=True)
    insurer = models.CharField(default='',max_length=255, null=True,)
    ticket_type = models.CharField(default='',max_length=255, null=True)
    ticket_status= models.CharField(default='',max_length=255, null=True)
    vehicle_reg_num= models.CharField(default='',max_length=255, null=True)
    vehicle_manufacturer= models.CharField(default='',max_length=255, null=True)    
    vehicle_model = models.CharField(default='',max_length=255, null=True)  
    assigned_to = models.CharField(default='',max_length=255, null=True)  
    tow_from = models.CharField(default='',max_length=255, null=True)  
    tow_to_workshop = models.CharField(default='',max_length=255, null=True)  
    tow_to_address = models.CharField(default='',max_length=255, null=True) 
    created_at = models.DateTimeField(auto_now_add=True,blank=True) 
    class Meta:
        db_table = 'tickets'


class VehicleManufacturer(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(default='',max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True,blank=True) 
    class Meta:
        db_table = 'vehiclemanufacturer'

class TowToWorkshop(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(default='',max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True,blank=True) 
    class Meta:
        db_table = 'towtoworkshop'
