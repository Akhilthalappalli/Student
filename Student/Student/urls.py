"""Student URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from app import views
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('user_register',views.user_register,name="user_register"),
    path('user_dashboard',views.user_dashboard,name="user_dashboard"),
    path('user_dashboard',views.user_dashboard,name="user_dashboard"),
    path('admin_dashboard',views.admin_dashboard,name="admin_dashboard"),
    path('',views.user_login,name="user_login"),
    path('admin_login',views.admin_login,name="admin_login"),
    path('admin_register',views.admin_register,name="admin_register"),
    path('edit_mark/<int:stdid>',views.edit_mark,name="edit_mark"),
    path('admin_logout',views.admin_logout,name="admin_logout"),
    path('user_logout',views.user_logout,name="user_logout"),
    path('edit_profile/<int:stdid>',views.edit_profile,name="edit_profile"),

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
