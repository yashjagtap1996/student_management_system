from django.shortcuts import render,redirect
from .form import Registration
from .models import Student
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    template_name='student_management_system_app/home.html'
    return render(request,template_name)


@login_required(login_url='login')
def registration(request):  
    if request.method=='POST':    
        register=Registration(request.POST)
        if register.is_valid():
            register.save()
            return redirect('data')
    register=Registration() 
    template_name='student_management_system_app/registration.html'
    context={'register':register}
    return render(request,template_name,context)

@login_required(login_url='login')
def data(request):
    stu=Student.objects.all()
    template_name='student_management_system_app/data.html'
    context={'stu':stu}
    return render(request,template_name,context)

def signup(request):
    form=UserCreationForm()
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    template_name='student_management_system_app/signup.html'
    context={'form':form}
    return render(request,template_name,context)

def log_in(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'invalid username or password')
    template_name='student_management_system_app/login.html'
    return render(request,template_name)

def log_out(request):
    logout(request)
    return redirect('login')

def remove(request,id):
    stu=Student.objects.get(id=id)
    stu.delete()
    return redirect('data')

def update(request,id):
    stu=Student.objects.get(id=id)
    if request.method=='POST':    
        register=Registration(request.POST,instance=stu)
        if register.is_valid():
            register.save()
            return redirect('data')
    register=Registration(instance=stu) 
    template_name='student_management_system_app/update.html'
    context={'register':register}
    return render(request,template_name,context)