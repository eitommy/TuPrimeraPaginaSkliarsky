from django.shortcuts import render, redirect
from django import forms
from .models import Profesor, Curso, Estudiante, Entregable  
from .forms import ProfesorForm, CursoForm, EstudianteForm, EntregableForm

def inicio(request):
    return render(request, "inicio.html")

def agregar_profesor(request):
    if request.method == "POST":
        form = ProfesorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = ProfesorForm()
    return render(request, "profesores.html", {"form": form})

def agregar_curso(request):
    if request.method == "POST":
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = CursoForm()
    return render(request, "cursos.html", {"form": form})

def agregar_estudiante(request):
    if request.method == "POST":
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')  
    else:
        form = EstudianteForm()
    return render(request, "estudiantes.html", {"form": form})
class EntregableForm(forms.ModelForm):
    class Meta:
        model = Entregable
        fields = ['nombre', 'fecha_de_entrega', 'entregado']
def agregar_entregable(request):
    if request.method == "POST":
        form = EntregableForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = EntregableForm()
    return render(request, "entregables.html", {"form": form})


def buscar_curso(request):
    cursos = None
    if "nombre" in request.GET:
        nombre = request.GET["nombre"]
        cursos = Curso.objects.filter(nombre__icontains=nombre)
    return render(request, "buscar.html", {"cursos": cursos})
