from __future__ import unicode_literals
from tabnanny import verbose
from django.db import models



class JobManager(models.Manager):
    def basic_validator(self, postData):
        errores = {}
        if len(postData["title"]) < 4:
            errores["title"] = "Titulo de tarea debe tener mas de 4 caracteres"
        if len(postData["desc"]) < 10:
            errores["desc"]= "Descripcion de la tarea debe tener mas de 10 caracteres"
        return errores 

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, unique=True, null=True)
    password = models.CharField(max_length=100)
    cpassword = models.CharField(max_length=100,null=True, blank=True)

    
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ['first_name']
        
    def __str__(self):
        return f"{self.name}"
    
    
class Job(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField( blank=True, null=True)
    location = models.CharField(max_length=255)
    usuario_job = models.ForeignKey(User, related_name="jobs", on_delete = models.CASCADE, null=True, blank=True) # El usuario que subio un libro
    
    
    def __str__(self):
        return f"{self.title}- {self.desc}-{self.location}"
    
    