from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('profesores/', views.agregar_profesor, name='agregar_profesor'),
    path('cursos/', views.agregar_curso, name='agregar_curso'),
    path('estudiante/', views.agregar_estudiante, name='agregar_estudiante'),
    path('entregable/', views.agregar_entregable, name='agregar_entregable'),
   path('buscar/', views.buscar_curso, name='buscar_curso'),
    ]