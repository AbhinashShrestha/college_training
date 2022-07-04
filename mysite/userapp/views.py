from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from userapp.forms import RegisterForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.
def register(request):
    if request.method =="POST":
        form=RegisterForm(request.POST)
        # import ipdb;ipdb.set_trace() for debug only
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
            username=form.cleaned_data.get('username')
            raw_password=form.cleaned_data.get('password')
            print(raw_password)
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

def password_reset_request(request):
    if request.method == "POST":
    password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
        data = password_reset_form.cleaned_data['email']
        associated_users = User.objects.filter(Q(email=data))
        if associated_users.exists():
        for user in associated_users:
        subject = "Password Reset Requested"
        email_template_name = "usermanagement/password_reset_email.txt"
        c = {
        "email":user.email,
        'domain':'127.0.0.1:8000',
        'site_name': 'Website',
        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
        "user": user,
        'token': default_token_generator.make_token(user),
        'protocol': 'http',
        }
    email = render_to_string(email_template_name, c)
    try:
    send_mail(subject, email, 'admin@example.com' , [user.email], fail_silently=False)
    except BadHeaderError:
    return HttpResponse('Invalid header found.')
    messages.success(request, 'A message with reset password instructions has been sent to your inbox.')
                    return redirect ("/")
            messages.error(request, 'An invalid email has been entered.')
    password_reset_form = PasswordResetForm()

    return render(request=request, template_name="usermanagement/password_reset_form.htm", context={"password_reset_form":password_reset_form})

def register(request):
    if request.method == "POST":
    form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.success(request, "Registration successful." )
        else:
            form = RegisterForm()
            context = {"form":form}
            return render(request, 'usermanagement/register.htm', context)
    return redirect('user_login')