from re import template
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import activate,signup

urlpatterns = [
    path('login/',auth_views.LoginView.as_view(template_name='accounts/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='accounts/logout.html'),name='logout'),
    path('signup/',signup,name='signup'),
    path('activate/<uidb64>/<token>/',activate, name='activate'), 
    
]
