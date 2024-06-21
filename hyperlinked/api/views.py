from django.shortcuts import render
from api.models import Student
from rest_framework import viewsets
from api.serializers import StudentSerializer
# Create your views here.
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
