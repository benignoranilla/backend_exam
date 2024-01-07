from django.db import models

class Marca(models.Model):
    idMarca = models.IntegerField()
    NombreMarca = models.CharField(max_length =30)

class Modelo(models.Model):
    idModelo = models.IntegerField()
    NombreModelo = models.CharField(max_length =30)
    
class Color(models.Model):
    idColor = models.IntegerField()
    NombreColor = models.CharField(max_length =30)

class Talla(models.Model):
    idTalla = models.IntegerField()
    NombreTalla = models.CharField(max_length =30)

class Producto(models.Model):
    idProducto = models.IntegerField()
    NombreProducto = models.CharField(max_length =30)
    idMarca = models.ForeignKey(Marca, null=True, on_delete=models.SET_NULL)
    idModelo = models.ForeignKey(Modelo, null=True, on_delete=models.SET_NULL)
    idColor = models.ForeignKey(Color, null=True, on_delete=models.SET_NULL)
    idTalla = models.ForeignKey(Talla, null=True, on_delete=models.SET_NULL)
    Imagen = models.ImageField(upload_to='producto')
    PrecioVenta = models.DecimalField(max_digits=12, decimal_places=2)