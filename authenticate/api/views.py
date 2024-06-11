from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializers
    authentication_classes=[BasicAuthentication]

    #isauthenticated only authorized person
    permission_classes=[IsAuthenticated] #all user are able to use this functionality who have the login crededintals like ssuperuser admin and normal user

class StudentModelViewSet1(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializers
    authentication_classes=[BasicAuthentication]
    permission_classes=[AllowAny]
    
class StudentModelViewSet2(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializers
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAdminUser]