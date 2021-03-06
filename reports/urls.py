from django.urls import path, include
from . import views

urlpatterns = [
    path('reminders/',  views.reminder,      name='reminder'),
    path('before1/',          views.before1,		name='before1'),
    path('during1/',          views.during1,		name='during1'),
    path('after1/',          views.after1,		name='after1'),
    path('dashboard/',          views.dashboard,		name='dashboard'),
    path('bp/record/', 			views.addbp,			name='bp-record'),
   	path('sugar/record/', 		views.addsugar,		    name='sugar-record'),
    path('report/record/',      views.addreport,        name='report-record'),
    path('report/download/',    views.report_pdf,       name='report-download'),
    path('sugar_level/chart/',  views.sugar_chart,      name='sugar-chart'),
    path('blood_pressure/chart/',  views.bp_chart,      name='bp-chart'),
]