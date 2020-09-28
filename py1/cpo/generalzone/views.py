from django.shortcuts import render,redirect,reverse
from . models import Enquiry,CustomerInfo,LoginInfo
import datetime
from . import smssender
from django.core.exceptions import ObjectDoesNotExist
from adminzone.models import Notification
# Create your views here.
#views are for redirecting on the given page
def index(request):
    nf=Notification.objects.all()
    return render(request,'index.html',{'nf':nf})

def about(request):
    nf=Notification.objects.all()
    return render(request,'about.html',{'nf':nf})

def registration(request):
    nf=Notification.objects.all()
    return render(request,'registration.html',{'nf':nf})
def login(request):
    nf=Notification.objects.all()
    return render(request,'login.html',{'nf':nf})

def enquiry(request):
    nf=Notification.objects.all()
    return render(request,'enquiry.html',{'nf':nf})

#creating view for enquiry
def saveenquiry(request): #saving recieved value in variable
    name=request.POST['name']
    gender=request.POST['gender']
    address=request.POST['address']
    contactno=request.POST['contactno']
    emailaddress=request.POST['emailaddress']
    enquirytext=request.POST['enquirytext']
    enquirydate=datetime.datetime.now().strftime('%Y/%m/%d')
    en=Enquiry(name=name,gender=gender,address=address,contactno=contactno,emailaddress=emailaddress,enquirytext=enquirytext,enquirydate=enquirydate)
    en.save()
    smssender.sendsms(contactno,'Thanks for enquiry we will contact you soon-Team HR')
    return redirect('index')


def custreg(request):
    name=request.POST['name']
    gender=request.POST['gender']
    address=request.POST['address']
    nationality=request.POST['nationality']
    contactno=request.POST['contactno']
    emailaddress=request.POST['emailaddress']
    password=request.POST['password']
    connectdate=datetime.datetime.now().strftime('%Y/%m/%d')
    usertype='customer'

    if CustomerInfo.objects.filter(emailaddress=emailaddress).exists():

        msg='Customer is already registered'
        return render(request,'registration.html',{'msg':msg})

        print(msg)
        
    else:
        ci = CustomerInfo(name=name, gender=gender, address=address, nationality=nationality, contactno=contactno,emailaddress=emailaddress, password=password, connectdate=connectdate)
        li = LoginInfo(userid=emailaddress, password=password, usertype=usertype)
        ci.save()
        li.save()
        msg='Registration is done' #,{'msg':msg}) put this dict in the return param in render only
    return render(request,'registration.html',{'msg':msg})
    return redirect('registration')

def validateuser(request):
    userid=request.POST['userid']
    password=request.POST['password']
    try:
        v=LoginInfo.objects.get(userid=userid,password=password)
        if v is not None:
            usertype=v.usertype
            if usertype=='customer':
                request.session['userid']=userid #creating session
                return redirect(reverse('userzone:homeuser'))
                #reverse rediects to baseurl and this is uded for redirecting to another app
                 #print('Valid User')
            elif usertype=='admin':
                request.session['adminid']=userid
                #key is adminid and value is userid
                return redirect(reverse('adminzone:adminhome'))


    except ObjectDoesNotExist:
        #print('Invalid User')
        return redirect('login')
    #return render(request,'index.html')

