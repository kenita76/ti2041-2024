from django.shortcuts import render

# Create your views here.
# productos/views.py
from django.shortcuts import render, redirect
from django.contrib import messages  # Para mostrar mensajes de validación

# Lista en memoria para almacenar los productos temporalmente
productos = []

def listar_productos(request):
    """
    Vista para listar todos los productos almacenados en memoria.
    """
    return render(request, "productos/consulta.html", {"productos": productos})

def crear_producto(request):
    """
    Vista para crear un nuevo producto.
    Procesa el formulario y valida los datos ingresados.
    """
    if request.method == "POST":
        # Recoge los datos del formulario
        codigo = request.POST.get("codigo")
        nombre = request.POST.get("nombre")
        marca = request.POST.get("marca")
        fecha_vencimiento = request.POST.get("fecha_vencimiento")

        # Validación simple de los campos
        if not codigo or not nombre or not marca or not fecha_vencimiento:
            messages.error(request, "Todos los campos son obligatorios.")
            return render(request, "productos/registro.html")

        # Crea un diccionario para representar el producto
        producto = {
            "codigo": codigo,
            "nombre": nombre,
            "marca": marca,
            "fecha_vencimiento": fecha_vencimiento,
        }

        # Agrega el producto a la lista de productos
        productos.append(producto)

        # Redirecciona a la página de resultado con un mensaje de éxito
        messages.success(request, "Producto registrado exitosamente.")
        return redirect("resultado_producto")

    # Si el método no es POST, muestra el formulario vacío
    return render(request, "productos/registro.html")

