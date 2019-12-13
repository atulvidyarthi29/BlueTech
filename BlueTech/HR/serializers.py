from rest_framework import serializers
from . models import *

class MeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meeting
        fields= '__all__'

class TrainingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Training
        fields = ['start_date','end_date','description']

class ComplaintSerializer(serializers.ModelSerializer):

    class Meta:
        model = Complaint
        fields = '__all__'
