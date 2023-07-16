from django import forms 

class FormularioCurso(forms.Form):
    nombre = forms.CharField(label="Nombre del Curso", max_length=50)
    inscriptos = forms.IntegerField(label="Inscriptos")
    solo_empresas = forms.BooleanField(label="Es solo para empresas?", required=False)
    TURNOS = (
        (1, "Mañana"),
        (2, "Tarde"),
        (3, "Noche"),
    )
    turno = forms.ChoiceField(label="Turno", choices=TURNOS)
    fecha_inicio = forms.DateField(label="Fecha Inicio")
