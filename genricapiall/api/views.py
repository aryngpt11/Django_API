#GenericAPIView and Model Mixin

from api.models import Student
from api.serializers import StudentSerializers
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin


#List and create  pk not required
class LCStudentList(GenericAPIView, ListModelMixin,CreateModelMixin):
    queryset=Student.objects.all()
    serializer_class=StudentSerializers #which serializer we want to use
    
    def get(self,request,*args,**kwargs):
            return self.list(request,*args,**kwargs)
    
    def post(self,request,*args,**kwargs):
            return self.create(request,*args,**kwargs)
    
class RUDStudentRetrieve(GenericAPIView, RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset=Student.objects.all()
    serializer_class=StudentSerializers
    
    def get(self,request,*args,**kwargs):
            return self.retrieve(request,*args,**kwargs)

    def put(self,request,*args,**kwargs):
            return self.update(request,*args,**kwargs)

    def delete(self,request,*args,**kwargs):
            return self.destroy(request,*args,**kwargs)