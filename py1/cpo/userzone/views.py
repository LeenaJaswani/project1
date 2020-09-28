from django.shortcuts import render,redirect,reverse
from generalzone.models import CustomerInfo,LoginInfo
import datetime
from .models import Complain,Question,Answer
from adminzone.models import Knowledgebase
from django.db.models import Q
# Create your views here.
def homeuser(request):
    #checking session
    if request.session['userid']:
      
        return render(request,'homeuser.html')#{'name':name}
    else:
        return render(request,'login.html')

def discussion(request):
    if request.session['userid']:
        quest=Question.objects.all()
        return render(request,'discussion.html',{'quest':quest})
    else:
        return render(request,'login.html')

def complainlog(request):
    if request.session['userid']:
        return render(request,'complainlog.html')
    else:
        return render(request,'login.html')

def searchsolution(request):
    if request.session['userid']:
        return render(request,'searchsolution.html')
    else:
        return render(request,'login.html')

def changepassword(request):
    if request.session['userid']:
        return render(request,'changepassword.html')
    else:
        return render(request,'login.html')

def logout(request):
    del request.session['userid']
    return redirect('login')

def savecomplain(request):
    if request.session['userid']:
        emailaddress=request.session.get('userid')
        customer=CustomerInfo.objects.get(emailaddress=emailaddress)
        name=customer.name
        gender=customer.gender
        address=customer.address
        contactno=customer.contactno
        subject=request.POST['subject']
        complainlog=request.POST['complainlog']
        complaindate=datetime.datetime.now().strftime('%Y/%m/%d')
        com=Complain(name=name,gender=gender,address=address,contactno=contactno,emailaddress=emailaddress,subject=subject,complainlog=complainlog,complaindate=complaindate)
        com.save()
        return redirect('userzone:homeuser')
    else:
        return render(request,'login.html')

def changepwd(request):
    if request.session['userid']:
        userid=request.session.get('userid')
        oldpassword=request.POST['oldpassword']
        newpassword=request.POST['newpassword']
        confirmpassword=request.POST['confirmpassword']
        if newpassword!=confirmpassword:
            return redirect('userzone:changepassword')
        else:
             user=LoginInfo.objects.get(userid=userid,password=oldpassword)
             if user is not None:
                 li=LoginInfo(password=newpassword,userid=userid,usertype='customer')
                 li.save()
                 return redirect('login')
             else:
                 return redirect('userzone:changepassword')
    else:
        return render(request,'login.html')


def postquestion(request):
    if request.session['userid']:
        emailaddress=request.session.get('userid')
        customer=CustomerInfo.objects.get(emailaddress=emailaddress)
        askedby=customer.name
        questiontext=request.POST['questiontext']
        posteddate=datetime.datetime.now().strftime('%Y/%m/%d')
        q=Question(questiontext=questiontext,askedby=askedby,posteddate=posteddate)
        q.save()
        return redirect('userzone:discussion')
    else:
        return render(request,'login.html')


def answer(request,qid):
    if request.session['userid']:
        return render(request,'answer.html',{'qid':qid})
    else:
        return render(request,'login.html')

def postanswer(request):
    if request.session['userid']:
        emailaddress=request.session.get('userid')
        customer=CustomerInfo.objects.get(emailaddress=emailaddress)
        answeredby=customer.name
        qid=request.POST['qid']
        answertext=request.POST['answertext']
        answereddate=datetime.datetime.now().strftime('%Y/%m/%d')
        a=Answer(answertext=answertext,answeredby=answeredby,qid=qid,answereddate=answereddate)
        a.save()
        return redirect('userzone:discussion')
    else:
        return render(request,'login.html')


def viewanswer(request,qid):
    if request.session['userid']:
        ans=Answer.objects.filter(qid=qid)
        return render(request,'viewanswer.html',{'ans':ans})
    else:
        return render(request,'login.html')

def search(request):
    if request.session['userid']:
        searchtext=request.POST['searchtext']
        kw=Knowledgebase.objects.filter(Q(problemid=searchtext) | Q(problemtext=searchtext))
        return render(request,'searchsolution.html',{'kw':kw})
    else:
        return render(request,'login.html')
