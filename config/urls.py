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
    path('add_staff', hodView.add_staff, name='hod_view'),
    path('', views.ShowLoginPage, name="home"),
    path('get_user_details', views.get_user_details),
    path('logout_user', views.logout_user),
    path('dologin', views.doLogin, name="doLogin"),
    path('admin/', admin.site.urls),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
