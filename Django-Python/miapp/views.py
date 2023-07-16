from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from . import forms

import sqlite3

# Create your views here.


def index(request):
    return HttpResponse("Bienvenidos al curso de Django")

def acerca(request):
    return HttpResponse("<html><h1>Acerca de mi pagina</h1></html>")


def cursos(request):
    
    conn = sqlite3.connect("cursos.db")
    cursor = conn.cursor()
    cursor.execute("SELECT nombre, inscriptos FROM cursos")
    
    html = """
    <html>
    <title>Lista de cursos</title>
    <table style="border: 1px solid">
    <thead>
    <tr>
    <th>Curso</th>
    <th>Inscriptos</th>
    </tr>
    </thead>
    """
    
    for (nombre, inscriptos) in cursor.fetchall():
        html += f"""
        <tr>
        <td>{nombre}</td>
        <td>{inscriptos}</td>
        </tr>
        """
    
    html += "</table></html>"
    
    conn.close()
    
    return HttpResponse(html)


def cursos_json(request):
    conn = sqlite3.connect( "cursos.db" )
    cursor = conn.cursor()
    cursor.execute( "SELECT nombre, inscriptos FROM cursos" )
    response = JsonResponse(cursor.fetchall(), safe = False )
    conn.close()
    return response

# def aeropuertos(request):
#     f = open("aeropuertos.csv", encoding="utf8")
#     html = """
#         <html>
#         <title>Lista de aeropuertos</title>
#         <table style="border: 1px solid">
#           <thead>
#             <tr>
#               <th>Aeropuerto</th>
#               <th>Ciudad</th>
#               <th>País</th>
#             </tr>
#           </thead>
#     """
#     for linea in f:
#         datos = linea.split(",")
#         nombre = datos[1].replace('"', "")
#         ciudad = datos[2].replace('"', "")
#         pais = datos[3].replace('"', "")
#         html += f"""
#             <tr>
#               <td>{nombre}</td>
#               <td>{ciudad}</td>
#               <td>{pais}</td>
#             </tr>
#         """
#     f.close()
#     html += "</table></html>"
#     return HttpResponse(html)

# def aeropuertos_json(request):
#     f = open("aeropuertos.csv", encoding="utf8")
#     aeropuertos = []
#     for linea in f:
#         datos = linea.split(",")
#         aeropuerto = {
#             "nombre": datos[1].replace('"', ""),
#             "ciudad": datos[2].replace('"', ""),
#             "pais": datos[3].replace('"', "")
#         } 
#         aeropuertos.append(aeropuerto)
#     f.close()
#     return JsonResponse(aeropuertos, safe=False)

def aeropuertos(request):
    html = """
        <html>
        <title>Lista de aeropuertos</title>
        <table style="border: 1px solid">
          <thead>
            <tr>
              <th>Aeropuerto</th>
              <th>Ciudad</th>
              <th>País</th>
            </tr>
          </thead>
    """
    with open("aeropuertos.csv", encoding="utf8") as file:
        for linea in file:
            datos = linea.split(",")
            nombre = datos[1].replace('"','')
            ciudad = datos[2].replace('"','')
            pais = datos[3].replace('"','')
            html += f"""
                <tr>
                    <td>{nombre}</td>
                    <td>{ciudad}</td>
                    <td>{pais}</td>
                </tr>
            """
    html += "</table></html>"
    return HttpResponse(html)



def aeropuertos_json(request):
    aeropuertos = []
    with open("aeropuertos.csv", encoding="utf8") as file:
        for linea in file:
            datos = linea.split(",")
            nombre = datos[1].replace('"','')
            ciudad = datos[2].replace('"','')
            pais = datos[3].replace('"','')
            aeropuerto = {
                "nombre": nombre,
                "ciudad": ciudad,
                "pais": pais
            }
            aeropuertos.append(aeropuerto)
    
    return JsonResponse(aeropuertos, safe=False)

def bienvenido(request):
    with open("miapp/templates/miapp/bienvenido.html", encoding="utf-8") as file:
        response = HttpResponse(file.read())
    return response    

def bienvenido2(request):
    ctx = {"nombre": "Juan Perez",
            "dni": 12345678,
            "cursos": ["Java", "Pyton", "c#", "Django"],
            "notas": [9, 7, 3, 10] 
            }
    return render(request, "miapp/bienvenido2.html", ctx)




def cursos2(request):
    conn = sqlite3.connect("cursos.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre, inscriptos FROM cursos")
    
    
    ctx = {"cursos": cursor.fetchall()}
    conn.close()
    return render(request, "miapp/cursos.html", ctx)


def un_curso(request, p_nombreCurso):
    conn = sqlite3.connect("cursos.db")
    cursor = conn.cursor()

    cursor.execute("SELECT id, nombre, inscriptos FROM cursos WHERE nombre=?", [p_nombreCurso])
    curso = cursor.fetchone()
    if curso is None:
        raise Http404
    ctx = {"cursos": curso}
    conn.close()
    return render(request, "miapp/un_curso.html", ctx)


def nuevo_curso(request):
    if request.method == "POST":
        form = forms.FormularioCurso(request.POST)
        if form.is_valid():
            conn = sqlite3.connect("cursos.db")
            cursor = conn.cursor()
            cursor.execute("INSERT INTO cursos (nombre, inscriptos) VALUES (?,?)",
                (
                    form.cleaned_data['nombre'],
                    form.cleaned_data['inscriptos']
                )
            )
            conn.commit()
            conn.close()
            return HttpResponseRedirect(reverse('cursos2'))
    else:
        form = forms.FormularioCurso()

    ctx = {"form": form}
    return render(request, "miapp/nuevo_curso.html", ctx)


def shopapp(request):
    ctx = {"nombre": "Juan Perez",
            "dni": 12345678,
            "cursos": ["Java", "Pyton", "c#", "Django"],
            "notas": [9, 7, 3, 10] 
            }
    return render(request, "miapp/shopapp.html", ctx)