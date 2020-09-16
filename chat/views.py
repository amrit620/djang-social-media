from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

from .models import Post

from .forms import CreateUserForm,MakePost
from django.contrib import messages


def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'Account was successfully created for '+user)

           

            return redirect('login')

    context = {'form':form}
    return render(request,'reg.html',context)

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,'Username or Password incorrect!!!')


    return render(request,'login.html')

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def home(request):
    post = Post.objects.all()
    
    
    context = {'post':post,}
    return render(request,'home.html',context)



@login_required(login_url='login')
def createPost(request):
    
    form = MakePost()
    if request.method == 'POST':
        form = MakePost(request.POST,request.FILES)
        if form.is_valid():
            name = request.user.first_name
            form.save()
            return redirect('home')

    context = {
        'form':form
    }
    return render(request,'create.html',context)


