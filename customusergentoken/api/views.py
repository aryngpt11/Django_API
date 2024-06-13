from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializers
    authentication_classes=[TokenAuthentication]

    #isauthenticated only authorized person
    #permission_classes=[IsAuthenticated] #all user are able to use this functionality who have the login crededintals like ssuperuser admin and normal user
    #permission_classes=[IsAuthenticatedOrReadOnly]
