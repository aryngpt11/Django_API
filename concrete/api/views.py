#concrete View Class

from api.models import *
from api.serializers import *
from rest_framework.generics import ListAPIView,ListCreateAPIView,CreateAPIView,UpdateAPIView,RetrieveAPIView,DestroyAPIView

class StudentList(ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializers

class StudentCreate(CreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializers

class StudentListt(ListCreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializers

class StudentRetrieve(RetrieveAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializers

class StudentUpdate(UpdateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializers

class StudentDestroy(DestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializers