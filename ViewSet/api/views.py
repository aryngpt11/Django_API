from django.shortcuts import render
from rest_framework.response import Response
from api.models import *
from api.serializers import *
from rest_framework import status
from rest_framework import viewsets

class StudentViewSet(viewsets.ViewSet):
    def list(self,request):
        print("********List********")
        print("Basename:", self.basename)
        print("Action:", self.action)
        print("Detail:", self.detail)
        print("Suffix:", self.suffix)
        print("Name:", self.name)
        print("Description:", self.description)
        stu=Student.objects.all()
        serializer=StudentSerializers(stu, many=True)
        return Response(serializer.data)
    
    def retrieve(self,request,pk=None):
        id=pk
        if id is not None:
            stu=Student.objects.get(id=id)
            serializer=StudentSerializers(stu)
            return Response(serializer.data)
    def create(self,request):
        serializer=StudentSerializers(data=request.data) #jo data frontend se ya jha se api hit hota h waha se
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def update(self,request,pk):
        id=pk
        stu=Student.objects.get(pk=id)
        serializer=StudentSerializers(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':' Complete Data Updated'},status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def partialupdate(self,request,pk):
        id=pk
        stu=Student.objects.get(pk=id)
        serializer=StudentSerializers(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':' Partial Data Updated'},status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self,request,pk):
        id=pk
        stu=Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg':' Partial Data Updated'},status=status.HTTP_404_NOT_FOUND)

