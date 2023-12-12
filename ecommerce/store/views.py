from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from .forms import CustomUserForm
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.core.mail import EmailMessage
import random
from django.contrib.auth.hashers import make_password 


def home(request):
    # category = Category.objects.all()
    # print("---------------------------category", category)
    # context = {'category': category}
    return render(request, "store/index.html")


def register(request):
    forms = CustomUserForm()
    if request.method == 'POST':
        forms = CustomUserForm(request.POST)
        if forms.is_valid():
            forms.save()
            messages.success(request, "Registered Successfully")
            return redirect('/login')

    context = {'forms': forms}
    return render(request, "store/register.html", context)


def loginpage(request):
    if request.user.is_authenticated:
        messages.success(request, "Already logged in !")
        return redirect('/')
    else:
        if request.method == 'POST':
            name = request.POST.get('username')
            passwd = request.POST.get('password')
            user = authenticate(request, username=name, password=passwd)

            if user is not None:
                login(request, user)
                messages.success(request, "Logged in Successfully")
                return redirect("/")
            else:
                messages.error(request, "Invalid Username or Password")
                return redirect('/login')
        return render(request, "store/login.html")


def logoutpage(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "Logged Out Successfully")
    return redirect("/")

def forgetpassword(request):
    token = random.randint(1111,9999)  
    if request.method == "POST":
        reset_email = request.POST.get('resetemail')
        if Register_user.objects.filter(email = reset_email ).exists():
            subject = 'Reset password'          
            message = f"your reset password otp in {token}"   
            from_email = 'recordsdevelopment@gmail.com'   
            email = EmailMessage(subject, message, from_email, [reset_email])   
            email.send()      
            inistances = Register_user.objects.filter(email =  reset_email).first() 
            inistances.token = token       
            inistances.save()     
            messages.success(request, "OTP Sent! ")
            return redirect('/otpscreen')
            
        else:
            messages.error(request, "Invalid Email")
    return render (request, 'store/forgetpassword.html')



def otpscreen(request):
    if request.method == 'POST':
        otp = request.POST.get('otpscreen')
        if Register_user.objects.filter(token = otp).exists():
            data = Register_user.objects.filter(token = otp).first()
            email = data.email
            return redirect('/resetpassword/'+ email)
        else:
            messages.error(request, "Invalid OTP! ")
    return render (request, 'store/otpscreen.html', )



def resetpassword(request, email):
    if request.method == 'POST':
        new_password = request.POST.get('newpassword')
        confirm_password = request.POST.get('confirmpassword')
        if new_password == confirm_password:
            newpassword = make_password(new_password)
            data =  Register_user.objects.get(email = email)
            data.password = newpassword
            data.save()
            messages.success(request, 'Password reset successfully')
            return redirect('/')
    return render (request, 'store/resetpassword.html')        







