from django.db import models

# Create your models here.

class Modelo_1(models.Model):
    # Campo de tipo AUTO INCREMENTAL, usado para ID's
    campo_1_modelo_1 = models.AutoField(primary_key=True)

    # CharField para textos cortos y medianos, requiere indicar el largo máximo del campo
    campo_2_modelo_1 = models.CharField(max_length=200, null=False)

    # TextField para textos largos
    campo_3_modelo_1 = models.TextField(default="Texto")


class Modelo_2(models.Model):
    # Campo de tipo AUTO INCREMENTAL
    campo_1_modelo_2 = models.AutoField(primary_key=True)

    # Campo de tipo RELACIÓN: cada objeto de Modelo_2 está relacionado con un objeto de Modelo_1
    campo_2_modelo_2 = models.ForeignKey(Modelo_1, on_delete=models.CASCADE)

    # Campo tipo FECHA
    campo_3_modelo_2 = models.DateField()

    # Campo tipo HORA
    campo_4_modelo_2 = models.TimeField()

    # Campo tipo FECHA con HORA
    campo_5_modelo_2 = models.DateTimeField()

    # Campo tipo ENTERO
    campo_6_modelo_2 = models.IntegerField()

    # Campo tipo DECIMAL: se debe indicar la cantidad máxima de dígitos y cantidad de decimales
    campo_7_modelo_2 = models.DecimalField(max_digits=10, decimal_places=2)

    # Campo tipo FLOTANTE
    campo_8_modelo_2 = models.FloatField()

    # Campo tipo BOOLEANO
    campo_9_modelo_2 = models.BooleanField()

    # Campo tipo CORREO
    campo_10_modelo_2 = models.EmailField()

    # Campo tipo URL
    campo_11_modelo_2 = models.URLField()

    # Campo tipo ARCHIVO
    campo_12_modelo_2 = models.FileField(upload_to="archivos/")

    # Campo tipo IMAGEN
    campo_13_modelo_2 = models.ImageField(upload_to="imagenes/")

class Comuna(models.Model):
    codigo = models.CharField(max_length=5, null=False)
    nombre_comuna = models.CharField(max_length=50, null=False)
    created_at= models.DateTimeField(auto_now_add=True) #si es comuna se actuliza con fecha de creacion
    update_at = models.DateTimeField(auto_now=True) #si se actualiza se crea actualizacion con fecha

class Nacionalidad (models.Model):
    pais = models.CharField(max_length=255, null=False)
    nacionalidad = models.CharField(max_length= 255, null=False)
    created_at= models.DateTimeField(auto_now_add=True) #si se comuna se actuliza con fecha de creacion
    update_at = models.DateTimeField(auto_now=True) #si se actualiza se crea actualizacion con fecha

class Direccion(models.Model):
    id_comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE, null=False) #selecciona foranea, CASCADE  es para no romper la integredidad de datos si se borra un dato de la clase llamada (relaciones si se borra un dato de otra clase)
    calle = models.CharField(max_length=100, null=False)
    numero = models.CharField(max_length=10, null=True)
    departamento = models.CharField (max_length=10, null=True)
    created_at= models.DateTimeField(auto_now_add=True) #si se comuna se actuliza con fecha de creacion
    update_at = models.DateTimeField(auto_now=True) #si se actualiza se crea actualizacion con fecha

class Autor(models.Model):
    nombre_autor = models.CharField(max_length=255, null=False)
    pseudonimo = models.CharField(max_length=50)
    id_nacionalidad = models.ForeignKey (Nacionalidad, on_delete=models.CASCADE,null=True)
    bio = models.TextField(null=True)
    created_at= models.DateTimeField(auto_now_add=True) #si se comuna se actuliza con fecha de creacion
    update_at = models.DateTimeField(auto_now=True) #si se actualiza se crea actualizacion con fecha

class Biblioteca(models.Model):
    nombre_biblioteca = models.CharField(max_length=100,null=False)
    id_direccion=models.ForeignKey(Direccion,on_delete=models.CASCADE,null=True)
    web = models.URLField(null=True)
    created_at= models.DateTimeField(auto_now_add=True) #si se comuna se actuliza con fecha de creacion
    update_at = models.DateTimeField(auto_now=True) #si se actualiza se crea actualizacion con fecha

class Categoria(models.Model):
    categoria = models.CharField(max_length=50, null=True)
    descripcion = models.TextField(null=True)
    created_at= models.DateTimeField(auto_now_add=True) #si se comuna se actuliza con fecha de creacion
    update_at = models.DateTimeField(auto_now=True) #si se actualiza se crea actualizacion con fecha

class Libro(models.Model):
    titulo = models.CharField(max_length=255,null=False)
    id_autor = models.ForeignKey(Autor,on_delete=models.CASCADE, null=False)
    paginas = models.IntegerField()
    copias = models.IntegerField()
    id_biblioteca = models.ForeignKey(Biblioteca, on_delete=models.CASCADE, null=False)
    id_categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE, null=True)
    created_at= models.DateTimeField(auto_now_add=True) #si se comuna se actuliza con fecha de creacion
    update_at = models.DateTimeField(auto_now=True) #si se actualiza se crea actualizacion con fecha

class Lector(models.Model):
    rut = models.IntegerField(null=False)
    digito_verificador = models.CharField(max_length=1,null=False)
    id_direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE, null=True)
    id_biblioteca = models.ForeignKey(Biblioteca, on_delete=models.CASCADE, null=False)
    habilitado = models.BooleanField(default=True)
    created_at= models.DateTimeField(auto_now_add=True) #si se comuna se actuliza con fecha de creacion
    update_at = models.DateTimeField(auto_now=True) #si se actualiza se crea actualizacion con fecha

class Prestamo(models.Model):
    id_libro = models.ForeignKey(Libro, on_delete=models.CASCADE, null=False)
    id_lector = models.ForeignKey(Lector, on_delete=models.CASCADE, null=False)
    fecha_prestamo = models.DateTimeField(auto_now=True)
    fecha_devolucion = models.DateField(null=False)
    fecha_entrega = models.DateTimeField(auto_now=True)