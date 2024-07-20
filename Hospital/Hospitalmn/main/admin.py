from django.contrib import admin
from .models import AppUser,HospitalMembers,Appointment,AdmitRoom
# Register your models here.
admin.site.register(AppUser)
admin.site.register(HospitalMembers)
admin.site.register(Appointment)
admin.site.register(AdmitRoom)