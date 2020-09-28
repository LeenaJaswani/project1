from django.shortcuts import render,redirect
from generalzone.models import Enquiry,CustomerInfo,LoginInfo
from userzone.models import Complain
from . models import Knowledgebase,Notification
import datetime

# Create your views here.
def adminhome(request):
    if request.session['adminid']:
        noti=Notification.objects.all()
        return render(request,'adminhome.html',{'noti':noti})
    else:
        return render(request,'login.html')
def enquiries(request):
    if request.session['adminid']:
        enq=Enquiry.objects.all()
        return render(request,'enquiries.html',{'enq':enq})
    else:
        return render(request,'login.html')

def complains(request):
    if request.session['adminid']:
        comp=Complain.objects.all()
        return render(request,'complains.html',{'comp':comp})
    else:
        return render(request,'login.html')

def customerinfo(request):
    if request.session['adminid']:
        cust=CustomerInfo.objects.all()
        return render(request,'customerinfo.html',{'cust':cust})
    else:
        return render(request,'login.html')

def knowledgebase(request):
    if request.session['adminid']:
        return render(request,'knowledgebase.html')
    else:
        return render(request,'login.html')

def logout(request):
    del request.session['adminid']
    return redirect('login')

def addnotification(request):
    if request.session['adminid']:
        notificationtext=request.POST['notificationtext']
        posteddate=datetime.datetime.now().strftime('%Y/%m/%d')
        n=Notification(notificationtext=notificationtext,posteddate=posteddate)
        n.save()
        return redirect('adminzone:adminhome')
    else:
        return render(request,'login.html')

def deletenotification(request,id):
    if request.session['adminid']:
        n=Notification.objects.get(id=id)
        n.delete()
        return redirect('adminzone:adminhome')
    else:
        return render(request,'login.html')

def deleteenquiries(request,id):
    if request.session['adminid']:
        e=Enquiry.objects.get(id=id)
        e.delete()
        return redirect('adminzone:enquiries')
    else:
        return render(request,'login.html')

def deletecomplains(request,id):
    if request.session['adminid']:
        c=Complain.objects.get(id=id)
        c.delete()
        return redirect('adminzone:complains')
    else:
        return render(request,'login.html')

def deletecustomerinfo(request,emailaddress): #emailadd. is primary key
    if request.session['adminid']:
        c=CustomerInfo.objects.get(emailaddress=emailaddress)
        l=LoginInfo.objects.get(userid=emailaddress)
        c.delete()
        l.delete()
        return redirect('adminzone:customerinfo')
    else:
        return render(request,'login.html')


def saveknowledgebase(request):
    if request.session['adminid']:
        problemid=request.POST['problemid']
        problemtext=request.POST['problemtext']
        solutiontext=request.POST['solutiontext']
        posteddate=datetime.datetime.now().strftime('%Y/%m/%d')
        kw=Knowledgebase(problemid=problemid,problemtext=problemtext,solutiontext=solutiontext,posteddate=posteddate)
        kw.save()
        return redirect('adminzone:knowledgebase')
    else:
        return render(request,'login.html')