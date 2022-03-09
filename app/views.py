from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib import messages
from app.forms import  UserForm, LoginForm, JobForm
from app.models import User, Job
import bcrypt

def index(request):
    
    if 'usuario' not in request.session:
        return redirect('/login')
    
    tareas = Job.objects.all()
    
    if request.method == 'POST':
        #POST
        form = JobForm(request.POST)
        if form.is_valid():
            tarea = form.save(commit=False)
            tarea.usuario = User.objects.get(id=request.session["usuario"]["id"])
            tarea.save()            
            messages.success(request, "Tarea agregada correctamente")
            return redirect('/')
        else:
            messages.error(request, "Formulario procesado con errores.")
            return render(request, 'app/index.html', {'form':form, 'tareas': tareas})
    
    else:
        #GET
        context = {
            'form': JobForm(),
            'tareas': tareas
        
    }
    
        return render(request, 'app/index.html', context)




def contacto(request):
    if 'usuario' not in request.session:
        return redirect('/login')
    
    if User.ADMINISTRADOR != request.session['usuario']['role']:
        messages.error(request,"No tienes permisos para entrar a ADMINISTRADOR")
        return redirect('/')
    
    return render(request, 'app/contacto.html')

def register(request):
    
    if 'usuario' in request.session:
        return redirect('/')
    
    
    if request.method == 'POST':
        #POST
        form = UserForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.password = bcrypt.hashpw(usuario.password.encode(), bcrypt.gensalt()).decode()
            usuario.save()            
            messages.success(request, "Usuario creado correctamente")
            return redirect('/')
        else:
            messages.error(request, "Formulario procesado con errroes.")
            return render(request, 'app/register.html', {'form':form})
    else:
        # GET
        context = {
            'form' : UserForm()
        }
        
        return render(request, 'app/register.html', context)
    
def login(request):
    
    if 'usuario' in request.session:
        return redirect('/')
    
    if request.method == 'POST':
        # POST
        user = User.objects.filter(email=request.POST['email'])
        
        if user:
            usuario_login = user[0]
            
            if bcrypt.checkpw(request.POST['password'].encode(),  usuario_login.password.encode()):
                print("USUARIO CORRECTO")
                request.session['usuario'] = { 'nombre':usuario_login.first_name , 'email':usuario_login.email, 'id':usuario_login.id}
                return redirect('/')
            else:
                print("USUARIO NO ES SU CONTRASEÑA")
                messages.error(request, "USUARIO NO ES SU CONTRASEÑA")

        else:
            messages.error(request, "Usuario no encontrado")
        
        return redirect('/login')
            
        
        
    else:
        
        # GET
        context = {
            'form' : LoginForm()
        }
            
        return render(request, 'app/login.html', context)
    
    
def logout(request):
    if 'usuario' in request.session:
        del request.session['usuario']
        
    return redirect('/')




def add(request):
    
    if 'usuario' not in request.session:
        return redirect('/login')
    
    tareas = Job.objects.all()
    
    
    if request.method == 'POST':
        #POST
        form = JobForm(request.POST)
        if form.is_valid():
            tarea = form.save(commit=False)
            tarea.usuario_job = User.objects.get(id=request.session["usuario"]["id"])
            tarea.save()
            messages.success(request, "Tarea añadida correctamente") 
            return redirect("/")
        else:
            messages.error(request, "Tarea no se añadio correctamente.")
            return render(request, "app/add.html", {"form":form, "tareas":tareas}) 
    
    else:
    # GET    
        context = {
        "form" : JobForm(),
        "tareas" : tareas
    }
        return render(request, "app/add.html", context)
    
    
def done(request, id):
    if 'usuario' not in request.session:
        return redirect('/login') 
    
    tarea = Job.objects.get(id=id)
    tarea.delete()   
    messages.success(request, "Tarea eliminada correctamente")
    return redirect("/")

def edit(request, id):
    if 'usuario' not in request.session:
        return redirect('/login') 
    
    tarea = Job.objects.get(id=id)
    if request.session["usuario"]["id"] != tarea.usuario_job.id:
        messages.error(request, "Esta tarea le pertenece a otro usuario.")
        return redirect('/login') 
    
    if request.method == 'POST':
        #POST
        form = JobForm(request.POST, instance=tarea)
        if form.is_valid():
            tarea.save()
            messages.success(request, "Tarea editada correctamente") 
            return redirect("/")
        else:
            messages.error(request, "Tarea no se logro editar.")
            return render(request, "app/edit.html", {"form":form})
    
    
    
    else:
        #GET
        
        form = JobForm(instance=tarea)
        context = {
            "form": form,
            "tarea": tarea,
        }
        return render(request, "app/edit.html", context)
    
    
def ver(request, id):
    usuario = User.objects.get(id=id)
    
    context = {
        "usuario": usuario,
    }
    return render(request, "app/ver.html", context)
