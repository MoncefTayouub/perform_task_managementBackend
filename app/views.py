from unicodedata import category
from django.shortcuts import render
from .models import * 
from rest_framework.response import *
from rest_framework.decorators import api_view
from rest_framework import permissions
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.renderers import * 
from django.core.files.images import ImageFile
from django.core.mail import *
from django.conf import settings
from django.contrib.auth import authenticate
import random
import string
from django.contrib.auth.models import User
from calendar import *
from .Manipulation import *
import json
from .serializable import * 
# Create your views here.
from datetime import * 

@api_view(['GET'])
def home(request):

    general_data = general.objects.all()
    if general_data.count() :
        general_data = general.objects.first() 
    return Response( {     
           'general' : generalSER(general_data).data ,
           'projects' : ProjectSER( Project.objects.all() , many = True ).data
            })

@api_view(['GET','POST','PUT','DELETE'])
def general_v(request):
    if request.method == 'PUT' :
        rq = general.objects.all()
        if rq.count() : 
            fr = rq.first() 
        else :
            fr = rq.create()
        fr.quote = request.POST.get('quote')
        fr.save()

    return Response( {     
           'we are home'
            })

@api_view(['GET','POST','PUT','DELETE'])
def project_rq(request):
    if request.method == 'POST' :
        rq = Project.objects.create()
        rq.name = request.POST.get('name')
        rq.save()
    if request.method == 'GET' : 
        proj_id = int(request.GET.get('data', ''))
        projetct = Project.objects.get(id=proj_id)
        stage = selectStage(projetct)
        
            
        return Response({
            'project' :ProjectSER(projetct ).data  ,
            'stage' : stage        
        }) 
    if request.method == 'PUT' :
        rq = Project.objects.get( id =  request.POST.get('id'))
        rq.name = request.POST.get('name')
        rq.save() 
        return Response('')     
    if request.method == 'DELETE' :
        rq = Project.objects.get(id = request.POST.get('id'))
        rq.delete()
        return Response('')
       
    return Response({   

        })   

@api_view(['GET','POST','PUT','DELETE'])
def stage_rq(request):

    if request.method == 'POST' :
        rq = Stage_table.objects.create()
        rq.name = request.POST.get('name')
        rq.parent = Project.objects.get(id = request.POST.get('id'))
        rq.save()
        return Response('')
    
    if request.method == 'PUT' :
        rq = Stage_table.objects.get(id=request.POST.get('id'))
        rq.name = request.POST.get('name')
        rq.save()  
        return Response('')
    
    if request.method == 'DELETE' :
        rq = Stage_table.objects.get(id = request.POST.get('id'))
        rq.delete()
        return Response('')

    if request.method == 'GET' :
        rq = Project.objects.get(id = int(request.GET.get('data', '')) )
        sq = Stage_table.objects.filter(parent = rq)
        sqSER = Stage_tableSER(sq , many = True).data
        index = 0
        for k in sq :
            sqSER[index]['todo'] = stagePackage(k) 
            index += 1 

        return Response({
            'project' : ProjectSER(rq).data ,
            'stages' : sqSER,
            
        })  
    
@api_view(['GET','POST','PUT','DELETE'])
def task_rq(request):

    if request.method == 'POST' :
        rq = task.objects.create()
        rq.name = request.POST.get('name')
        rq.parent = Stage_table.objects.get(id = int(request.POST.get('id')))
        rq.save()
        return Response('')
    
    if request.method == 'PUT' :
        rq = task.objects.get(id=request.POST.get('id'))
        rq.name = request.POST.get('name')
        rq.save()
        return Response('')  
    
    if request.method == 'DELETE' :
        rq = task.objects.get(id = request.POST.get('id'))
        rq.delete()  
        return Response('')  

@api_view(['GET','POST','PUT','DELETE'])
def steps_rq(request):
    if request.method == 'POST' :
        rq = steps.objects.create()
        rq.name = request.POST.get('name')
        rq.parent = task.objects.get(id = int(request.POST.get('id')))
        rq.save()
        return Response('')  
    if request.method == 'PUT' :
        rq = steps.objects.get(id = request.POST.get('id'))
        rq.name = request.POST.get('name')
        done = request.POST.get('done')
        if done is not None:
            if done == 'True' :
                rq.done = True
            else :
                rq.done = False
        rq.save()
    
    if request.method == 'DELETE' :
        rq = steps.objects.get(id = request.POST.get('id'))
        rq.delete()
  
    return Response('')