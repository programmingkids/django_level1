"""django_level1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import include
from chapter03 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chapter02/', include('chapter02.urls')),
    path('work01/', views.work01),
    path('work02/', views.work02),
    path('work03/', views.work03),
    path('chapter03/', include('chapter03.urls')),
    path('chapter04/', include('chapter04.urls')),
    path('chapter05/', include('chapter05.urls')),
    path('chapter06/', include('chapter06.urls')),
    path('chapter07/', include('chapter07.urls')),
    path('chapter08/', include('chapter08.urls')),
    path('chapter09/', include('chapter09.urls')),
]
