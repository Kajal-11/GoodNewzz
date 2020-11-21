from .forms import BPForm, SugarForm, ReportForm
from .models import BloodPressure, Sugar, Report 
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View
from MatraTatva.utils import render_to_pdf
from user.models import User
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
def before1(request):
    return render(request, 'reports/before.html')


@login_required
def during1(request):
    return render(request, 'reports/during.html')


@login_required
def after1(request):
    return render(request, 'reports/after.html')

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
            form.instance.patient = request.user
            form.instance.time = datetime.datetime.now()
            form.save()   
            messages.success(request, f'Your sugar level has been successfully recorded.')
    else:
        messages.success(request, f'Your sugar level could not be recorded.')
    
    return redirect('dashboard')
            

@login_required
def addreport(request):
    if request.method == 'POST':
        form = ReportForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.patient = request.user
            form.instance.time = datetime.datetime.now()
            form.save()   
            messages.success(request, f'Your report has been successfully stored.')
    else:
        messages.success(request, f'Your bp could not be stored.')
    
    return redirect('dashboard')
            
@login_required
def report_pdf(request):
    context = {
            'objects': Report.objects.filter(patient=request.user), 
    }
    # return render(request, 'reports/report.html', context)
    pdf = render_to_pdf('reports/report.html', context)
    if pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "Report_%s.pdf" %(datetime.datetime.now())
        content = "inline; filename='%s'" %(filename)
        download = request.GET.get("download")
        if download:
            content = "attachment; filename='%s'" %(filename)
        response['Content-Disposition'] = content
        return response
    return HttpResponse("Not found")