from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

# Register your models here.

admin.site.register(Usuario,UserAdmin)
admin.site.register(Participante)
admin.site.register(Responsable)
admin.site.register(Instructor)
admin.site.register(RegPaciente)
admin.site.register(Expaciente)
admin.site.register(Expacienteingreso)
admin.site.register(Exprogramacirugia)
admin.site.register(Exsala)
admin.site.register(Hoespecialidad)
admin.site.register(Homedico)
admin.site.register(PacientesUsuario)
admin.site.register(PacientesUsuarioGroups)
admin.site.register(PacientesUsuarioUserPermissions)
admin.site.register(Pvpaquete)
admin.site.register(Sitipoingreso)
