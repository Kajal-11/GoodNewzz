from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import BPForm, SugarForm, ReportForm
from user.models import User
from .models import BloodPressure, Sugar, Report 
import datetime

@login_required
def dashboard(request):
    context = {
        'bpform': BPForm(),
        'sugarform': SugarForm(),
        'reportform': ReportForm(),
    }
    
    return render(request, 'reports/dashboard.html', context)

@login_required
def addbp(request):
    if request.method == 'POST':
        form = BPForm(request.POST)
        if form.is_valid():
            form.instance.patient = request.user
            form.instance.time = datetime.datetime.now()
            form.save()   
            messages.success(request, f'Your bp has been successfully recorded.')
    else:
        messages.success(request, f'Your bp could not be recorded.')
    
    return redirect('dashboard')
            


@login_required
def addsugar(request):
    if request.method == 'POST':
        form = SugarForm(request.POST)
        if form.is_valid():
            sugar = form.save()
            sugar.instance.patient = request.user
            sugar.instance.time = datetime.datetime.now()
            sugar.save()   
            messages.success(request, f'Your sugar level has been successfully recorded.')
    else:
        messages.success(request, f'Your sugar level could not be recorded.')
    
    return redirect('dashboard')
            

@login_required
def addreport(request):
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            report = form.save()
            report.instance.patient = request.user
            report.instance.time = datetime.datetime.now()
            report.save()   
            messages.success(request, f'Your report has been successfully stored.')
    else:
        messages.success(request, f'Your bp could not be stored.')
    
    return redirect('dashboard')
            
