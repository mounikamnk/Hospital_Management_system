from django.shortcuts import render
from app.models import *
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def About(request):
    return render(request,'About.html')
def Home(request):
    return render(request,'Home.html')

def contact(request):
    return render(request,'contact.html')

@login_required
def index(request):
    doctor=Doctor.objects.all()
    patient=Patient.objects.all()
    appoint=Appointment.objects.all()
    d=0
    p=0
    a=0
    for i in doctor:
        d+=1
    for i in patient:
        p+=1
    for i in appoint:
        a+=1
    d1={'d':d,'p':p,'a':a}
    return render(request,'Index.html',d1)

def user_login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        AUO=authenticate(username=username,password=password)
        if AUO:
            if AUO.is_active:
                login(request,AUO)
                request.session['username']=username
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('Not a Active User')
        else:
            return HttpResponse('Invalid Details')
    return render(request,'user_login.html')



@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('user_login'))
@login_required
def view_Doctor(request):
    DOC=Doctor.objects.all()
    d={'DOC':DOC}
    return render(request,'View_Doctor.html',d)
@login_required
def delete_Doctor(request,pid):
    doctor=Doctor.objects.get(id=pid)
    doctor.delete()
    return HttpResponseRedirect(reverse('view_Doctor'))
@login_required
def add_Doctor(request):
    if request.method=='POST':
        n=request.POST['Name']
        m=request.POST['mobile']
        s=request.POST['special']
        DO=Doctor.objects.get_or_create(Name=n,mobile=m,special=s)[0]
        DO.save()
        return HttpResponseRedirect(reverse('view_Doctor'))
    return render(request,'Add_Doctor.html')

@login_required
def view_Patient(request):
    PAT=Patient.objects.all()
    d={'PAT':PAT}
    return render(request,'View_Patient.html',d)
@login_required
def delete_Patient(request,pid):
    patient=Patient.objects.get(id=pid)
    patient.delete()
    return HttpResponseRedirect(reverse('view_Patient'))
@login_required
def add_Patient(request):
    if request.method=='POST':
        n=request.POST['name']
        m=request.POST['mobile']
        g=request.POST['gender']
        a=request.POST['address']
        PO=Patient.objects.get_or_create(name=n,mobile=m,gender=g,address=a)[0]
        PO.save()
        return HttpResponseRedirect(reverse('view_Patient'))
    return render(request,'Add_Patient.html')

@login_required
def add_Appoint(request):   
    doctor1=Doctor.objects.all()
    patient1=Patient.objects.all()
    d={'doctor':doctor1,'patient':patient1}
    if request.method=='POST':
        n=request.POST['doctor']
        p=request.POST['patient']
        date=request.POST['date']    
        time=request.POST['time']
        doctor=Doctor.objects.get(Name=n)
        patient=Patient.objects.get(name=p)
        DQ=Appointment.objects.filter(Doctor=doctor,date=date,time=time)
        PQ=Appointment.objects.filter(Patient=patient,date=date,time=time)
        
        if  DQ or  PQ:
            return HttpResponse('time collapse')
        else:
            AO=Appointment.objects.get_or_create(Doctor=doctor,Patient=patient,date=date,time=time)[0]
            AO.save()
            return HttpResponseRedirect(reverse('view_Appoint'))    
    return render(request,'Add_Appoint.html',d)

@login_required
def view_Appoint(request):
    APT=Appointment.objects.all()
    d={'APT':APT}
    return render(request,'view_Appoint.html',d)

@login_required
def delete_Appoint(request,pid):
    Appoint=Appointment.objects.get(id=pid)
    Appoint.delete()
    return HttpResponseRedirect(reverse('view_Appoint'))

