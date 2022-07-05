from django.db import models


# Create your models here.

class DeviceModels(models.Model):
    Values = models.IntegerField()
    Time   = models.DateField('date_now')   