from django.db import models
from user.models import User

class BloodPressure(models.Model):
    patient     = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    systole     = models.PositiveIntegerField(default=0)
    diastole    = models.PositiveIntegerField(default=0)
    time        = models.DateTimeField(auto_now=True)

class Sugar(models.Model):
    patient     = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    value       = models.PositiveIntegerField(default=0)
    time        = models.DateTimeField(auto_now=True)

class Report(models.Model):
    patient     = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    time        = models.DateTimeField(auto_now=True)
    title       = models.CharField(default='', max_length=500)
    image       = models.ImageField(upload_to='reports', blank=True)
    