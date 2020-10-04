from django.db import models
from django.contrib.auth.models import User 
# Create your models here.

class Notas(models.Model):
    usuarionotas=models.ForeignKey(User, on_delete=models.PROTECT  )
    titulo=models.CharField(max_length=100)
    nota=models.TextField()

    

    