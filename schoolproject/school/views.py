from django.shortcuts import render
# Create your views here.
from django.shortcuts import render
# Create your views here.
from django.contrib.auth.models import User, auth
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login,logout
from django.shortcuts import render
from django.contrib import messages
from .forms import RegistrationForm, COURSE_CHOICES
from django.contrib.auth import logout as django_logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

def get_courses(request):
    department = request.GET.get('department')
    if department:
        courses = COURSE_CHOICES.get(department, [])
    else:
        courses = []
    return JsonResponse({'courses': courses})


def index(request):
    return render(request,"index.html")

def register1(request):
    if request.method == 'POST':
        user_name = request.POST['Username']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']
        if pass1==pass2:
            if User.objects.filter(username=user_name).exists():
                messages.info(request,"Username taken")
            else:
                user = User.objects.create_user(user_name, pass1, pass2)
                user.save()
                return redirect('login')
        else:
            messages.info(request,"Passwords are not matching")
            return redirect('register1')
    return render(request, "register1.html")

def login(request):
    if request.method == 'POST':
        user_name1 = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request,username=user_name1,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('loggedin')
        else:
            messages.info(request,"Invalid credentials")
            return redirect('login')
    return render(request,"login.html")
def loggedin(request):

    return render(request,"loggedin.html")
@login_required
def regform(request):

    if request.method == 'POST':

        form = RegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Order Confirmed')
            return redirect('confirm')  # Replace 'home' with the URL name of your home page
    else:

        form = RegistrationForm()
    return render(request, 'regform.html', {'form': form})

@login_required
def logout(request):
    django_logout(request)
    return redirect('/')
def confirm(request):
    return render(request,"confirm.html")