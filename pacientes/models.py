from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.base import Model
from django.db.models.fields import proxy
from django.core.validators import MaxValueValidator, MinValueValidator 

# Create your models here.

class Usuario(AbstractUser):
    class Roles(models.TextChoices):
        PARTICIPANTE =  "PARTICIPANTE","Participante"
        INSTRUCTOR =  "INSTRUCTOR","Instructor"
        RESPONSABLE =  "RESPONSABLE","Responsable"


    rol = models.CharField(max_length=50,choices=Roles.choices,default=Roles.PARTICIPANTE)
    imagen = models.ImageField(default="male_avatar.svg",null=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class ParticipanteManager(models.Manager):
    def get_queryset(self,*args,**kwargs):
        return super().get_queryset(*args,**kwargs).filter(rol=Usuario.Roles.PARTICIPANTE)

class InstructorManager(models.Manager):
    def get_queryset(self,*args,**kwargs):
        return super().get_queryset(*args,**kwargs).filter(rol=Usuario.Roles.INSTRUCTOR)


class ResponsableManager(models.Manager):
    def get_queryset(self,*args,**kwargs):
        return super().get_queryset(*args,**kwargs).filter(rol=Usuario.Roles.RESPONSABLE)

class Participante(Usuario):
    objects = ParticipanteManager()
    class Meta:
        proxy = True
    
    def save(self,*args,**kwargs):
        if not self.pk:
            self.rol = Usuario.Roles.PARTICIPANTE
        return super().save(*args,**kwargs)

class Instructor(Usuario):
    objects = InstructorManager()
    class Meta:
        proxy = True
    
    def save(self,*args,**kwargs):
        if not self.pk:
            self.rol = Usuario.Roles.INSTRUCTOR
        return super().save(*args,**kwargs)

class Responsable(Usuario):
    objects = ResponsableManager()
    class Meta:
        proxy = True
    
    def save(self,*args,**kwargs):
        if not self.pk:
            self.rol = Usuario.Roles.RESPONSABLE
        return super().save(*args,**kwargs)





#Model que define los campos de registro de pacientes para la base de datos
class RegPaciente(models.Model):
    Expediente = models.IntegerField(blank=True, null=True)
    NumeroCuenta = models.IntegerField(blank=True, null=True, verbose_name='Numero de cuenta')
    FechaIngreso = models.DateField()
    HoraIngreso = models.TimeField()
    FechaEgreso = models.DateField()
    HoraEgreso = models.TimeField()
    DiasEstancia = models.IntegerField(blank=True, null=True)
    NombrePaciente = models.CharField(max_length=150,verbose_name='Nombre del Paciente')
    LugarEgreso = models.CharField(max_length=100) 
    SEXO = (('M', 'M'),
             ('F', 'F'))
    sexo = models.CharField(max_length=50,default=SEXO[0], choices=SEXO)      
    FechaNacimiento = models.DateField(verbose_name='Fecha de Nacimiento')
    TIPO_ATENCION =(
            ('CONSULTA CANCELADA','CONSULTA CANCELADA'),
            ('CONSULTA EXTERNA ESPECIALISTA','CONSULTA EXTERNA ESPECIALISTA '),
            ('ESTANCIA EN URGENCIAS','ESTANCIA EN URGENCIAS'),
            ('ESTUDIO','ESTUDIO'),
            ('PARTICULAR', 'PARTICULAR'),
            ('SURTIR MEDICAMENTO', 'SURTIR MEDICAMENTO'),
            ('TRAMITE ADMINISTRATIVO', 'TRAMITE ADMINISTRATIVO'),
            ('VENTA AL PUBLICO', 'VENTA AL PUBLICO')
        )
    TipoAtencion = models.CharField(max_length=100,default=TIPO_ATENCION[1], choices=TIPO_ATENCION, verbose_name='Tipo de Atencion')
    TIPO_PACIENTE = (
            ('CONVENIO','CONVENIO'),
            ('EMPLEADO','EMPLEADO'),
            ('MEDICO','MEDICO'),
            ('PARTICULAR','PARTICULAR')
        )
    
    TipoPaciente = models.CharField(max_length=100,verbose_name='Tipo de Paciente')
    TIPO_INGRESOS = (
            ('Ambulatorio','Ambulatorio'),
            ('Interno fue Urgencia','Interno fue Urgencia'),
            ('Internamiento Normal','Internamiento Normal'),
            ('Recien Nacido','Recien Nacido'),
            ('Interno fue ambulatorio', 'Interno fue ambulatorio'),
            ('Externo', 'Externo'),
            ('Urgencias', 'Urgencias')
        )
    TipoIngreso = models.CharField(max_length=100,default=TIPO_INGRESOS[1], choices=TIPO_INGRESOS,verbose_name='Tipo de Ingreso')    
    Empresa = models.CharField(max_length=100, blank=True)
    ServicioPrestado = models.CharField(max_length=100, blank=True, null=True)
    Paquete= models.CharField(max_length=100,blank=True)
    Cuarto = models.CharField(max_length=100, blank=True)
    Cirugia =  models.CharField(max_length=100, blank=True)
    SALA_CX = (
            ('SALA 1','SALA 1'),
            ('SALA 2','SALA 2'),
            ('SALA 3','SALA 3'),
            ('SALA ENDOSCOPIA','SALA ENDOSCOPIA'),
            ('SALA LPR', 'SALA LPR'),
    )
    SalaCX =  models.CharField(max_length=100,default=SALA_CX[0], choices=SALA_CX, blank=True)  
    MedicoTratante =  models.CharField(max_length=150,verbose_name='Medico Tratante')
    Especialidad =  models.CharField(max_length=100)
    MedInterconsultante = models.CharField(max_length=150, verbose_name='Medico Interconsultante')
    MedicoAnestesiologo = models.CharField(max_length=150,verbose_name='Medico Anestesiologo')
    TipoAnestesia =  models.CharField(max_length=100, verbose_name='Tipo de Anestesia')
    Diagnostico = models.CharField(max_length=150)
    Cie10 = models.CharField(max_length=50)
    DiagnosticoCIE10 = models.CharField(max_length=150, verbose_name='Diagnostico CIE10')
    Recoi = models.CharField(max_length=20)
    DiagnosticoRecoi = models.CharField(max_length=150, verbose_name='Diagnostico Recoi')
    Procedimiento = models.CharField(max_length=150)
    FechaCirugia = models.CharField(max_length= 50 ,verbose_name='Fecha de Cirugia')
    EgresoUrgencias = models.CharField(max_length=50, verbose_name='Egreso de Urgencias')
    NACIDO_VIVO =( ('Si','Si'),
                ('No','No'),
                ('No Aplica', 'No Aplica')
            )
    NacidoVivo = models.CharField(max_length=250,default=NACIDO_VIVO[2], choices=NACIDO_VIVO) 
    PesoRN = models.CharField(max_length=250, blank=True, null=True)   
    TallaRN = models.CharField(max_length=250, blank=True, null=True)
    MamaRN = models.CharField(max_length=250, blank=True, null=True)
    SalpingoPuerperio = models.CharField(max_length=50, verbose_name='Salpingo Puerperio')
    MotivoEgreso = models.CharField(max_length=50, verbose_name='Motivo de Egreso')
    EgresoCensable = models.CharField(max_length=5, blank=True,null=True)
    Reingreso = models.CharField(max_length=5)
    MotivoReingreso = models.CharField(max_length=100)
    Certificado = models.CharField(max_length=50)
    NumeroCertificado = models.CharField(max_length=100)
    Observaciones = models.CharField(max_length=150, blank=True)
    estatus = models.CharField(max_length=5,default = 1)

class Adtipopaciente(models.Model):
    tnycvetipopaciente = models.IntegerField()
    vchdescripcion = models.CharField(max_length=45)
    bitutilizaplan = models.IntegerField(blank=True, null=True)
    bitutilizaconvenio = models.IntegerField(blank=True, null=True)
    chrtipo = models.CharField(max_length=2, blank=True, null=True)
    bitdesconocido = models.IntegerField(blank=True, null=True)
    bitactivo = models.IntegerField(blank=True, null=True)
    bitfamiliar = models.IntegerField(blank=True, null=True)
    trial562 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'adtipopaciente'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class Ccempresa(models.Model):
    intcveempresa = models.IntegerField(primary_key=True)
    vchdescripcion = models.CharField(max_length=100)
    tnycvetipoconvenio = models.IntegerField()
    chrrfcempresa = models.CharField(max_length=50, blank=True, null=True)
    chrcalle = models.CharField(max_length=250, blank=True, null=True)
    chrtelefonoempresa = models.CharField(max_length=40, blank=True, null=True)
    bitactivo = models.IntegerField(blank=True, null=True)
    intcveciudad = models.IntegerField()
    vchrazonsocial = models.CharField(max_length=200)
    bitmostrarempresapaciente = models.IntegerField(blank=True, null=True)
    intnumcontactocc = models.IntegerField(blank=True, null=True)
    intnumcontactopromotor = models.IntegerField(blank=True, null=True)
    vchobservaciones = models.CharField(max_length=4000, blank=True, null=True)
    vchrequisitosingreso = models.CharField(max_length=4000, blank=True, null=True)
    vchcolonia = models.CharField(max_length=100, blank=True, null=True)
    intestado = models.IntegerField(blank=True, null=True)
    vchgirocomercial = models.CharField(max_length=100, blank=True, null=True)
    intcvepromotor = models.IntegerField(blank=True, null=True)
    vchcodigopostal = models.CharField(max_length=20, blank=True, null=True)
    vchnumerointerior = models.CharField(max_length=50, blank=True, null=True)
    vchnumeroexterior = models.CharField(max_length=50, blank=True, null=True)
    vchcorreo = models.CharField(max_length=100, blank=True, null=True)
    bitdesglosaconceptosseguro = models.IntegerField(blank=True, null=True)
    bitexcluyeconcsegpendientes = models.IntegerField(blank=True, null=True)
    bitcalculaconcsegcondescuento = models.IntegerField(blank=True, null=True)
    bitcalculaconceptoseguroconiva = models.IntegerField(blank=True, null=True)
    bitajustarcfdi = models.IntegerField(blank=True, null=True)
    bitnoidentificacion = models.IntegerField(blank=True, null=True)
    relporcentajeserviciosemp = models.FloatField(blank=True, null=True)
    smicveimpuestoconcepsseg = models.IntegerField(blank=True, null=True)
    vchregimenfiscal = models.CharField(max_length=3, blank=True, null=True)
    trial566 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ccempresa'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('PacientesUsuario', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Expaciente(models.Model):
    exregpaciente = models.ForeignKey(RegPaciente, on_delete=models.DO_NOTHING)
    intnumpaciente = models.IntegerField(primary_key=True)
    intcvetipopaciente = models.IntegerField(blank=True, null=True)
    intcveempresa = models.IntegerField(blank=True, null=True)
    intcvetipopoliza = models.IntegerField(blank=True, null=True)
    intcveempresapaciente = models.IntegerField(blank=True, null=True)
    intcvereligion = models.IntegerField(blank=True, null=True)
    intcveestadocivil = models.IntegerField(blank=True, null=True)
    intcveciudadnacimiento = models.IntegerField(blank=True, null=True)
    intcvenacionalidad = models.IntegerField(blank=True, null=True)
    vchnumexpediente = models.CharField(max_length=50, blank=True, null=True)
    vchapellidopaterno = models.CharField(max_length=100, blank=True, null=True)
    vchapellidomaterno = models.CharField(max_length=100, blank=True, null=True)
    vchnombre = models.CharField(max_length=100, blank=True, null=True)
    chrsexo = models.CharField(max_length=1, blank=True, null=True)
    dtmfechanacimiento = models.DateTimeField(blank=True, null=True)
    vchrfc = models.CharField(max_length=50, blank=True, null=True)
    vchcurp = models.CharField(max_length=50, blank=True, null=True)
    vchocupacion = models.CharField(max_length=100, blank=True, null=True)
    vchcorreoelectronico = models.CharField(max_length=50, blank=True, null=True)
    vchconyugenombre = models.CharField(max_length=100, blank=True, null=True)
    vchconyugeapellidopaterno = models.CharField(max_length=100, blank=True, null=True)
    vchconyugeapellidomaterno = models.CharField(max_length=100, blank=True, null=True)
    vchnombrepadre = models.CharField(max_length=300, blank=True, null=True)
    vchnombremadre = models.CharField(max_length=300, blank=True, null=True)
    vchnumafiliacion = models.CharField(max_length=100, blank=True, null=True)
    vchautorizacion = models.CharField(max_length=100, blank=True, null=True)
    vchnumpoliza = models.CharField(max_length=100, blank=True, null=True)
    intprevio = models.IntegerField(blank=True, null=True)
    intcveocupacion = models.IntegerField(blank=True, null=True)
    intcveidioma = models.IntegerField(blank=True, null=True)
    vchalergias = models.CharField(max_length=1000, blank=True, null=True)
    vchformanacimiento = models.CharField(max_length=7, blank=True, null=True)
    intcvegrupo = models.IntegerField(blank=True, null=True)
    intcvetiposanguineo = models.IntegerField(blank=True, null=True)
    bitenviarpromociones = models.IntegerField(blank=True, null=True)
    dtmfechanacimientoconyuge = models.DateTimeField(blank=True, null=True)
    dtmfechanacimientopadre = models.DateTimeField(blank=True, null=True)
    dtmfechanacimientomadre = models.DateTimeField(blank=True, null=True)
    intembarazada = models.FloatField(blank=True, null=True)
    dtmultimamenstruacion = models.DateTimeField(blank=True, null=True)
    intlactancia = models.IntegerField(blank=True, null=True)
    vchcontrasena = models.CharField(max_length=50, blank=True, null=True)
    vchusuario = models.CharField(max_length=50, blank=True, null=True)
    trial566 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'expaciente'


class Expacienteingreso(models.Model):
    exregpacienteingreso = models.ForeignKey(RegPaciente, null=True, on_delete=models.DO_NOTHING)
    intnumcuenta = models.IntegerField(primary_key=True)
    intnumpaciente = models.IntegerField(blank=True, null=True)
    intcvetipoingreso = models.IntegerField()
    intcveempleadoingreso = models.IntegerField(blank=True, null=True)
    intcvedepartamento = models.IntegerField(blank=True, null=True)
    intcvedeptoingreso = models.IntegerField(blank=True, null=True)
    intcveprocedencia = models.IntegerField(blank=True, null=True)
    intcveempresapaciente = models.IntegerField(blank=True, null=True)
    intcveempleadomodifico = models.IntegerField(blank=True, null=True)
    intcveempleadoegreso = models.IntegerField(blank=True, null=True)
    intcvetipopaciente = models.IntegerField(blank=True, null=True)
    intcveempresa = models.IntegerField(blank=True, null=True)
    intcvetipopoliza = models.IntegerField(blank=True, null=True)
    intnumcuentamama = models.IntegerField(blank=True, null=True)
    intcvemedicorelacionado = models.IntegerField(blank=True, null=True)
    intcveempleadorelacionado = models.IntegerField(blank=True, null=True)
    intcveparentescoemergencia = models.IntegerField(blank=True, null=True)
    intcveparentescoresponsable = models.IntegerField(blank=True, null=True)
    intcvemedicoemergencias = models.IntegerField(blank=True, null=True)
    intcvemedicotratante = models.IntegerField(blank=True, null=True)
    intcvediagnosticoprevio = models.IntegerField(blank=True, null=True)
    intcveestadosalud = models.IntegerField(blank=True, null=True)
    intcvepaquete = models.IntegerField(blank=True, null=True)
    intcveconceptoatencion = models.IntegerField(blank=True, null=True)
    intcvecuarto = models.IntegerField(blank=True, null=True)
    dtmfechahoraingreso = models.DateTimeField(blank=True, null=True)
    dtmfechahoraegreso = models.DateTimeField(blank=True, null=True)
    chrestatus = models.CharField(max_length=1, blank=True, null=True)
    vchnumafiliacion = models.CharField(max_length=100, blank=True, null=True)
    vchautorizacion = models.CharField(max_length=300, blank=True, null=True)
    vchnumpoliza = models.CharField(max_length=100, blank=True, null=True)
    chrtipoatencion = models.CharField(max_length=1, blank=True, null=True)
    numanticiposugerido = models.FloatField(blank=True, null=True)
    vchnombreemergencia = models.CharField(max_length=300, blank=True, null=True)
    vchdomicilioemergencia = models.CharField(max_length=100, blank=True, null=True)
    vchtelefonoemergencia = models.CharField(max_length=50, blank=True, null=True)
    vchnombreresponsable = models.CharField(max_length=300, blank=True, null=True)
    vchdomicilioresponsable = models.CharField(max_length=500, blank=True, null=True)
    vchtelefonoresponsable = models.CharField(max_length=50, blank=True, null=True)
    vchlugartrabajoresponsable = models.CharField(max_length=100, blank=True, null=True)
    vchobservacion = models.CharField(max_length=1400, blank=True, null=True)
    intcuentafacturada = models.IntegerField(blank=True, null=True)
    intcuentacerrada = models.IntegerField(blank=True, null=True)
    intcuentabloqueada = models.IntegerField(blank=True, null=True)
    intcuentaocupada = models.IntegerField(blank=True, null=True)
    intordeninternamiento = models.IntegerField(blank=True, null=True)
    vchdiagnosticoespecifico = models.CharField(max_length=1000, blank=True, null=True)
    vchmotivoingreso = models.CharField(max_length=1000, blank=True, null=True)
    intcvefamiliar = models.IntegerField(blank=True, null=True)
    intcvesocio = models.IntegerField(blank=True, null=True)
    chrtipoingreso = models.CharField(max_length=1)
    dtmfechanacimientoemergencia = models.DateTimeField(blank=True, null=True)
    dtmfechanacimientoresponsable = models.DateTimeField(blank=True, null=True)
    bitclienteexterno = models.IntegerField(blank=True, null=True)
    trial569 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'expacienteingreso'
        unique_together = (('intnumcuenta', 'intcvetipoingreso'),)


class Exprogramacirugia(models.Model):
    intconsecutivo = models.IntegerField(primary_key=True)
    intnumcuenta = models.IntegerField()
    intnumpaciente = models.IntegerField()
    chrtipopaciente = models.CharField(max_length=1)
    dtmfechahora = models.DateTimeField()
    dtmfechahoratermino = models.DateTimeField()
    smiminutosprogramados = models.IntegerField()
    intclavesala = models.IntegerField(blank=True, null=True)
    intcvemedico = models.IntegerField()
    chrestatusprogramacion = models.CharField(max_length=2)
    tnycveanestesia = models.IntegerField()
    intcveempleado = models.IntegerField(blank=True, null=True)
    smicvedepartamento = models.IntegerField()
    trial572 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'exprogramacirugia'


class Exsala(models.Model):
    intclave = models.IntegerField(primary_key=True)
    vchdescripcion = models.CharField(max_length=100)
    intminutoslimpieza = models.IntegerField()
    bitstatus = models.IntegerField(blank=True, null=True)
    trial572 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'exsala'


class Hoespecialidad(models.Model):
    tnycveespecialidad = models.IntegerField(primary_key=True)
    vchdescripcion = models.CharField(max_length=40)
    bitactiva = models.IntegerField(blank=True, null=True)
    chrcvesecundaria = models.CharField(max_length=2, blank=True, null=True)
    trial572 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hoespecialidad'


class Homedico(models.Model):
    intcvemedico = models.IntegerField(primary_key=True)
    vchapellidopaterno = models.CharField(max_length=20)
    vchapellidomaterno = models.CharField(max_length=20)
    vchnombre = models.CharField(max_length=25)
    vchrfcmedico = models.CharField(max_length=15, blank=True, null=True)
    vchcedulaprofesional = models.CharField(max_length=10, blank=True, null=True)
    vchregsalubridad = models.CharField(max_length=15, blank=True, null=True)
    chrsexo = models.CharField(max_length=1)
    vchpartcalle = models.CharField(max_length=200, blank=True, null=True)
    vchpartcolonia = models.CharField(max_length=100, blank=True, null=True)
    vchpartcodpostal = models.CharField(max_length=10, blank=True, null=True)
    vchconsulcalle = models.CharField(max_length=60, blank=True, null=True)
    vchconsulcolonia = models.CharField(max_length=100, blank=True, null=True)
    vchconsulcodpostal = models.CharField(max_length=10, blank=True, null=True)
    bitestaactivo = models.IntegerField(blank=True, null=True)
    vchhorario = models.CharField(max_length=60, blank=True, null=True)
    vchemail = models.CharField(max_length=100, blank=True, null=True)
    vchgrupo = models.CharField(max_length=1, blank=True, null=True)
    bitdiagnoimagen = models.CharField(max_length=1)
    vchpassword = models.CharField(max_length=120, blank=True, null=True)
    bitisr = models.IntegerField()
    bitcomisiones = models.IntegerField()
    bitemergencias = models.IntegerField()
    intcveempleado = models.IntegerField(blank=True, null=True)
    intareaservicio = models.IntegerField(blank=True, null=True)
    intesppredeterminada = models.IntegerField()
    intcveciudad = models.IntegerField(blank=True, null=True)
    bitinternoresidente = models.IntegerField()
    vchpartnumeroexterior = models.CharField(max_length=100, blank=True, null=True)
    vchpartnumerointerior = models.CharField(max_length=100, blank=True, null=True)
    vchconsulnumeroexterior = models.CharField(max_length=100, blank=True, null=True)
    vchconsulnumerointerior = models.CharField(max_length=100, blank=True, null=True)
    intemitirbloqueo = models.IntegerField()
    vchpasswordweb = models.CharField(max_length=150, blank=True, null=True)
    bitpaquetes = models.IntegerField()
    intcvetipopaciente = models.IntegerField(blank=True, null=True)
    bitcorreohonoraios = models.FloatField(blank=True, null=True)
    vchcurp = models.CharField(max_length=20, blank=True, null=True)
    incvebanco = models.FloatField(blank=True, null=True)
    vchclabe = models.CharField(max_length=20, blank=True, null=True)
    intcveretencion = models.IntegerField(blank=True, null=True)
    intmedicocreden = models.IntegerField()
    blbimagenfirma = models.TextField(blank=True, null=True)
    vchuniversidad = models.CharField(max_length=250, blank=True, null=True)
    dtmfechaprivilegio = models.DateTimeField(blank=True, null=True)
    vchobservabloqueo = models.CharField(max_length=250, blank=True, null=True)
    dtminicioproceso = models.DateTimeField(blank=True, null=True)
    dtmfechacertifica = models.DateTimeField(blank=True, null=True)
    bitrtp = models.FloatField()
    vchsucursal = models.CharField(max_length=4, blank=True, null=True)
    vchregimenfiscal = models.CharField(max_length=3, blank=True, null=True)
    trial572 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'homedico'


class PacientesRegpaciente(models.Model):
    id = models.BigAutoField(primary_key=True)
    expediente = models.IntegerField(db_column='Expediente', blank=True, null=True)  # Field name made lowercase.
    numerocuenta = models.IntegerField(db_column='NumeroCuenta', blank=True, null=True)  # Field name made lowercase.
    nombrepaciente = models.CharField(db_column='NombrePaciente', max_length=150, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    fechanacimiento = models.CharField(db_column='FechaNacimiento', max_length=100, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    fechaingreso = models.DateField(db_column='FechaIngreso', blank=True, null=True)  # Field name made lowercase.
    horaingreso = models.TimeField(db_column='HoraIngreso', blank=True, null=True)  # Field name made lowercase.
    fechaegreso = models.DateField(db_column='FechaEgreso', blank=True, null=True)  # Field name made lowercase.
    horaegreso = models.TimeField(db_column='HoraEgreso', blank=True, null=True)  # Field name made lowercase.
    sexo = models.CharField(max_length=50, db_collation='utf8mb3_general_ci', blank=True, null=True)
    diasestancia = models.IntegerField(db_column='DiasEstancia', blank=True, null=True)  # Field name made lowercase.
    lugaregreso = models.CharField(db_column='LugarEgreso', max_length=150, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    tipoatencion = models.CharField(db_column='TipoAtencion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tipopaciente = models.CharField(db_column='TipoPaciente', max_length=100, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    tipoingreso = models.CharField(db_column='TipoIngreso', max_length=100, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    empresa = models.CharField(db_column='Empresa', max_length=100, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    servicioprestado = models.CharField(db_column='ServicioPrestado', max_length=100, blank=True, null=True)  # Field name made lowercase.
    paquete = models.CharField(db_column='Paquete', max_length=100, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    cuarto = models.CharField(db_column='Cuarto', max_length=100, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    cirugia = models.CharField(db_column='Cirugia', max_length=100, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    salacx = models.CharField(db_column='SalaCX', max_length=100, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    medicotratante = models.CharField(db_column='MedicoTratante', max_length=150, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    especialidad = models.CharField(db_column='Especialidad', max_length=150, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    medinterconsultante = models.CharField(db_column='MedInterconsultante', max_length=150, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    medicoanestesiologo = models.CharField(db_column='MedicoAnestesiologo', max_length=150, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    tipoanestesia = models.CharField(db_column='TipoAnestesia', max_length=150, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    diagnostico = models.CharField(db_column='Diagnostico', max_length=150, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    cie10 = models.CharField(db_column='Cie10', max_length=10, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    diagnosticocie10 = models.CharField(db_column='DiagnosticoCIE10', max_length=250, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    recoi = models.CharField(db_column='Recoi', max_length=200, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    diagnosticorecoi = models.CharField(db_column='DiagnosticoRecoi', max_length=250, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    procedimiento = models.CharField(db_column='Procedimiento', max_length=150, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    fechacirugia = models.CharField(db_column='FechaCirugia', max_length=50, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    egresourgencias = models.CharField(db_column='EgresoUrgencias', max_length=50, blank=True, null=True)  # Field name made lowercase.
    nacidovivo = models.CharField(db_column='NacidoVivo', max_length=10, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    pesorn = models.CharField(db_column='PesoRN', max_length=30, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    tallarn = models.CharField(db_column='TallaRN', max_length=30, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    mamarn = models.CharField(db_column='MamaRN', max_length=30, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    salpingopuerperio = models.CharField(db_column='SalpingoPuerperio', max_length=30, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    motivoegreso = models.CharField(db_column='MotivoEgreso', max_length=60, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    egresocensable = models.CharField(db_column='EgresoCensable', max_length=5, blank=True, null=True)  # Field name made lowercase.
    reingreso = models.CharField(db_column='Reingreso', max_length=50, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    motivoreingreso = models.CharField(db_column='MotivoReingreso', max_length=50, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    certificado = models.CharField(db_column='Certificado', max_length=50, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    numerocertificado = models.CharField(db_column='NumeroCertificado', max_length=250, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    observaciones = models.CharField(db_column='Observaciones', max_length=250, db_collation='utf8mb3_general_ci', blank=True, null=True)  # Field name made lowercase.
    estatus = models.CharField(max_length=20, db_collation='utf8mb3_general_ci', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pacientes_regpaciente'


class PacientesUsuario(models.Model):
    id = models.BigAutoField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()
    rol = models.CharField(max_length=50)
    imagen = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pacientes_usuario'


class PacientesUsuarioGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    usuario = models.ForeignKey(PacientesUsuario, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pacientes_usuario_groups'
        unique_together = (('usuario', 'group'),)


class PacientesUsuarioUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    usuario = models.ForeignKey(PacientesUsuario, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pacientes_usuario_user_permissions'
        unique_together = (('usuario', 'permission'),)


class Pvpaquete(models.Model):
    intnumpaquete = models.IntegerField(primary_key=True)
    chrdescripcion = models.CharField(max_length=100, blank=True, null=True)
    smiconceptofactura = models.IntegerField()
    chrtratamiento = models.CharField(max_length=12)
    chrtipo = models.CharField(max_length=10)
    mnyanticiposugerido = models.FloatField()
    bitactivo = models.IntegerField(blank=True, null=True)
    bitincrementoautomatico = models.IntegerField(blank=True, null=True)
    dtmfechaactualizacion = models.DateTimeField(blank=True, null=True)
    bitcostobase = models.IntegerField()
    chrtipoingresodescuento = models.CharField(max_length=1)
    bitvalidacargospaquete = models.IntegerField()
    bitseleccionarhonorarios = models.FloatField(blank=True, null=True)
    intorigen = models.FloatField(blank=True, null=True)
    dtmfechaaltapaquete = models.DateTimeField(blank=True, null=True)
    trial575 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pvpaquete'


class Sitipoingreso(models.Model):
    intcvetipoingreso = models.IntegerField(primary_key=True)
    vchnombre = models.CharField(max_length=100, blank=True, null=True)
    chrtipoingreso = models.CharField(max_length=1, blank=True, null=True)
    intactivo = models.IntegerField(blank=True, null=True)
    trial575 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sitipoingreso'


