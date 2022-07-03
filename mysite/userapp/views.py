from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from userapp.forms import RegisterForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordResetForm
# Create your views here.
def register(request):
    if request.method =="POST":
        form=RegisterForm(request.POST)
        import ipdb;ipdb.set_trace()
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            raw_password=form.cleaned_data.get('password1')
            user=authenticate(username=username,password=raw_password)
            # login(request,user)
            messages.success(request,"Registration sucessful")
            return redirect('user_login')
    else:
        form=RegisterForm()
    context={"form":form}
    return render(request,'userapp/register.html',context)
def user_login(request):
    if request.method=='POST':
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            raw_password=form.cleaned_data.get('password1')
            user=authenticate(username=username,password=raw_password)
            if user is not None:
                login(request,user)
                return redirect('laptop-list')
            else:
                messages.error(request,"You are not registered yet")
        else:
            messages.error(request,"Invalid credentials")
    form = AuthenticationForm()
    return render(request,'userapp/login.html',{'form':form})