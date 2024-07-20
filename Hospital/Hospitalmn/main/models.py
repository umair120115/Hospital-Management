from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.
class AppUserManager(BaseUserManager):
    def create_user(self,doctor_id,password=None,**extra_fields):
        if not doctor_id:
            raise ValueError("Doctor id is must")
        if not password:
            raise ValueError("Password is must")
        user=self.model(doctor_id=doctor_id,**extra_fields)
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('is_member',True)
        extra_fields.setdefault('is_staff',True)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self,doctor_id,password,**extra_fields):
        extra_fields.setdefault('is_superuser',True)
        user=self.create_user(doctor_id,password,**extra_fields)
        return user


class AppUser(AbstractBaseUser):
    doctor_id=models.IntegerField(unique=True)
    password=models.CharField(max_length=20)
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=300)
    age=models.IntegerField()
    dob=models.DateField()
    joined=models.DateField(auto_now_add=True)
    timing=models.CharField(max_length=100)
    department=models.CharField(max_length=100)
    is_active=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    is_member=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)



    USERNAME_FIELD='doctor_id'
    REQUIRED_FIELDS=['name','description','age','dob','department','timing'] 
    def __str__(self):
        return self.name
    objects=AppUserManager()
    
    def has_module_perms(self,app_label):
        return True
    def has_perm(self,perm,obj=None):
        return True


class Appointment(models.Model):
    doctor_name=models.CharField(max_length=100)
    date_appointment=models.DateField(auto_now_add=True)
    patient_name=models.CharField(max_length=100)
    patient_father=models.CharField(max_length=100)
    patient_mobile=models.IntegerField()


class HospitalMembers(models.Model):
    name=models.CharField(max_length=100)
    post=models.CharField(max_length=50)
    age=models.IntegerField()
    address=models.CharField(max_length=300)


class AdmitRoom(models.Model):
    romm_no=models.IntegerField(unique=True)
    patient_name=models.CharField(max_length=100)
    doctor_name=models.CharField(max_length=100)
    patient_details=models.TextField()






