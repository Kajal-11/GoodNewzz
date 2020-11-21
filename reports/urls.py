from django.urls import path, include
from . import views

urlpatterns = [
    path('before1/',          views.dashboard,		name='before1'),
    path('during1/',          views.dashboard,		name='during1'),
    path('after1/',          views.dashboard,		name='after1'),
    path('dashboard/',          views.dashboard,		name='dashboard'),
    path('bp/record/', 			views.addbp,			name='bp-record'),
   	path('sugar/record/', 		views.addsugar,		    name='sugar-record'),
    path('report/record/',      views.addreport,        name='report-record'),
    path('report/download/',    views.report_pdf,       name='report-download'),
]