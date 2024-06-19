from django.shortcuts import render
from api.serializers import StudentSerializer
from rest_framework.generics import ListAPIView
from api.models import Student


# Create your views here.

class StudentList(ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
#This method is used if someone wants to access only their data. When the user logs in, only their data is displayed to them.    
    def get_queryset(self):
        user=self.request.user  #request.user consist the curent user
        return Student.objects.filter(passby=user)
    