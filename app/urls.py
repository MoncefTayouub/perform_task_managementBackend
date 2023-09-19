from django.urls import path 
from . import views 


urlpatterns = [
     path('', views.home ) ,
     path('general', views.general_v ) ,
     path('project', views.project_rq ) ,
     path('stage', views.stage_rq ) ,
     path('task', views.task_rq ) ,   
     path('step', views.steps_rq ) ,   
] 