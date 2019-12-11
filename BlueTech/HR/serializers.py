from rest_framework import serializers
from . models import *

class MeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model=Meeting
        fields= '__all__'
