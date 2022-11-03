"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from config import settings
from school_system_app import views, hodView
urlpatterns = [
    path('demo/', views.showDemoPage, name='demo'),
    path('admin_home', hodView.hod_View, name='hod_view'),
    path('add_staff', hodView.add_staff),
    path('', views.ShowLoginPage, name="home"),
    path('get_user_details', views.get_user_details),
    path('logout_user', views.logout_user),
    path('dologin', views.doLogin, name="doLogin"),
    path('admin/', admin.site.urls),
    path('add_staff_save', hodView.add_staff_save),
    path('add_course', hodView.add_course),
    path('add_course_save', hodView.add_course_save),
    path('add_student', hodView.add_student),
    path('add_student_save', hodView.add_student_save),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
