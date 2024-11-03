# productos/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("consulta/", views.listar_productos, name="consulta_productos"),
    path("registro/", views.crear_producto, name="registro_producto"),
    path("resultado/", views.resultado_producto, name="resultado_producto"),  # Para mostrar confirmación
]

