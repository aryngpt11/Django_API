from rest_framework import serializers
from api.models import Student






class StudentSerializer(serializers.ModelSerializer):
    def start_with_a(value):
        if value[0].lower() != 'a':
            raise serializers.ValidationError('Name should be satrt with A')
    #we have to write explicitly
    name=serializers.CharField(validators=[start_with_a])
    class Meta:
        model=Student
        fields=['name','roll','city']


    
    #Field Level Validation

    def validate_roll(self,value):   #roll me jo input krnge whi value aayega
        if value >=200:
            raise serializers.ValidationError("Seat full")
        return value
    
    #object level Validation

    """ def validate(self, data):
        nm=data.get('name')
        ct=data.get('city')
        if nm.lower() =='aryan' and ct.lower() !='ballia':
            raise serializers.ValidationError("city must be ballia")
        return data """
    
    #Validators third type of validataion


        