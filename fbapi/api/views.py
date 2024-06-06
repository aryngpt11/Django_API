from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
#function based 
@api_view()
def hello_world(request):
    return Response({'msg':'Hello World'})  #response data == python native data type
