from django.db import models

# Create your models here.
class Doctor(models.Model):
    name = models.CharField(max_length=255)
    specialty = models.CharField(max_length=255)

class Patient(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)