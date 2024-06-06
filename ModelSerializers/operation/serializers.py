from rest_framework import serializers
from operation.models import Student

class StudentSerializer(serializers.ModelSerializer):
    #name=serializers.CharField(read_only=True) #add any validation only in one feild
    class Meta:
        model=Student
        fields=['name','roll','city']
        #or
        #read_only_fields=['name','roll']
        #or
        extra_kwargs={'name':{'read_only':True}}







    
