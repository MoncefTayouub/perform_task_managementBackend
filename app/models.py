from django.db import models

# Create your models here.

class general (models.Model):
    quote = models.TextField() 
    BGC = models.TextField()
    S_BGC = models.TextField()
    TC = models.TextField()
    STC = models.TextField()
    def __str__(self):
        return self.quote

class Project (models.Model):
    name = models.TextField() 
    def __str__(self):
        return self.name



class Stage_table (models.Model) :
    name = models.TextField() 
    parent = models.ForeignKey(Project, on_delete=models.CASCADE,null=True,blank=True) 
    def __str__(self):
        return self.name

class task (models.Model) :
    name = models.TextField() 
    parent = models.ForeignKey(Stage_table, on_delete=models.CASCADE,null=True,blank=True) 
    def __str__(self):
        return self.name

class steps (models.Model) :
    name = models.TextField() 
    parent = models.ForeignKey(task, on_delete=models.CASCADE,null=True,blank=True) 
    done = models.BooleanField(default=False)
    def __str__(self):
        return self.name