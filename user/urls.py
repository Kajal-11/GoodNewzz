from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views as core_views

urlpatterns = [
    path('',                core_views.home,												        name='home'),
    path('signup/',         core_views.userregister,												name='signup'),
    path('login/', 			auth_views.LoginView.as_view(template_name='user/login.html'),			name='login'),
   	path('logout/', 		auth_views.LogoutView.as_view(template_name='user/logout.html'),		name='logout'),
    path('activate/<uidb64>/<token>/',core_views.activate,                                          name='activate'),
]