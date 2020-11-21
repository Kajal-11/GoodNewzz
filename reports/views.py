from .forms import BPForm, SugarForm, ReportForm
from .models import BloodPressure, Sugar, Report 
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import View
from MatraTatva.utils import render_to_pdf
from user.models import User
import datetime


def sugar_chart(request):
    labels = []
    data = []
    queryset = Sugar.objects.filter(patient=request.user).values('time').annotate(sugar_level=Sum('value')).order_by('time')
    for entry in queryset:
        labels.append(entry['time'])
        data.append(entry['sugar_level'])
    
    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })

def bp_chart(request):
    labels = []
    data = []
    queryset = BloodPressure.objects.filter(patient=request.user).values('time').annotate(blood_pressure=Sum('systole')).order_by('time')
    for entry in queryset:
        labels.append(entry['time'])
        data.append(entry['blood_pressure'])
    
    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })
    
def dashboard(request):
    return render(request, 'reports/dashboard.html')

@login_required
def before1(request):
    return render(request, 'reports/before_lp.html')


@login_required
def during1(request):
    return render(request, 'reports/during_lp.html')


@login_required
def after1(request):
    return render(request, 'reports/after_lp.html')

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
    
    context = {
        'bpform': BPForm(),
    }
    
    return render(request, 'reports/dashboard1.html', context)

            


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
    
    context = {
        'sugarform': SugarForm(),
    }
    
    return render(request, 'reports/dashboard2.html', context)            

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
        
    context = {
        'reportform': ReportForm(),
    }
    
    return render(request, 'reports/dashboard3.html', context)
            
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