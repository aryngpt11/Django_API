from .models import *
from .serializers import *
from rest_framework import viewsets

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializers