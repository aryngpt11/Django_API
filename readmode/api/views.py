from .models import *
from .serializers import *
from rest_framework import viewsets

class StudentReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializers