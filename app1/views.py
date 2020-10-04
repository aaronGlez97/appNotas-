from django.shortcuts import render,redirect

from django.contrib.auth import logout as do_logout


from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from app1.forms import UserCreationForm
#from django.contrib.auth.forms import UserCreationForm

from app1.forms import AgregarNota
from app1.models import Notas 

from django.contrib.auth.models import User



# Create your views here.



def welcome(request):

    if request.user.is_authenticated:
      #obteniendo el id del usuario que se autentico 
      userID=request.user.id
      #ejecutando el querie que filtra las notas de los usuarios por medio del usuario que inicio sesion
      notas=Notas.objects.filter(usuarionotas_id=userID)


      
      form=AgregarNota(initial={'usuarionotas_id':userID,}) 
      return render(request, "inicio.html",{"form":form, "notas": notas })
    return redirect('/login') 



def register(request):

    
    # Creamos el formulario de autenticación vacío
    form = UserCreationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = UserCreationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():

            # Creamos la nueva cuenta de usuario
            user = form.save()

            # Si el usuario se crea correctamente 
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/')

    form.fields['username'].help_text = None
    form.fields['password1'].help_text = None
    form.fields['password2'].help_text = None            

    # Si llegamos al final renderizamos el formulario
    return render(request, "register.html", {'form': form})
   

def login(request):
    form = AuthenticationForm()

    if request.method == "POST":

         form= AuthenticationForm(data=request.POST)

         if form.is_valid():

              # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)

            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/')

    # Si llegamos al final renderizamos el formulario
    return render(request, "login.html", {'form': form})




def logout(request):

    # Redireccionamos a la portada
    do_logout(request)
    
    return redirect('/')


def mostrarNotas(request):
    if request.user.is_authenticated:
      #obteniendo el id del usuario que se autentico 
      userID=request.user.id
      #ejecutando el querie que filtra las notas de los usuarios por medio del usuario que inicio sesion
      notas=Notas.objects.filter(usuarionotas_id=userID)

    return render(request,"misnotas.html",{'notas':notas})



def agregarNota(request):
    
    if request.method=='POST':
       
        form=AgregarNota(request.POST)
        if form.is_valid:
            
            #se crea una instancia del formulario para que todavia no se guarde y despues se asigna el id del usuario
            #logeado con request.user y despues se guarda el formulario 
            form1=form.save(commit=False)
            form1.usuarionotas=request.user        
            form1.save()


            return render(request,"addnota.html")
    else:
      #obteniendo el id del usuario que se autentico 
        userID=request.user.id
        form=AgregarNota(initial={'usuarionotas_id':userID,})
        
       

        return render(request,"agregarNota.html", {"form":form})

def eliminar(request):

    if request.user.is_authenticated:
      #obteniendo el id del usuario que se autentico 
      userID=request.user.id
      #ejecutando el querie que filtra las notas de los usuarios por medio del usuario que inicio sesion
      notas=Notas.objects.filter(usuarionotas_id=userID)

    return render(request, "eliminar.html", {'notas':notas })  

def eliminarnota(request):

    if request.POST["id1"]:

        form=request.POST["id1"]

        notas=Notas.objects.filter(id=form) 
        notas.delete()
        return render(request, "eliminado.html") 
    else :
       if request.user.is_authenticated:
        #obteniendo el id del usuario que se autentico 
        userID=request.user.id
        #ejecutando el querie que filtra las notas de los usuarios por medio del usuario que inicio sesion
       notas=Notas.objects.filter(usuarionotas_id=userID)

       return render(request, "misnotas.html", {'notas':notas})

   

def actualizarRegistro(request, items_id):

    #creando una instancia para pasarle los datos del registro al formulario y despues actualizarlos
    instancia=Notas.objects.get(id=items_id)
    form=AgregarNota(instance=instancia)

    if request.method=="POST":
        
        form=AgregarNota(request.POST, instance=instancia)

        if form.is_valid():
            #funcion para actualizar el registro despues se vuelve a crear una instancia del formulario para limpiar el registro  
            instancia.save()

            form=AgregarNota()
        #si el registro es exitoso se le redirecciona a una vista que confirma la actualizacion como exitosa
        return render(request, "editar.html", {'form': form}) 
    else :
        instancia=Notas.objects.get(id=items_id)

        form= AgregarNota(instance= instancia )

   
    return render(request,"editarRegistro.html", {'form': form})

    