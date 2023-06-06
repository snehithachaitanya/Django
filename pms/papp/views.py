from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

@login_required(login_url="login")
def home(request):
    return render(request,'bgimage.html')

@login_required(login_url="login")
def hording(request):
    return render(request,'poster.html')

@login_required(login_url="login")
def instagram(request):
    return render(request,'instagram.html')

@login_required(login_url="login")
def news(request):
    return render(request,'news.html')

@login_required(login_url="login")
def onNews(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email = request.POST.get('email')
        pgno = request.POST.get('pgno')
        side = request.POST.get('side')
        data=newsDB(name=name,email=email,page=pgno,side=side)
        data.save()
    return redirect('home')

@login_required(login_url="login")
def onInsta(request):
    if request.method=='POST':
        name=request.POST.get('name')
        em = request.POST.get('id')
        data=instaDB(name=name,ig=em)
        data.save()
    return redirect('home')

def onPomplet(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email = request.POST.get('email')
        pgno = request.POST.get('pgno')
        fold = request.POST.get('fold')
        data=pompletDB(name=name,email=email,page=pgno,fold=fold)
        data.save()
    return redirect('home')

def logIn(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,'username or password is incorrect')
            return render(request, 'longin.html')

    return render(request,'longin.html')

@login_required(login_url="login")
def OnHorror(request):

    if request.method=='POST':
        name=request.POST.get('Name')
        email = request.POST.get('Email')
        msg = request.POST.get('Message')
        data=horrorDB(name=name,email=email,message=msg)
        data.save()
    return render(request,'writer.html')

@login_required(login_url="login")
def onAction(request):
    if request.method=='POST':
        name=request.POST.get('Name')
        email = request.POST.get('Email')
        msg = request.POST.get('Message')
        data=actionDB(name=name,email=email,message=msg)
        data.save()
    return render(request,'writer.html')

@login_required(login_url="login")
def onDev(request):
    if request.method=='POST':
        name=request.POST.get('Name')
        email = request.POST.get('Email')
        msg = request.POST.get('Message')
        data=DevDB(name=name,email=email,message=msg)
        data.save()
    return render(request,'writer.html')

def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'account created sucessfully for '+ user)
            return redirect('login')

    context = {'form' : form}
    return render(request,'reg.html',context)

def logOut(request):
    logout(request)
    return redirect('login')

@login_required(login_url="login")
def writer(request):
    return render(request,'writer.html')

@login_required(login_url="login")
def pomplet(request):
    return render(request,'pomplet.html')

@login_required(login_url="login")
def horror(request):
    return render(request,'horror.html')

@login_required(login_url="login")
def action(request):
    return render(request,'action.html')

@login_required(login_url="login")
def devo(request):
    return render(request,'devotuonal.html')