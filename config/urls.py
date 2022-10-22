"""insektizid URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include
from django.views.generic import TemplateView

react_app_view = TemplateView.as_view(template_name="base.html")

urlpatterns = [
    path("", TemplateView.as_view(template_name="pages/home.html"), name="home"),
    path( "about/", TemplateView.as_view(template_name="pages/about.html"), name="about"),
    # Django Admin, use {% url 'admin:index' %}
    # path(settings.ADMIN_URL, admin.site.urls),
    path('accounts/', include("django.contrib.auth.urls")),

    # User management
    # path("users/", include("insektizid.users.urls", namespace="users'")),
    # path("accounts/", include("allauth.urls")),

    # 
    # path("login/", TemplateView.as_view(template_name="registration/login.html"), name="my_login" ),
    # path("forgot-password/", TemplateView.as_view(template_name="auth/forgot_password.html"), name="forgot_password" ),
    # path("create-account/", TemplateView.as_view(template_name="auth/create_account.html"), name="create_account" ),


    ### REACT APP ROUTES
    # this route catches the "naked" URL with no path specified. you can link to it in most places
    path('app/', react_app_view, name='react_app'),  
    # this route catches any url below the main one, passing it to the front end
    path('app/<path:path>', react_app_view, name='react_app'),  

]