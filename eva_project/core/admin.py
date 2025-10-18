from django.contrib import admin
from .models import Paciente, Medicamento, Prescripcion

admin.site.register(Paciente)
admin.site.register(Medicamento)
admin.site.register(Prescripcion)