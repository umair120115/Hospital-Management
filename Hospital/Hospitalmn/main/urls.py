from django.urls import path
from . import views

urlpatterns=[
    
    path('appointment/register',views.AppointmentEntryView.as_view(),name="appointment_create"),
    path('members/',views.HospitalMembersView.as_view(),name="members")
]