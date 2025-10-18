from django.shortcuts import render, redirect, get_object_or_404
from .models import Paciente, Medicamento, Prescripcion
from django.urls import reverse

def lista_pacientes(request):
    pacientes = Paciente.objects.all()
    return render(request, 'pacientes/lista.html', {'pacientes': pacientes})

def crear_paciente(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        rut = request.POST['rut']
        fecha_nacimiento = request.POST['fecha_nacimiento']
        direccion = request.POST['direccion']
        Paciente.objects.create(nombre=nombre, rut=rut, fecha_nacimiento=fecha_nacimiento, direccion=direccion)
        return redirect('lista_pacientes')
    return render(request, 'pacientes/formulario.html')

def editar_paciente(request, id):
    paciente = get_object_or_404(Paciente, id=id)
    if request.method == 'POST':
        paciente.nombre = request.POST['nombre']
        paciente.rut = request.POST['rut']
        paciente.fecha_nacimiento = request.POST['fecha_nacimiento']
        paciente.direccion = request.POST['direccion']
        paciente.save()
        return redirect('lista_pacientes')
    return render(request, 'pacientes/formulario.html', {'paciente': paciente})

def eliminar_paciente(request, id):
    paciente = get_object_or_404(Paciente, id=id)
    paciente.delete()
    return redirect('lista_pacientes')


def lista_medicamentos(request):
    medicamentos = Medicamento.objects.all()
    return render(request, 'medicamentos/lista.html', {'medicamentos': medicamentos})

def crear_medicamento(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']
        laboratorio = request.POST['laboratorio']
        Medicamento.objects.create(nombre=nombre, descripcion=descripcion, laboratorio=laboratorio)
        return redirect('lista_medicamentos')
    return render(request, 'medicamentos/formulario.html')

def editar_medicamento(request, id):
    medicamento = get_object_or_404(Medicamento, id=id)
    if request.method == 'POST':
        medicamento.nombre = request.POST['nombre']
        medicamento.descripcion = request.POST['descripcion']
        medicamento.laboratorio = request.POST['laboratorio']
        medicamento.save()
        return redirect('lista_medicamentos')
    return render(request, 'medicamentos/formulario.html', {'medicamento': medicamento})

def eliminar_medicamento(request, id):
    medicamento = get_object_or_404(Medicamento, id=id)
    medicamento.delete()
    return redirect('lista_medicamentos')

def lista_prescripciones(request):
    prescripciones = Prescripcion.objects.all()
    return render(request, 'prescripciones/lista.html', {'prescripciones': prescripciones})

def crear_prescripcion(request):
    pacientes = Paciente.objects.all()
    medicamentos = Medicamento.objects.all()
    if request.method == 'POST':
        paciente_id = request.POST['paciente']
        medicamento_id = request.POST['medicamento']
        dosis = request.POST['dosis']
        fecha_inicio = request.POST['fecha_inicio']
        fecha_fin = request.POST['fecha_fin']
        Prescripcion.objects.create(
            paciente_id=paciente_id,
            medicamento_id=medicamento_id,
            dosis=dosis,
            fecha_inicio=fecha_inicio,
            fecha_fin=fecha_fin
        )
        return redirect('lista_prescripciones')
    return render(request, 'prescripciones/formulario.html', {'pacientes': pacientes, 'medicamentos': medicamentos})

def eliminar_prescripcion(request, id):
    prescripcion = get_object_or_404(Prescripcion, id=id)
    prescripcion.delete()
    return redirect('lista_prescripciones')