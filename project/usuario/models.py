from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField(null=True)
    avatar = models.ImageField(upload_to="avatares", null=True, blank=True)
    
    def __str__(self):
        return f"{self.apellido}, {self.nombre}"

