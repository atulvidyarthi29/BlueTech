# from rest_framework import serializers
# from . models import *
# from Users.models import Employee, User
#
# class MeetingSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Meeting
#         fields= ['location', 'description', 'date']
#
# class TrainingSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Training
#         fields= ['start_date', 'end_date', 'description']
#
# class ComplaintSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Complaint
#         fields = ['against', 'complain', 'date']
#
# class UserMeetingSerializer(serializers.ModelSerializer):
#     meeting = MeetingSerializer(many=True, read_only=True)
#
#     class Meta:
#         model = Employee
#         fields = ['first_name', 'last_name']
#
#
# class UserTrainingSerializer(serializers.ModelSerializer):
#     trainings = TrainingSerializer(many=True, read_only=True)
#
#     class Meta:
#         model = Employee
#         fields = ['first_name', 'last_name']
#
#
# class UserComplaintSerializer(serializers.ModelSerializer):
#     complaints = ComplaintSerializer(many=True, read_only=True)
#
#     class Meta:
#         model = Employee
#         fields = ['first_name']
