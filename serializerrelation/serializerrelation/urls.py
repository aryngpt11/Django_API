from django.contrib import admin
from django.urls import path,include
from api.views import SingerViewSet,SongViewSet
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('singer',SingerViewSet,basename='singer')
router.register('song',SongViewSet,basename='song')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('auth/',include('rest_framework.urls',namespace='rest_framework'))
]
