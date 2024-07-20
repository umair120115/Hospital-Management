from rest_framework import serializers
from .models import AppUser,Appointment,AdmitRoom,HospitalMembers

class AppUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=AppUser
        fields=['doctor_id','password','name','description','dob','department','timing','age','is_active','is_staff']

    def create(self, validated_data):
        user=AppUser.objects.create_user(**validated_data)
        
        return user
    



class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Appointment
        fields='__all__'

class AdmitRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model=AdmitRoom
        fields='__all__'

class HospitalMembersSerializer(serializers.ModelSerializer):
    class Meta:
        model=HospitalMembers
        fields='__all__'