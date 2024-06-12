from django.contrib import admin
from django.urls import path,include

from api import views
from rest_framework.routers import DefaultRouter

#creation router object
router=DefaultRouter()

#register StudentViewSet with router
router.register('studentapi',views.StudentModelViewSet,basename='student')
#router.register('studentapi1',views.StudentModelViewSet1,basename='student1')
#router.register('studentapi2',views.StudentModelViewSet2,basename='student2')
#router.register('studentapi3',views.StudentModelViewSet3,basename='student3')
#router.register('studentapi4',views.StudentModelViewSet4,basename='student4')
""" router.register('studentapi/<int:pk>',views.StudentViewSet,basename='student') """ #no need to write this it will internally mnaged by router
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/',include('rest_framework.urls',namespace='rest_framework'))
    
]