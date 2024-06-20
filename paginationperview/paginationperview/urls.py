from django.contrib import admin
from django.urls import path
from api.views import StudentList
urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/',StudentList.as_view(),name='studentlist')
]
