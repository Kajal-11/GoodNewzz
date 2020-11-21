from django.contrib import admin
from .models import BloodPressure, Sugar, Report

admin.site.register(BloodPressure)
admin.site.register(Sugar)
admin.site.register(Report)