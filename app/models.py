from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Doctor(models.Model):
    Name=models.CharField(max_length=100)
    mobile=models.IntegerField()
    special=models.CharField(max_length=100)
    def __str__(self):
        return self.Name
class Patient(models.Model):
    name=models.CharField(max_length=100)
    mobile=models.IntegerField(null=True)
    gender=models.CharField(max_length=100)
    address=models.TextField()
    def __str__(self):
        return self.name

class Appointment(models.Model):
    Doctor=models.ForeignKey('Doctor',on_delete=models.CASCADE)
    Patient=models.ForeignKey('Patient',on_delete=models.CASCADE)
    date=models.DateField()
    time=models.TimeField()

