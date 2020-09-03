from rest_framework import serializers
from .models import Empdetails, CustomerDetails

class EmpdetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empdetails
        fields = '__all__'

class CustomerDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerDetails
        fields = '__all__'