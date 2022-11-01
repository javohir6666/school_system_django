from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from school_system_app.EmailBackEnd import EmailBackEnd
from django.contrib import messages
# Create your views here.
def showDemoPage(request):
    return render(request, 'demo.html')

def ShowLoginPage(request):
    return render(request, 'login-page.html')

def doLogin(request):
    if request.method!="POST":
        return HttpResponse("<h2> Method Not Allowed </h2>")
    else:
        user = EmailBackEnd.authenticate(request, username=request.POST.get('email'), password=request.POST.get('password'))
        if user!=None:
            login(request, user)
            return HttpResponseRedirect('hod_view')
        else:
            messages.error(request, "Invalid login details")
            return HttpResponseRedirect('/')
        
def get_user_details(request):
    if request.user !=None:
        return HttpResponse("User: " + request.user.email  + "UserType: " + request.user.user_type)
    else:
        return HttpResponse("Please Login first!")

def logout_user(request):
    logout(request)
    return HttpResponseRedirect("/")