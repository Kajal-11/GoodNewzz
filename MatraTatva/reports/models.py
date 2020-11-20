from django.db import models
from user.models import User

class BloodPressure(models.Model):
    patient     = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    systole     = models.PositiveIntegerField(default=0)
    diastole    = models.PositiveIntegerField(default=0)
    time        = models.DateTimeField()

class Sugar(models.Model):
    patient     = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    value       = models.PositiveIntegerField(default=0)
    time        = models.DateTimeField()

class Report(models.Model):
    patient     = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    time        = models.DateTimeField()
    title       = models.CharField(default='', max_length=500)
    report_image = models.ImageField(upload_to='reports', blank=True)
    