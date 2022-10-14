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
from turtle import tracer
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include
from django.views.generic import TemplateView

from insektizid.tracker.views import (
    tracker_home_view
)

urlpatterns = [
    # path('admin/', admin.site.urls),
    path("", TemplateView.as_view(template_name="pages/home.html"), name="home"),
    path( "about/", TemplateView.as_view(template_name="pages/about.html"), name="about"),

    # this route catches the "naked" URL with no path specified. you can link to it in most places
    path('my-react-page/', tracker_home_view , name='react_app'),  

]