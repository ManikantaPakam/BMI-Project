from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from Registation import settings
from django.contrib.auth.decorators import login_required


# Create your views here.

def signup_view(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if pass1 != pass2:
            messages.error(request,"Your password and confirm password didn't match....!")

        if User.objects.filter(username=username):
            messages.error(request,'Your username already existed...!')
            return redirect('/home')

        if User.objects.filter(email=email):
            messages.error(request,'Your email Id already existed...!')
            return redirect('/home')

        myuser = User.objects.create_user(username, email, pass1)
        myuser.save()
        messages.success(request,'Your account has been created successfully.')

        #Welcome Email

        subject = "Welcome to BMI World...!"
        message = "Hello " + myuser.first_name + "!!  \n" + "Welcome to BMI!! \n Thank you for visiting our website \n Your account have been created successfully. \n\n Thanking you \n Manikanta"
        from_email = settings.EMAIL_HOST_USER
        to_list = [myuser.email]
        send_mail(subject, message, from_email, to_list, fail_silently=True)
        return redirect('/signin')

    return render(request,'app1/signup.html')

def signin_view(request):

    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(request,username=username, password=pass1)

        if user is not None:
            login(request,user)
            return render(request,'app1/home.html')
        else:
            messages.error(request,'Bad credential.')
            return redirect('/signin')

    return render(request,'app1/signin.html')


@login_required
def home_view(request):
    return render(request,'app1/home.html')


@login_required
def metric_view(request):
    context = {}
    if request.method == 'POST':
        name = request.POST['name']
        gender = request.POST['gender']
        weight = float(request.POST['weight'])
        height = float(request.POST['height'])

        bmi = (weight / (height ** 2))

        if bmi < 16:
            state = 'Sever Thinness'
        elif (bmi > 16 and bmi < 20):
            state = 'Mild Thinness'
        elif (bmi > 20 and bmi < 25):
            state = 'Normal'
        elif (bmi > 25 and bmi < 30):
            state = 'OverWeigt'
        elif (bmi > 30 and bmi < 35):
            state = 'Obese Class I'
        elif (bmi > 35 and bmi < 40):
            state = 'Obese Class II'

        context["bmi"] = bmi
        context["state"] = state

    return render(request,'app1/metric.html',context)

@login_required
def imperial_view(request):
    context = {}
    if request.method == 'POST':
        name = request.POST['name']
        gender = request.POST['gender']
        weight = float(request.POST['weight']) / 2.205
        height = (float(request.POST['feet']) * 30.48 + float(request.POST['inches']) * 2.54) / 100

        bmi = (weight / (height ** 2))

        if bmi < 16:
            state = 'Sever Thinness'
        elif (bmi > 16 and bmi < 20):
            state = 'Mild Thinness'
        elif (bmi > 20 and bmi < 25):
            state = 'Normal'
        elif (bmi > 25 and bmi < 30):
            state = 'OverWeigt'
        elif (bmi > 30 and bmi < 35):
            state = 'Obese Class I'
        elif (bmi > 35 and bmi < 40):
            state = 'Obese Class II'

        context["bmi"] = bmi
        context["state"] = state

    return render(request,'app1/imperial.html',context)