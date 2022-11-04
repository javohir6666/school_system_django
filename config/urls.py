from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from config import settings
from school_system_app import views, hodView
urlpatterns = [
    path('demo/', views.showDemoPage, name='demo'),
    path('admin_home', hodView.hod_View, name='hod_view'),

    path('', views.ShowLoginPage, name="home"),
    path('get_user_details', views.get_user_details),
    path('logout_user', views.logout_user),
    path('dologin', views.doLogin, name="doLogin"),
    path('admin/', admin.site.urls),
    # COURSE
    path('add_course', hodView.add_course),
    path('add_course_save', hodView.add_course_save),
    path('manage_courses', hodView.manage_courses),
    # SUBJECT
    path('add_subject', hodView.add_subject),
    path('manage_subjects', hodView.manage_subjects),
    path('add_subject_save', hodView.add_subject_save),
    # STAFF
    path('add_staff', hodView.add_staff),
    path('add_staff_save', hodView.add_staff_save),
    path('edit_staff/<str:staff_id>/', hodView.edit_staff),
    path('manage_staffs', hodView.manage_staffs),
    #STUDENT
    path('add_student', hodView.add_student),
    path('manage_students', hodView.manage_students),
    path('edit_student/<str:student_id>/', hodView.edit_student),
    path('add_student_save', hodView.add_student_save),
    path('edit_student_save', hodView.edit_student_save),
    

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
