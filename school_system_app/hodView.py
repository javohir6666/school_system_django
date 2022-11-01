from django.shortcuts import render

def hod_View(request):
    return render(request, "hod_templates/home_content.html")

def add_staff(request):
    return render(request, "hod_templates/add_staff.html")