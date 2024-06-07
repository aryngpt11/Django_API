from django.shortcuts import render
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializers
from rest_framework import status
from rest_framework.views import APIView  #class based api view

class StudentAPI(APIView):
    def get(self,request,pk=None,format=None):
        id=pk
        if id is not None:
            stu=Student.objects.get(id=id)
            serializer=StudentSerializers(stu)
            return Response(serializer.data)
        stu=Student.objects.all()
        serializer=StudentSerializers(stu, many=True)
        return Response(serializer.data) 
    def post(self,request,format=None):
        serializer=StudentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,pk=None,format=None):
        #id=pk or
        stu=Student.objects.get(pk=pk)
        serializer=StudentSerializers(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Data Updated'}) #pyhton dict ke form me
        return Response(serializer.errors)
    
    def patch(self,request,pk=None,format=None):
        #id=pk or
        stu=Student.objects.get(pk=pk)
        serializer=StudentSerializers(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial Data Updated'}) #pyhton dict ke form me
        return Response(serializer.errors)
    

    def delete(self,request,pk=None,format=None):
        #id=pk or
        stu=Student.objects.get(pk=pk)
        stu.delete()
        return Response({'msg':'Data Deleted'})











        
    
        
    
   
        
    
