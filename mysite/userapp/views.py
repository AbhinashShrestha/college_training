from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,lagout
from userapp.forms import RegisterForm
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method =="POST":
        form=RegisterForm(request.POST)
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
    return render(request,'usermanagement/register.html',context)