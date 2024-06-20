from django.shortcuts import render
from api.models import Student
from api.serializers import StudentSerializer
from rest_framework.generics import ListAPIView
# Create your views here.

class StudentList(ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer