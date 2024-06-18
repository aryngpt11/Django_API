#concrete View Class

from api.models import *
from api.serializers import *
from rest_framework.generics import ListAPIView,ListCreateAPIView,CreateAPIView,UpdateAPIView,RetrieveAPIView,DestroyAPIView
from rest_framework.throttling import ScopedRateThrottle
class StudentList(ListAPIView):
    queryset=Student.objects.all() 
    serializer_class=StudentSerializers
    throttle_classes=[ScopedRateThrottle]
    throttle_scope='viewstu'

class StudentCreate(CreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializers
    throttle_classes=[ScopedRateThrottle]
    throttle_scope='modifystu'

class StudentListt(ListCreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializers
    throttle_classes=[ScopedRateThrottle]
    throttle_scope='modifystu'


class StudentRetrieve(RetrieveAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializers
    throttle_classes=[ScopedRateThrottle]
    throttle_scope='viewstu'

class StudentUpdate(UpdateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializers
    throttle_classes=[ScopedRateThrottle]
#Destroy
class StudentDestroy(DestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializers
    throttle_classes=[ScopedRateThrottle]