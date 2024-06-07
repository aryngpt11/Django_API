from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import Student
from api.serializers import StudentSerializers
from rest_framework import status
# Create your views here.
@api_view(['GET','POST','PUT','PATCH','DELETE'])

def student_api(request, pk=None):
    if request.method=='GET':
        id=pk
        if id is not None:
            stu=Student.objects.get(id=id)
            serializer=StudentSerializers(stu)
            return Response(serializer.data)
        stu=Student.objects.all()
        serializer=StudentSerializers(stu, many=True)
        return Response(serializer.data) 
    if request.method=='POST':
        serializer=StudentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    if request.method=='PUT':
        #id=pk or
        stu=Student.objects.get(pk=pk)
        serializer=StudentSerializers(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Data Updated'}) #pyhton dict ke form me
        return Response(serializer.errors)
    
    if request.method=='PATCH':
        #id=pk or
        stu=Student.objects.get(pk=pk)
        serializer=StudentSerializers(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial Data Updated'}) #pyhton dict ke form me
        return Response(serializer.errors)
    
    if request.method=='DELETE':
        #id=pk or
        stu=Student.objects.get(pk=pk)
        stu.delete()
        return Response({'msg':'Data Deleted'})
