from django.urls import path
from . import views

urlpatterns = [
    path('pacientes/', views.lista_pacientes, name='lista_pacientes'),
    path('pacientes/nuevo/', views.crear_paciente, name='crear_paciente'),
    path('pacientes/editar/<int:id>/', views.editar_paciente, name='editar_paciente'),
    path('pacientes/eliminar/<int:id>/', views.eliminar_paciente, name='eliminar_paciente'),

    path('medicamentos/', views.lista_medicamentos, name='lista_medicamentos'),
    path('medicamentos/nuevo/', views.crear_medicamento, name='crear_medicamento'),
    path('medicamentos/editar/<int:id>/', views.editar_medicamento, name='editar_medicamento'),
    path('medicamentos/eliminar/<int:id>/', views.eliminar_medicamento, name='eliminar_medicamento'),

    path('prescripciones/', views.lista_prescripciones, name='lista_prescripciones'),
    path('prescripciones/nuevo/', views.crear_prescripcion, name='crear_prescripcion'),
    path('prescripciones/eliminar/<int:id>/', views.eliminar_prescripcion, name='eliminar_prescripcion'),
]
