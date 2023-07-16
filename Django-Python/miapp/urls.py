

from django.urls import path, include
from . import views

urlpatterns = [
    
    path('', views.index, name="index"),
    path('acerca/', views.acerca, name="acerca"),
    path('cursos/', views.cursos , name="cursos"),
    path( "cursos/json/" , views.cursos_json, name = "cursos_json" ),
    path("aeropuertos", views.aeropuertos, name="aeropuertos"),
    path("aeropuertos/json", views.aeropuertos_json, name="aeropuertos_json"),
    path('bienvenido/', views.bienvenido , name="bienvenido"),
    path('bienvenido2/', views.bienvenido2 , name="bienvenido2"),
    path('cursos2/', views.cursos2 , name="cursos2"),
    path('un_curso/<p_nombreCurso>', views.un_curso , name="un_curso"),
    path('nuevo_curso/', views.nuevo_curso, name="nuevo_curso"),
    path('shopapp/', views.shopapp, name="shopapp"),

]
