
from django.urls import path 
from App import views
from .views import *

urlpatterns = [
    
    path('index/' , views.index, name='index'),
    path('about/' , views.about, name='about'),
    path('base/',views.base, name='base'),
    path('home/', views.home, name='home'),
    path('gt/', views.gt, name='gt'),
   

    path('contact/', views.contact, name='contact'),
    path('contact_us/' , views.contact_us, name='contact_us'),
    
    path('signup/', views.Signup, name='signup'),
    path('login/', views.Login, name='login'),
    path('logout/',views.Logout,name='logout'),
]