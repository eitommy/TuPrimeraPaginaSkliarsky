from django import forms
from .models import Profesor, Curso, Estudiante, Entregable

class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = '__all__'

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['nombre', 'apellido', 'email']  

class EntregableForm(forms.ModelForm):
    class Meta:
        model = Entregable
        fields = ['nombre', 'fecha_de_entrega']  # Incluye el campo de fecha

        widgets = {
            'fecha_de_entrega': forms.DateInput(attrs={
                'type': 'date',  
                
            }),
        }
