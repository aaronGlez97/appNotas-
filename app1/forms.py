from django import forms


from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from django.forms import ModelForm
from app1.models import Notas


#extendiendo el formulario de inicio de sesion
#con este codigo extiendo mi modelo de inicio de sesion del formulario 
class UserCreationForm(UserCreationForm):
    class Meta:
        fields=["username","first_name","last_name","email"]
        model=get_user_model()

class AgregarNota(ModelForm):
    
    nota=forms.Textarea
     
    class Meta:
        model=Notas
        fields=['titulo','nota']  
        
