from .models import * 
from .serializable import * 


def stagePackage (stage):
    tasks = task.objects.filter(parent = stage)

            # ------ done tasks ------

    tasksPackage = []
    for l in tasks :
        steps_r = steps.objects.filter(parent = l)
        done = steps.objects.filter(parent = l , done = True )
        todo = {
            'task' : taskSER(l).data ,
            'statistics' : {
                'done' : done.count() ,
                'total' : steps_r.count()
            } ,
            'steps' : stepsSER(steps_r,many = True).data
        }
        tasksPackage.append(todo)
    return tasksPackage


def selectStage(proj) :
    stages = Stage_table.objects.filter(parent = proj)
    
    totalSteps = 0
    doneSteps = 0
    index = 0 
    for k in stages : 
        tasks = task.objects.filter(parent = k )
        if tasks.count() :
            for t in tasks : 
                doneSteps += steps.objects.filter(parent = t , done = True).count()
                totalSteps += steps.objects.filter(parent = t ).count()
            
            if totalSteps != doneSteps :

                return {
                    'stage' : Stage_tableSER(k).data ,
                    'tasks' : stagePackage(k) ,
                    'totalStages' : stages.count() ,
                    'currentStage' : index + 1
                    
                    }
        index += 1
    return None

