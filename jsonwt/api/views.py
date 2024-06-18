from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
#from api.customauth import *
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializers
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated] #all user are able to use this functionality who have the login crededintals like ssuperuser admin and normal user
    