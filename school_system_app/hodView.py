from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from school_system_app.models import Courses, CustomUser


def hod_View(request):
    return render(request, "hod_templates/home_content.html")

def add_student(request):
    course = Courses.objects.all
    return render(request, "hod_templates/add_student.html")

def add_staff(request):
    return render(request, "hod_templates/add_staff.html")

def add_course(request):
    return render(request, "hod_templates/add_course.html")


def add_staff_save(request):
    if request.method != "POST":
        return HttpResponse("Method not allowed")
    else:
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        username = request.POST.get("username")
        address = request.POST.get("address")
        try:
            user = CustomUser.objects.create_user(
                username=username,
                first_name=first_name,
                last_name=last_name,
                password=password,
                email=email,
                user_type=2
            )
            user.staffs.address = address
            user.save()
            messages.success(request, "Successfully added Staff")
            return HttpResponseRedirect("/add_staff")
        except:
            messages.error(request, "Failed to add Staff")
            return HttpResponseRedirect("/add_staff")

def add_course_save(request):
    if request.method != "POST":
        return HttpResponse("Method not allowed")
    else:
        course = request.POST.get("course")
        try:
            course_model = Courses(course_name = course)
            course_model.save()
            messages.success(request, "Successfully added Course "+ course)
            return HttpResponseRedirect("/add_course")
        except:
            messages.error(request, "Failed to add Course")
            return HttpResponseRedirect("/add_course")

def add_student_save(request):
    if request.method != "POST":
        return HttpResponse("Method not allowed")
    else:
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        username = request.POST.get("username")
        address = request.POST.get("address")
        course_id = request.POST.get("course")
        gender = request.POST.get("gender")
        session_start = request.POST.get("session_start")
        session_end = request.POST.get("session_end")
        user.students.gender = gender
        user.students.course_id = course_obj
        course_obj = Courses.objects.get(id =course_id)
        user.students.session_start_year=session_start
        user.students.session_end_year=session_end
        user.students.profile_pic=""
        try:
            user = CustomUser.objects.create_user(
                username=username,
                first_name=first_name,
                last_name=last_name,
                password=password,
                email=email,
                user_type=3 
            )
            user.students.address = address
            user.save()
            messages.success(request, "Successfully added Staff")
            return HttpResponseRedirect("/add_staff")
        except:
            messages.error(request, "Failed to add Staff")
            return HttpResponseRedirect("/add_staff")
