import re
from urllib import response
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import csv
from .forms import *
from .models import *
from .decorators import *
from .filters import PacienteFilter
from .models import RegPaciente , Expacienteingreso, Expaciente
from .forms import PacienteForm, Expacienteingresoform
from django.db.models import Q
from django.db import connection
from django.http import HttpResponseRedirect



# ----- USUARIOS LOGIN Y LOGOUT

@login_required(login_url='login')
def home(request):
    context = {}
    return render(request, 'inicio.html', context)

@unauthenticated_user
def registro(request):
    form = CrearUsuarioForm()

    if request.method == 'POST':
        form = CrearUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,f"Usuario {user} creado con exito")

            return redirect('login')
    
    context = {'form':form}
    return render(request,'registro.html',context)

@unauthenticated_user
def loginPag(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password =request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('inicio')
        else:
            messages.info(request, 'Nombre de usuario o contraseña incorrecto')
    context = {}
    return render(request, 'login.html', context)

def logoutUsuario(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def verPerfil(request):
    context = {}
    return render(request,'ver_perfil.html',context)

@login_required(login_url='login')
def editarPerfil(request):
    user = request.user
    form = UserForm(instance=user)

    if request.method == 'POST':
        form = UserForm(request.POST,request.FILES,instance=user)
        if form.is_valid():
            form.save()
            
    context = {'form':form}
    return render(request,'editar_perfil.html',context)


# --------------------------------------------------------------------------------------#

@login_required(login_url='login')
@allowed_users(allowed_roles=['RESPONSABLE'])

def Expaciente_list(request):
    if request.method == "POST":
        pacienteform = RegPacienteForm(request.POST)
        pacienteingresoform = Expacienteingresoform(request.POST)

        if pacienteform.is_valid() and pacienteingresoform.is_valid():
            pacienteform.save()
            pacienteingresoform.save()

        else:
            context = {
                'pacienteform': pacienteform,
                'pacienteingresoform': pacienteingresoform,
            }    
        return render(request, 'SIOH.html', context)

def ArchivoClinico(request):
    responsable = request.user
    registropacientes = RegPaciente.objects.filter(Q(estatus__contains = '0') | Q(estatus__contains = '1'))
    paciente_count = registropacientes.count()
    context = {'registropacientes':registropacientes, 'paciente_count':paciente_count,'responsable':responsable}
    return render(request,'ArchivoClinico.html', context)

@login_required(login_url='login')
def DatosPaciente(request,pk):
    paciente = RegPaciente.objects.get(id=pk)
    context = {'paciente':paciente}
    return render(request,'Propuesta.html', context)


@login_required(login_url='login')
#def DatosPacienteSIOH(request,pk):
  #if request.method == "POST":
   #     pacienteform = RegPacienteForm(request.POST)
    #    pacienteingresoform = Expacienteingresoform(request.POST)

     #   if pacienteform.is_valid() and pacienteingresoform.is_valid():
      #      pacienteform.save()
       #     pacienteingresoform.save()
        #    return HttpResponseRedirect('/success')  

        #else:
         #   context = {
          #      'pacienteform': pacienteform,
           #     'pacienteingresoform': pacienteingresoform,
            #}    
        #return render(request, 'SIOH.html', context)


@login_required(login_url='login')
def updatePaciente(request, pk):
    paciente = RegPaciente.objects.get(id=pk)
    form = PacienteForm(instance=paciente)

    if request.method == 'POST':
        form = PacienteForm(request.POST, instance=paciente)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    context = {'form': form}
    return render(request,'Paciente_Hospitalizacion_form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['RESPONSABLE'])
def createPacienteHospitalizacion(request,pk):
    responsable = Responsable.objects.get(id=pk)
    form = PacienteForm(initial={'responsable':responsable},instance=responsable)
    form.responsable = responsable
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ArchivoClinico')
        

    context = {'form': form,'responsable':responsable}
    return render(request,'Paciente_Hospitalizacion_form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['RESPONSABLE'])
def createPacienteUrgencias(request,pk):
    responsable = Responsable.objects.get(id=pk)
    form = PacienteForm(initial={'responsable':responsable},instance=responsable)
    form.responsable = responsable
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ArchivoClinico')
        

    context = {'form': form,'responsable':responsable}
    return render(request,'Paciente_Urgencias_form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['RESPONSABLE'])
def deletePropuesta(request, pk):
    paciente = RegPaciente.objects.get(id=pk)
    if request.method == 'POST':
        paciente.delete()
        return redirect('ArchivoClinico')
    return render(request,'borrar_paciente.html', {'obj':paciente})

#-----------Consejo Divisional --------------#
@login_required(login_url='login')
def AllDatosPacientes(request):
    if request.user.is_superuser:
        Datospac = RegPaciente.objects.filter(Q(estatus__contains = '1') | Q(estatus__contains = '0'))
        paciente_count = Datospac.count()
        context = {'Datospac':Datospac, 'paciente_count':paciente_count}
        return render(request,'AllDatosPacientes.html', context)
    else:
         return redirect('inicio')

def actualizar(request,pk):
    paciente = RegPaciente.objects.get(id=pk)
    form = PacienteForm(instance=paciente)

    if request.method == 'POST':
        form = PacienteForm(request.POST, instance=paciente)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    context = {'form': form,'paciente':paciente}
    return render(request,'actualizar_estatus.html', context)


  

@login_required(login_url='login')
def AllPacientes(request):
        registropacientes = RegPaciente.objects.filter(Q(estatus__contains = '1'))
        paciente_count = registropacientes.count()
        context = {'registropacientes':registropacientes, 'paciente_count':paciente_count}
        return render(request,'Pacientes.html', context)

@login_required(login_url='login')
def TusEventos(request):
    if(((request.user.is_superuser)&(request.user.rol != 'PARTICIPANTE')) | (request.user.rol == 'RESPONSABLE')):
        responsable = request.user
        registropacientes = RegPaciente.objects.filter(Q(estatus__contains = '1') | Q(estatus__contains = '0'))
        paciente_count = registropacientes.count()
        context = {'registropacientes':registropacientes, 'paciente_count':paciente_count,'responsable':responsable}
        return render(request,'TusEventos.html', context)
    else:
        return redirect('inicio')

def export(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename= "pacientes.csv"' 

    writer = csv.writer(response)
    writer.writerow(['id','Expediente','Numero de cuenta','Fecha de ingreso','Hora de ingreso'
                    ,'Fecha de egreso','Hora de egreso','Dias de estancia','Nombre del Paciente','Lugar de Egreso','Sexo',
                    'Tipo de paciente','Tipo de ingreso','Cirugia','Medico Tratante','Medico Anestesiologo',
                    'Tipo de Anestesia', 'CIE10','Diagnostico CIE10', 'Recoi', 'Diagnostico Recoi','Procedimiento'
                    ,'Fecha de Cirugia','Nacido Vivo','Peso RN','Talla RN','Salpingo Puerperio','Motivo de Egreso', 'Reingreso','Certficado','Numero de Certificado','Observaciones','Estatus'])

    for paciente in RegPaciente.objects.all().values_list('id','Expediente','NumeroCuenta','FechaIngreso','HoraIngreso','FechaEgreso'
    ,'HoraEgreso','DiasEstancia','NombrePaciente','LugarEgreso','sexo','TipoPaciente','TipoIngreso','Cirugia','MedicoTratante',
    'MedicoAnestesiologo','TipoAnestesia','Cie10','DiagnosticoCIE10','Recoi','DiagnosticoRecoi','Procedimiento','FechaCirugia'
    ,'NacidoVivo','PesoRN','TallaRN','SalpingoPuerperio','MotivoEgreso','Reingreso'
    ,'Certificado','NumeroCertificado','Observaciones','estatus'):
        writer.writerow(paciente)
  
    return response

def BuscarPaciente(request):
    if request.method == "POST":
        buscar = request.POST['buscar']
        pacientes = RegPaciente.objects.filter(Q(NombrePaciente__icontains = buscar))

        return render(request, 'buscador.html',{'buscar':buscar,'pacientes':pacientes})
    else:
        return render(request, 'buscador.html',{})

   
