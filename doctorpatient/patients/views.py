from django.shortcuts import render
from .models import *

# Create your views here.
def doc(request):
    user = Doctor.objects.all()
    print(user)
    return render(request,'doctordata.html',{'user':user})


def pat(request):
    pat = Patient.objects.all()
    return render(request,'doctordata.html',{'user':pat})