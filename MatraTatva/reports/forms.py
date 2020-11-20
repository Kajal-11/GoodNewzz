from django import forms
from .models import BloodPressure, Sugar, Report


class BPForm(forms.ModelForm):
	class Meta():
		model 	= BloodPressure
		fields 	= ['systole', 'diastole']

class SugarForm(forms.ModelForm):
	class Meta():
		model 	= Sugar
		fields 	= ['value']

class ReportForm(forms.ModelForm):
	class Meta():
		model 	= Report
		fields 	= ['title', 'report_image']
