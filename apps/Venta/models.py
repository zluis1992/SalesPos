# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Almacen(models.Model):
    nombre = models.CharField(max_length=45)
    direccion = models.CharField(max_length=45)
    estado = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Almacen'


class Caja(models.Model):
    usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='Usuario_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Caja'


class Categoria(models.Model):
    nombre = models.CharField(max_length=45)
    encatalogo = models.IntegerField(db_column='enCatalogo')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Categoria'

    def __str__(self):
        return self.nombre


class Cierrecaja(models.Model):
    caja = models.ForeignKey(Caja, models.DO_NOTHING, db_column='Caja_id')  # Field name made lowercase.
    fechacierre = models.DateTimeField(db_column='fechaCierre', blank=True, null=True)  # Field name made lowercase.
    dinero = models.FloatField()

    class Meta:
        managed = False
        db_table = 'CierreCaja'


class Cliente(models.Model):
    categoriaespecial = models.CharField(db_column='CategoriaEspecial', max_length=45, blank=True, null=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=45, blank=True, null=True)
    deudamaxima = models.FloatField(db_column='deudaMaxima', blank=True, null=True)  # Field name made lowercase.
    direccion = models.CharField(max_length=45, blank=True, null=True)
    telefono = models.CharField(max_length=45, blank=True, null=True)
    correo = models.CharField(max_length=45, blank=True, null=True)
    notas = models.CharField(max_length=45, blank=True, null=True)
    creado = models.CharField(max_length=45)
    estado = models.IntegerField(blank=True, null=True)
    impuesto = models.ForeignKey('Impuesto', models.DO_NOTHING, db_column='Impuesto_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Cliente'


class Detallerecibo(models.Model):
    recibo = models.ForeignKey('Recibo', models.DO_NOTHING, db_column='Recibo_id')  # Field name made lowercase.
    producto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='Producto_id')  # Field name made lowercase.
    cantidad = models.FloatField()
    precio = models.FloatField()

    class Meta:
        managed = False
        db_table = 'DetalleRecibo'


class Existencia(models.Model):
    producto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='Producto_id')  # Field name made lowercase.
    localalmacen = models.ForeignKey('Localalmacen', models.DO_NOTHING, db_column='LocalAlmacen_id')  # Field name made lowercase.
    minima = models.IntegerField(blank=True, null=True)
    maxima = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Existencia'


class Impuesto(models.Model):
    nombre = models.CharField(max_length=45)
    validopara = models.CharField(db_column='validoPara', max_length=45)  # Field name made lowercase.
    valor = models.FloatField()

    class Meta:
        managed = False
        db_table = 'Impuesto'

    def __str__(self):
        return self.nombre


class Inventario(models.Model):
    producto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='Producto_id')  # Field name made lowercase.
    atributo = models.CharField(max_length=45, blank=True, null=True)
    cantidad = models.FloatField()
    precio = models.CharField(max_length=45, blank=True, null=True)
    razon = models.CharField(max_length=45)
    localalmacen = models.ForeignKey('Localalmacen', models.DO_NOTHING, db_column='LocalAlmacen_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Inventario'


class Local(models.Model):
    nombre = models.CharField(max_length=45)
    direccion = models.CharField(max_length=45, blank=True, null=True)
    estado = models.IntegerField()
    telefono = models.CharField(max_length=45, blank=True, null=True)
    nit = models.CharField(db_column='NIT', unique=True, max_length=45)  # Field name made lowercase.
    slogan = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Local'

    def __str__(self):
        return self.nombre


class Localalmacen(models.Model):
    local = models.ForeignKey(Local, models.DO_NOTHING, db_column='Local_id')  # Field name made lowercase.
    almacen = models.ForeignKey(Almacen, models.DO_NOTHING, db_column='Almacen_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LocalAlmacen'


class Movimiento(models.Model):
    producto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='Producto_id')  # Field name made lowercase.
    atributo = models.CharField(max_length=45, blank=True, null=True)
    unidades = models.CharField(max_length=45, blank=True, null=True)
    precio = models.CharField(max_length=45, blank=True, null=True)
    razon = models.IntegerField()
    fecha = models.CharField(max_length=45)
    observacion = models.CharField(max_length=45, blank=True, null=True)
    usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='Usuario_id')  # Field name made lowercase.
    localalmacen = models.ForeignKey(Localalmacen, models.DO_NOTHING, db_column='LocalAlmacen_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Movimiento'


class Producto(models.Model):
    categoria = models.ForeignKey(Categoria, models.DO_NOTHING, db_column='Categoria_id')  # Field name made lowercase.
    codigobarras = models.CharField(db_column='codigoBarras', max_length=45)  # Field name made lowercase.
    nombre = models.CharField(max_length=45)
    preciocompra = models.FloatField(db_column='precioCompra')  # Field name made lowercase.
    precioventa = models.FloatField(db_column='precioVenta')  # Field name made lowercase.
    imagen = models.CharField(max_length=45, blank=True, null=True)
    impuesto = models.ForeignKey(Impuesto, models.DO_NOTHING, db_column='Impuesto_id')  # Field name made lowercase.
    estado = models.IntegerField()
    unidadprincipal = models.ForeignKey('Unidad', models.DO_NOTHING, related_name='unidadprincipal', blank=True, null=True)
    unidadfraccion = models.ForeignKey('Unidad', models.DO_NOTHING, related_name='unidadfraccion', blank=True, null=True)
    cantidadfraccion = models.IntegerField(blank=True, null=True)
    fraccionminimaventa = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Producto'

    def __str__(self):
        return self.nombre


class ProductoAtributo(models.Model):
    producto = models.ForeignKey(Producto, models.DO_NOTHING, db_column='Producto_id')  # Field name made lowercase.
    atributos = models.ForeignKey('Atributos', models.DO_NOTHING)
    valoratributo = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Producto_Atributo'


class Recibo(models.Model):
    caja = models.ForeignKey(Caja, models.DO_NOTHING, db_column='Caja_id')  # Field name made lowercase.
    cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='Cliente_id')  # Field name made lowercase.
    local = models.ForeignKey(Local, models.DO_NOTHING, db_column='Local_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Recibo'


class Rol(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Rol'


class Unidad(models.Model):
    nombre = models.CharField(max_length=45)
    simbolo = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'Unidad'

    def __str__(self):
        return self.nombre


class Usuario(models.Model):
    rol = models.ForeignKey(Rol, models.DO_NOTHING, db_column='Rol_Id')  # Field name made lowercase.
    nombre = models.CharField(max_length=45, blank=True, null=True)
    usuario = models.CharField(max_length=45, blank=True, null=True)
    password = models.CharField(max_length=45, blank=True, null=True)
    imagen = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Usuario'


class Atributos(models.Model):
    nombre = models.CharField(max_length=45)
    aceptado = models.IntegerField()
    notas = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'atributos'

    def __str__(self):
        return self.nombre