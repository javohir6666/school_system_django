from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

from school_system_app.EmailBackEnd import EmailBackEnd

# Create your views here.
def showDemoPage(request):
    return render(request, 'demo.html')

def ShowLoginPage(request):
    return render(request, 'login-page.html')

def doLogin(request):
    if request.method!="POST":
        return HttpResponse("<h2> Method Not Allowed </h2>")
    else:
        user = EmailBackEnd.authenticate(request, request.POST.get('email'), request.POST.get('password'))
        if user!=None:
            
        return HttpResponse("Email : "+request.POST.get("email")+ " Password: " +request.POST.get("password"))