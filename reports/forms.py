from django import forms
from .models import BloodPressure, Sugar, Report, Reminder


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

class ReminderForm(forms.ModelForm):
	time = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
		help_text = "Format- DD/MM/YYYY HH:MM"
        
    )
	class Meta():
		model 	= Reminder
		fields 	= ['reminder_message', 'time']
