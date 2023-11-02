from rest_framework import serializers
from .models import CustomUser,Product
from rest_framework import serializers



    
class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = CustomUser
        fields = ['username','email', 'password','first_name','last_name','birthday']
        

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'