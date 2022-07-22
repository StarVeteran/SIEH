import django_filters
from django_filters import DateFilter
from .models import RegPaciente

class PacienteFilter(django_filters.FilterSet):
    class Meta:
        model = RegPaciente
        fields = '__all__'
        exclude = ['Expediente','NumeroCuenta','DiasEstancia','FechaIngreso','HoraIngreso','FechaEgreso','HoraEgreso','TipoPaciente','TipoIngreso','Cirugia','MedicoTratante','MedicoAnestesiologo','TipoAnestesia','DiagnosticoRecoi','Procedimiento','Cie10','DiagnosticoCIE10','Recoi','FechaCirugia','NacidoVivo','PesoRN','TallaRN','SalpingoPuerperio','MotivoEgreso','Reingreso','Certificado','NumeroCertificado','Observaciones','estatus','sexo','Edad','LugarEgreso']