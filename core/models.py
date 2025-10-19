from django.db import models

class Medicamento(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    stock = models.IntegerField(default=0)
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    dosis_recomendada = models.DecimalField(max_digits=5, decimal_places=2, default=0)  # obligatorio con default

    def __str__(self):
        return self.nombre

class Prescripcion(models.Model):
    paciente = models.CharField(max_length=100)
    medicamento = models.CharField(max_length=100)
    dosis = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    frecuencia = models.CharField(max_length=50, default="1 vez al dia")
    duracion = models.CharField(max_length=50, default="7 dias")

    def __str__(self):
        return f"{self.paciente} - {self.medicamento}"
