from django.shortcuts import render
from .models import personalInfo
from rest_framework import viewsets, status
from .serializers import PersonalSerializer

# Create your views here.

class PersonalViewSet(viewsets.ModelViewSet):
    queryset = personalInfo.objects.all() #used by serializers output
    serializer_class =  PersonalSerializer
    
