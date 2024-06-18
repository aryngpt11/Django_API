from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser,IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly
from rest_framework.throttling import AnonRateThrottle,UserRateThrottle

from api.throttling import JackRateThrottle

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializers
    authentication_classes=[SessionAuthentication]

    #isauthenticated only authorized person
    #permission_classes=[IsAuthenticated] #all user are able to use this functionality who have the login crededintals like ssuperuser admin and normal user
    permission_classes=[IsAuthenticatedOrReadOnly]
    throttle_classes=[AnonRateThrottle,UserRateThrottle]
class StudentModelViewSet1(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializers
    authentication_classes=[SessionAuthentication]
    permission_classes=[AllowAny]
    throttle_classes=[AnonRateThrottle,JackRateThrottle]
    
class StudentModelViewSet2(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializers
    authentication_classes=[SessionAuthentication]
    permission_classes=[IsAdminUser]

class StudentModelViewSet3(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializers
    authentication_classes=[SessionAuthentication]
    permission_classes=[DjangoModelPermissions]

class StudentModelViewSet4(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializers
    authentication_classes=[SessionAuthentication]
    permission_classes=[DjangoModelPermissionsOrAnonReadOnly]