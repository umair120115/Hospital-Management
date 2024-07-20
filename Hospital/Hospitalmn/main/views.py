from django.shortcuts import render
from .serializers import *
from rest_framework import generics,filters
from .models import *
from rest_framework.permissions import AllowAny,IsAuthenticated,IsAdminUser


# Create your views here.
class CreateUserView(generics.ListCreateAPIView):
    permission_classes=[AllowAny]
    serializer_class=AppUserSerializer
    queryset=AppUser.objects.all()
    filter_backends=[filters.SearchFilter]# for searching use of django_filters library
    search_fields = ['=department', '^name']

class AppointmentEntryView(generics.CreateAPIView):
    permission_classes=[AllowAny]
    serializer_class=AppointmentSerializer
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()
              


class AppointmentGetView(generics.ListAPIView):
    permission_classes=[IsAuthenticated]
    serializer_class=AppointmentSerializer
    def get_queryset(self):
        user=self.request.user['name']
        return Appointment.objects.filter(doctor_name=user)
    
class HospitalMembersView(generics.ListCreateAPIView):
    permission_classes=[AllowAny]
    serializer_class=HospitalMembersSerializer
    queryset=HospitalMembers.objects.all()

    def perform_create(self,serializer):
        if serializer.is_valid():
            serializer.save()


     
        

    