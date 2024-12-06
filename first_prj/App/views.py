from django.shortcuts import render,redirect,HttpResponse
#from .serializers import *
from django.conf import settings
from .models import *
from .Serializer import *
from .form import *
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.contrib import messages


from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render( request , 'index.html')

def about(request):
    return render(request, 'about.html')

def base(request):
    return render( request , 'base.html')
def home(request):
    return render(request, 'home.html')

def gt(request):
    return render(request, 'gt.html')

#----------------------------------------CONTACT-----------------------

def contact(request):
    cnct_frm= ContactForm()
    context ={
            'form' : cnct_frm
        }
    return render(request, 'contact.html', context)
def contact_us(request):
    if request.method == 'POST':
         Name      =request.POST['Name']
         Email     =request.POST['Email']
         Id        =request.POST['Id']
         
         obj = Contact_Us(Name=Name, Email=Email, Id=Id )
         obj.save()
    return HttpResponse("The CONTACT has be Submitted Succesfully")

'''
def contact(request):
    if request.method =='POST':
        form = ContactForm(request.POST)
        if form.is_valid ():
            return 'success'
        
        form= ContactForm()
        return render(request, 'contact.html', {'form':form})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'contact.html')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})'''
    
    
    
    
'''
def contact(request):
    if request.method == 'POST':
        object=ContactModel(request.POST)
        Name     =request.POST.get('Name')
        Email    =request.POST.get('Email')
        
        
        object.Name=Name
        object.Email= Email
        
        if object.save():
            messages.success(request, ("The CONTACT has be Submitted Succesfully"))
            return redirect( 'base')        
    else:
        object = ContactModel()
        return render (request, 'app/contact.html')
        

def contact(request):
    if request.method == 'POST':
        Name     =request.POST['Name']
        Email    =request.POST['Email']
        

        obj = ContactModel(Name=Name, Email=Email, Address=Address, City=City, State=State,Pincode=Pincode)
        obj.save()
    return render (request, 'contact.html',{})'''





#----------------------------------------------------LOG_IN-----------------------
@login_required(login_url='login')
def Signup(request):
    if request.method=='POST':
        name=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1 != pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(name,email,pass1)
            my_user.save()
            return redirect('login')
    return render (request,'signup.html')
def Login(request):
    if request.method=='POST':
        username =request.POST.get('username')
        pass1    =request.POST.get('pass')
        user     =authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('base')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")
    return render (request,'login.html')
def Logout(request):
    logout(request)
    return redirect('login')

