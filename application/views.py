from django.shortcuts import render,render_to_response
from django.http.response import HttpResponseRedirect
from .forms import *
import json
from django.contrib.auth.models import User
from django.conf import settings
from bs4 import BeautifulSoup as BS
import requests
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.core.context_processors import csrf
from django.contrib import auth
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/accounts/login')
def index(request):

    return render_to_response('ignou.html',{'user':request.user})

def question(request):
    #q=QOA.objects.all()
    y = Years.objects.all()
    s= QOA.objects.all()
    return render_to_response('Question_paper.html',{'question':y})


def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    else:
        form=LoginForm()
        c={'form':form}
        c.update(csrf(request))
        return render(request,'registration/login.html',c)

def em(request):
    e=request.POST.get('email')
    f=User.objects.filter(email=e)
    if f:
        return HttpResponse("exist")
    else:
        return HttpResponse("Not")


def logout(request):
    auth.logout(request)
    return render_to_response('registration/logged_out.html')


def ajax_answer(request,pk):
    form = answerforms(request.POST)
    if form.is_valid():
        print("idddd",pk)
        task = form.save(commit=False)
        #qs = p.replace('-',' ')
        #qes= Question.objects.get(qs=qs).id
        task.user_id = request.user.id
        task.qes_id = pk
        task.save()
        return HttpResponse('OK')
    else:
        return HttpResponse('NOT')
        #Answer.objects.create(qs=1,user=request.user.id,)


def anss(request,pk):
    form = answerforms()
    qs = pk.replace('-',' ')
    qes=Question.objects.get(qs=qs)
    ans = qes.answer_set.all()
    comment = Comment.objects.all()
    #print(pk)
    return render(request,'answer.html',{'answer':ans,'question':qes,'comments':comment,'form':form})

def answer(request):
    #if request.method == 'POST':
        #an = request.POST.get('answers')
    return render_to_response('give_answer.html')

def post_comment(request,pk):
    print(pk)
    if request.method=='POST':
        form = comment_form(request.POST)
        if form.is_valid():
            task=form.save(commit=False)
            ans = Answer.objects.get(id=pk)
            task.forwhat_id = ans.id
            task.user_id = request.user.id
            task.save()
            form.save()
            return HttpResponse('OK')
        else:
            return HttpResponse('NOT')
        #Comment.objects.create()

def community(request):
    com = Question.objects.all()
    return render_to_response('community.html',{'com':com})

def registration(request):
    form=Registrationform(request.POST or None)
    #pform = Registrationformprofile(request.POST)
    #pform=Registrationformprofile(data=request.POST,instance=request.user.profile)
    #print("before")
    if request.method=='POST':
        if form.is_valid():
     #       print("valiiddd")
            form.save()
            return HttpResponse('OK')
        else:
            print("this is else part")
            ems=str(request.POST.get('username'))
            u=request.POST.get('email')
            #print(type(ems))
            l=str(u)
            u=str(ems)
            #print(User.objects.filter(email=l))
            print(u)
            print(User.objects.filter(email=l))

            #print(User.objects.filter(username=u))
            #ems = cleaned_data.get('email')
            #u = self.cleaned_data.get('username')

            if User.objects.filter(username=u):
                return HttpResponse('user')
                #raise forms.ValidationError("Username Already exist")
            elif User.objects.filter(email=l):
                return HttpResponse('email')
                #raise forms.ValidationError("Email already exist")
            else:
                form.save()
                print(form)
                #return HttpResponseRedirect('/accounts/login')
                return HttpResponse('OK')
            #return HttpResponse('error')

    return render(request,'registration/registration.html',{'form':form})


def regi(request):
    form=Registrationform(request.POST or None)
    #pform = Registrationformprofile(request.POST)
    #pform=Registrationformprofile(data=request.POST,instance=request.user.profile)
    print("before")
    if request.method=='POST' and form.is_valid():
        print("valiiddd")
        #if e:
        #    return HttpResponse('email')
        form.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request,'registration/registration.html',{'form':form})

"""def auth_view(request):
    args={}
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username=form.cleaned_data.get('username')
        password=form.cleaned_data.get('password')
    args['form']=form
    return render(request,'registration/logins.html',args)"""""

def auth_view(request):
    if request.method=='POST':
        response_data={}
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        u=User.objects.filter(username=username)
        if not u:
            return HttpResponse('username')
        if user is not None:
            auth.login(request, user)
#            response_data['result'] = 'Success'
#            response_data['message'] = 'you are login'
            #return HttpResponse(json.dumps(response_data),content_type="application/json")
            return HttpResponseRedirect('/')
        elif request.user.is_authenticated():
            return HttpResponseRedirect('/')
        else:


#            form = LoginForm(request.POST)
#            c = {'form': form}
#            c.update(csrf(request))
 #           response_data['result'] = 'fail'
  #          response_data['message'] = 'do not'
            return HttpResponse('not')
            #return HttpResponse(json.dumps(response_data),content_type="application/json")

            #return render(request, 'registration/login.html', c)"""""

def grade(request):
    return render_to_response('grade.html')


def code_list(request,year,month):
    #s=Sessions.objects.filter(session=month.capitalize())[0].id
    l=QOA.objects.filter(year=year,session=month)
    c=[]

    #for i in l:
    #    c.append(i.code.title)
        #print(i.code)
    return render_to_response('code.html',{'c':Subject.objects.all()})
    #return HttpResponse(set(c))

def question_paper(request,year,month,code):
    q=QOA.objects.filter(code=code,year=year,session=month)
    context={
        'question':q,
        'q':q[0]
    }
    return render_to_response('solved_answer.html',context)

    #return HttpResponse("lkhdslkf")

def result(request):
    enrol=request.GET['enrol']
    option=request.GET['Program']
    url='https://webservices.ignou.ac.in/GradecardM/result.asp?eno='+enrol+'&program='+option+'&HIDDEN_submit=OK'
    print(url)
    r=requests.get(url)
    print(r.status_code)
    soup=BS(r.content,'html.parser')
    #print(soup)
    enrol=soup.find_all('b')[3].text
    name=soup.find_all('b')[4].text
    prog=soup.find_all('b')[5].text
    info=[str(enrol),str(name),str(prog)]
    main=[]
    m=0
    num=0
    tr=soup.find_all('tr')
    for i in tr:
        temp=[]
        td=i.find_all('td')
        for j in td:
            temp.append(j.text)
        main.append(temp)


    return render_to_response('result.html',{'info':info,'mark':main,'user':request.user})

""""        if form.is_valid():
            response_data['result'] = 'Success'
            response_data['message'] = 'you are login'
        else:
            response_data['result'] = 'fail'
            response_data['message'] = 'do not'
        return HttpResponse(json.dumps(response_data),content_type="application/json")"""""
"""def auth_view(request):
    username=request.POST.get('username','')
    password=request.POST.get('password','')
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request,user)
        return HttpResponseRedirect('/')
    elif request.user.is_authenticated():
        return HttpResponseRedirect('/')
    else:
        form=LoginForm(request.POST)
        c={'form':form}
        c.update(csrf(request))
        return render(request,'registration/login.html',c)
        """
