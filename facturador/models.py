from django.db import models
from django.utils import timezone

# Create your models here.
class CFDI(models.Model):
  version = models.CharField(max_length=5)
  serie = models.CharField(max_length=1)
  asignarFolio = models.CharField(max_length=25)
  fecha = models.DateTimeField(default=timezone.now)
  formaPago = models.CharField(max_length=5)
  noCertificado = models.CharField(max_length=100)
  condicionesDePago = models.CharField(max_length=100)
  subtotal =models.CharField(max_length=100)
  descuento = models.CharField(max_length=100)
  moneda = models.CharField(max_length=10)
  tipoCambio = models.CharField(max_length=100)
  total = models.CharField(max_length=100)
  tipoComprobante = models.CharField(max_length=5)
  metodoPago = models.CharField(max_length=50)
  lugarExpedicion = models.CharField(max_length=50)
  tipoDocumento = models.CharField(max_length=50)
  #Datos del Emisor
  rfcEmisor = models.CharField(max_length=50)
  nombreEmisor = models.CharField(max_length=200)
  regimenFiscalEmisor = models.CharField(max_length=100)
  #Datos del Receptor
  rfcReceptor = models.CharField(max_length=50)
  nombre = models.CharField(max_length=200)
  usoCFDI = models.CharField(max_length=100)
  #Concepto
  claveProdServ = models.CharField(max_length=20)
  noIdentificacion = models.CharField(max_length=50)
  cantidad = models.CharField(max_length=50)
  claveUnidad = models.CharField(max_length=50)
  unidadKilogramos = models.CharField(max_length=50)
  descripcion = models.CharField(max_length=50)
  valorUnitario = models.CharField(max_length=50)
  importe = models.CharField(max_length=20)
  descuento = models.CharField(max_length=50)
