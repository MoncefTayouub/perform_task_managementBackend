from dataclasses import fields
from rest_framework import serializers
from .models import *



class generalSER(serializers.ModelSerializer):
    class Meta :
        fields = '__all__'
        model = general 

class ProjectSER(serializers.ModelSerializer):
    class Meta :
        fields = '__all__'
        model = Project 

class Stage_tableSER(serializers.ModelSerializer):
    class Meta :
        fields = '__all__'
        model = Stage_table 

class taskSER(serializers.ModelSerializer):
    class Meta :
        fields = '__all__'
        model = task 

class stepsSER(serializers.ModelSerializer):
    class Meta :
        fields = '__all__'
        model = steps 