from django.db import models

# Create your models here.


class persona(models.Model):
    id_persona=models.BigIntegerField(primary_key=True,db_column='id_persona',db_index='id_pesona')
    nombre=models.TextField(db_column='nombre',blank=False,null=False)
    apellido=models.TextField(db_column='apellido',blank=False,null=False)
    direccion=models.TextField(db_column='direccion',blank=False,null=False)
    telefono=models.CharField(db_column='telefono',blank=False,null=False,max_length=10)
    fecc_nac=models.DateField(db_column='fecha_nac')
    class Meta:
        managed = False
        db_table = 'persona'

class estudiantes (models.Model):
    id_estudiante=models.BigIntegerField(primary_key=True,db_column='id_estudiante')
    id_persona=models.ForeignKey(persona,on_delete=models.PROTECT,db_column='id_persona')
    activo= models.BooleanField(db_column='activo',null=False,blank=False)
    grado=models.IntegerField(db_column='grado_esc',max_length=3,null=False,blank=False)
    class Meta:
        managed = False
        db_table = 'estudiante'

class grado(models.Model):
    id_grado= models.BigIntegerField(primary_key=True,db_column='id_grado')
    nombre=models.CharField(db_column='nombre',max_length=10)
    jornada=models.CharField(db_column='jornada',max_length=10)
    salon=models.CharField(db_column='salon',max_length=10)
    class Meta:
        managed = False
        db_table = 'grado'

class docentes(models.Model):
    id_docentes=models.BigIntegerField(primary_key=True,)
