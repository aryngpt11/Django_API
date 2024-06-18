"""
URL configuration for sessionauthenticate project.

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
from django.urls import path,include

from api import views
from rest_framework.routers import DefaultRouter

#creation router object
router=DefaultRouter()

#register StudentViewSet with router
router.register('studentapi',views.StudentModelViewSet,basename='student')
router.register('studentapi1',views.StudentModelViewSet1,basename='student1')
router.register('studentapi2',views.StudentModelViewSet2,basename='student2')
router.register('studentapi3',views.StudentModelViewSet3,basename='student3')
router.register('studentapi4',views.StudentModelViewSet4,basename='student4')
""" router.register('studentapi/<int:pk>',views.StudentViewSet,basename='student') """ #no need to write this it will internally mnaged by router
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/',include('rest_framework.urls',namespace='rest_framework'))
    
]

