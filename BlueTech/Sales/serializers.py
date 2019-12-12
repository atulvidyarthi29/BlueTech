from rest_framework import serializers
from .models import *
from Users.models import Employee
from django.contrib.auth.models import User

class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'

class LeadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lead
        fields = '__all__'

class userdataSerializer(serializers.ModelSerializer):
    user=serializers.ReadOnlyField(source=Employee.user)
    class Meta:
        model=Employee
        fields=('user', 'first_name','last_name','position')




