from django.shortcuts import render
from CourseExplorer.forms import Signup
import requests
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from .models import KooferData,CourseExplorerData,RateMyProfessor
# Dummy method
def index(request):
    return render(request, "base.html")
# Controller for login page
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/index/')
            else:
                return HttpResponse('Your account is disabled. Please activate it')
        else:
            return HttpResponse("Login Failed, please check your username and password")
    else:
        return render(request, 'login.html')
# Controller for sign-up page
def user_signup(request):
    if request.method == 'POST':
        user_form = Signup(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            return HttpResponseRedirect('/ce/index/')
        else:
            error = "Please fill out all the fields"
            return render(request, 'error.html')
    else:
        user_form = Signup()
        print("Hello")
        return render(request, "signup.html", {'form': user_form})

# User index page
def user_index(request):
    c = KooferData.objects.all()
    return render(request,'index.html', {'c':c})
def user_search(request):
    if request.method == 'POST':
        course_name = request.POST.get('search', False);
        course_explorer_data = CourseExplorerData.objects.filter(number=course_name)
        koofer_data = KooferData.objects.filter(number=course_name)
        r = requests.get('https://www.reddit.com/r/UIUC/search.json?q='+course_name+'&restrict_sr=on')
        for x in RateMyProfessor.objects.all():
            if x.instructor.number == course_explorer_data[0].number:
                return render(request, 'index.html', {'c': course_explorer_data[0], 'k': koofer_data[0], 'r': x, 'red'
                :r.json()})
    else:
        return render(request,'search.html')
def landing(request):
    return render(request,'landing.html')
