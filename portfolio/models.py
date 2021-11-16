from django.db import models

# AGREGAR APP A WEBPERSONAL/SETTINGS - INSTALLED APPS

# Create your models here.
class Project(models.Model): # model representa una tabla dentro de la base de datos
  title = models.CharField(max_length=200)
  description = models.TextField()
  image = models.ImageField()
  
  # Almaceno fecha de creacion y fecha de edicion del campo
  cretaed = models.DateTimeField(auto_now_add=True) # campo de fecha y hora
  updated = models.DateTimeField(auto_now=True)
  
  # diferencia entre auto_now_add y auto_now es que auto_now se actualiza cada vez que 
  # hacemos un cambio, y auto_now_add se actualiza solamente el dia de la creación