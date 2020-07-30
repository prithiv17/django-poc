from rest_framework import serializers
from .models import Empdetails

class EmpdetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empdetails
        fields = '__all__'