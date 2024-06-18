"""
URL configuration for scopedthrotlling project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from api.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('StudentList/',StudentList.as_view(),name='StudentList'),
    path('StudentListt/',StudentListt.as_view(),name='StudentListt'),
    path('StudentCreate/',StudentCreate.as_view(),name='StudentCreate'),
    path('StudentRetrieve/<int:pk>',StudentRetrieve.as_view(),name='StudentRetrieve'),
    path('StudentUpdate/<int:pk>',StudentUpdate.as_view(),name='StudentUpdate'),
    path('StudentDestroy/<int:pk>',StudentDestroy.as_view(),name='StudentDestroy'),

    #path('StudentList/<int:pk>',RUDStudentRetrieve.as_view(),name='StudentDelete')
]
