# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Jugador(models.Model):
    id_j = models.AutoField(primary_key=True)
    id_u_creador = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_u_creador', blank=True, null=True)
    nombre_c = models.CharField(max_length=100)
    sexo = models.IntegerField(blank=True, null=True)
    skill = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Jugador'


class JugadorPosicion(models.Model):
    id_j = models.ForeignKey(Jugador, models.DO_NOTHING, db_column='id_j', blank=True, null=True)
    id_pos = models.ForeignKey('Posicion', models.DO_NOTHING, db_column='id_pos', blank=True, null=True)
    id_j_p = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'Jugador_Posicion'


class Posicion(models.Model):
    id_pos = models.AutoField(primary_key=True)
    nombre_pos = models.CharField(max_length=50)
    id_rol_pos = models.ForeignKey('RolPos', models.DO_NOTHING, db_column='id_rol_pos', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Posicion'


class Usuario(models.Model):
    id_u = models.AutoField(primary_key=True)
    nombre_c = models.CharField(max_length=100)
    email = models.CharField(unique=True, max_length=150, blank=True, null=True)
    sexo = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Usuario'


class UsuarioPosicion(models.Model):
    id_u = models.ForeignKey(Usuario, models.DO_NOTHING, db_column='id_u', blank=True, null=True)
    id_pos = models.ForeignKey(Posicion, models.DO_NOTHING, db_column='id_pos', blank=True, null=True)
    id_u_p = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'Usuario_Posicion'


class RolPos(models.Model):
    id_rol_pos = models.AutoField(primary_key=True)
    nombre = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'rol_pos'
