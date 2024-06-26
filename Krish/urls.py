"""Krish URL Configuration

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
from django.urls import path, re_path
from django.urls.conf import include
from home.views import mainpage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('',include('home.urls')),
    path('',mainpage.as_view(),),
    path('',include('imgupload.urls')),
    path('',include('consult.urls')),
    path('',include('weatherapp.urls')),
    re_path(r'^i18n/', include('django.conf.urls.i18n')),
    re_path(r'^rosetta/', include('rosetta.urls')),
    path('', include('pwa.urls')),
]
