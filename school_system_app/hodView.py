from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from school_system_app.models import *
from django.core.files.storage import FileSystemStorage

def hod_View(request):
    return render(request, "hod_templates/home_content.html")


# STUDENT
def add_student(request):
    courses = Courses.objects.all
    response ={'courses': courses}
    return render(request, "hod_templates/add_student.html", response)


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
        gender = request.POST.get("gender")
        session_start = request.POST.get("session_start")
        session_end = request.POST.get("session_end")
        course_id = request.POST.get("course")
        if request.FILES['image']:
            file = request.FILES['image']
            fs = FileSystemStorage()
            filename = fs.save(file.name, file)
            profile_pic_url = fs.url(filename)

        try:
            user = CustomUser.objects.create_user(
                username=username,
                first_name=first_name,
                last_name=last_name,
                password=password,
                email=email,
                user_type=3 
            )
            user.students.gender = gender
            user.students.session_start_year=session_start
            user.students.session_end_year=session_end 
            user.students.address = address
            user.profile_pic = profile_pic_url
            user.save()
            messages.success(request, "Successfully added Student")
            return HttpResponseRedirect("/add_student")
        except:
            messages.error(request, "Failed to add Student")
            return HttpResponseRedirect("/add_student")


def manage_students(request):
    students = Students.objects.all()
    return render(request, "hod_templates/manage_students.html",{"students": students})


def edit_student(request, student_id):
    courses = Courses.objects.all()
    student = Students.objects.get(id=student_id)
    return render(request, "hod_templates/edit_student.html", {"student": student,"courses": courses})

def edit_student_save(request):
    if request.method != "POST":
        return HttpResponse("Method not allowed")
    else:
        student_id  = request.POST.get("student_id")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        username = request.POST.get("username")
        address = request.POST.get("address")
        gender = request.POST.get("gender")
        session_start = request.POST.get("session_start")
        session_end = request.POST.get("session_end")
        course_id = request.POST.get("course")
        
        if request.FILES['image-upload']:
            file = request.FILES['image-upload']
            fs = FileSystemStorage()
            filename = fs.save(file.name, file)
            profile_pic_url = fs.url(filename)
        else:
            profile_pic_url = None
        try:
            user = CustomUser.objects.get(id=student_id)
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.username = username
            user.save()
            student = Students.objects.get(admin_id=student_id)
            student.address = address
            student.gender = gender
            student.profile_pic = profile_pic_url
            student.session_start_year = session_start
            student.session_end_year = session_end
            course = Courses.objects.get(id=course_id)
            student.course_id = course
            student.save()
            messages.success(request, "Successfully edited Student")
            return HttpResponseRedirect("/edit_student/" + student_id)
        except:
            messages.error(request, "Failed to edit Student")
            return HttpResponseRedirect("/edit_student/" + student_id)


# STAFF
def add_staff(request):
    return render(request, "hod_templates/add_staff.html")


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


def manage_staffs(request):
    staffs = Staffs.objects.all()
    return render(request, "hod_templates/manage_staffs.html",{"staffs": staffs})

def edit_staff(request, staff_id):
    staffs = Staffs.objects.get(admin=staff_id)
    return render(request, "hod_templates/edit_staff.html",{"staffs":staffs})



# COURSE
def add_course(request):
    return render(request, "hod_templates/add_course.html")


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


def edit_course(request):
    return render(request, "hod_templates/edit_course.html")

def manage_courses(request):
    return render(request, "hod_templates/manage_courses.html")


# SUBJECT

def add_subject(request):
    return render(request, "hod_templates/add_subject.html")


def add_subject_save(request):
    pass


def manage_subjects(request):
    pass


def edt_subject(request):
    pass

