from django.shortcuts import render, redirect, get_object_or_404
from .models import Medicamento, Prescripcion
from .forms import PacienteForm, MedicamentoForm, PrescripcionForm

def lista_pacientes(request):
    return render(request, 'pacientes/lista.html', {'pacientes'})

def crear_paciente(request):
    form = PacienteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_pacientes')
    return render(request, 'pacientes/formulario.html', {'form': form})

def editar_paciente(request, id):
    paciente = get_object_or_404(id=id)
    form = PacienteForm(request.POST or None, instance=paciente)
    if form.is_valid():
        form.save()
        return redirect('lista_pacientes')
    return render(request, 'pacientes/formulario.html', {'form': form})

def eliminar_paciente(request, id):
    paciente = get_object_or_404(id=id)
    paciente.delete()
    return redirect('lista_pacientes')

def lista_medicamentos(request):
    medicamentos = Medicamento.objects.all()
    return render(request, 'medicamentos/lista.html', {'medicamentos': medicamentos})

def crear_medicamento(request):
    form = MedicamentoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_medicamentos')
    return render(request, 'medicamentos/formulario.html', {'form': form})

def editar_medicamento(request, id):
    medicamento = get_object_or_404(Medicamento, id=id)
    form = MedicamentoForm(request.POST or None, instance=medicamento)
    if form.is_valid():
        form.save()
        return redirect('lista_medicamentos')
    return render(request, 'medicamentos/formulario.html', {'form': form})

def eliminar_medicamento(request, id):
    medicamento = get_object_or_404(Medicamento, id=id)
    medicamento.delete()
    return redirect('lista_medicamentos')

def lista_prescripciones(request):
    prescripciones = Prescripcion.objects.all()
    return render(request, 'prescripciones/lista.html', {'prescripciones': prescripciones})

def crear_prescripcion(request):
    form = PrescripcionForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_prescripciones')
    return render(request, 'prescripciones/formulario.html', {'form': form})

def editar_prescripcion(request, id):
    prescripcion = get_object_or_404(Prescripcion, id=id)
    form = PrescripcionForm(request.POST or None, instance=prescripcion)
    if form.is_valid():
        form.save()
        return redirect('lista_prescripciones')
    return render(request, 'prescripciones/formulario.html', {'form': form})

def eliminar_prescripcion(request, id):
    prescripcion = get_object_or_404(Prescripcion, id=id)
    prescripcion.delete()
    return redirect('lista_prescripciones')
