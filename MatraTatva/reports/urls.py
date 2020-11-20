from django.urls import path, include
from . import views

urlpatterns = [
    
    path('dashboard/',          views.dashboard,		name='dashboard'),
    path('bp/record/', 			views.addbp,			name='bp-record'),
   	path('sugar/record/', 		views.addsugar,		    name='sugar-record'),
    path('report/record/',      views.addreport,        name='report-record'),
]