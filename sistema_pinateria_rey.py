import json
import os
import random
from datetime import datetime

ARCH_PRODUCTOS = "productos_rey.json"
ARCH_VENTAS = "ventas_rey.json"
ARCH_PEDIDOS = "pedidos_rey.json"


def cargar_datos(nombre_archivo):
    """Carga datos desde un archivo JSON. Si no existe, devuelve una lista vacía."""
    if not os.path.exists(nombre_archivo):
        return []

    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        try:
            return json.load(archivo)
        except json.JSONDecodeError:
            return []


def guardar_datos(nombre_archivo, datos):
    """Guarda datos en un archivo JSON."""
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)


def leer_texto(mensaje):
    """Lee texto y evita que el usuario deje el campo vacío."""
    while True:
        dato = input(mensaje).strip()
        if dato:
            return dato
        print("Error: no puede quedar vacío.")


def leer_entero(mensaje, minimo=None):
    """Lee un número entero y valida el valor mínimo."""
    while True:
        try:
            valor = int(input(mensaje))
            if minimo is not None and valor < minimo:
                print(f"Error: debe ser mayor o igual a {minimo}.")
                continue
            return valor
        except ValueError:
            print("Error: ingrese un número entero válido.")


def leer_float(mensaje, minimo=None):
    """Lee un número decimal y valida el valor mínimo."""
    while True:
        try:
            valor = float(input(mensaje))
            if minimo is not None and valor < minimo:
                print(f"Error: debe ser mayor o igual a {minimo}.")
                continue
            return valor
        except ValueError:
            print("Error: ingrese un número válido.")


def fecha_actual():
    """Devuelve la fecha y hora actual."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def inicializar_catalogo(productos):
    """Agrega productos iniciales de la Piñatería REY si el catálogo está vacío."""
    if not productos:
        base = [
            {"codigo": "R001", "nombre": "Piñata mediana", "categoria": "Piñatas", "evento": "Cumpleaños", "precio": 45.0, "stock": 20},
            {"codigo": "R002", "nombre": "Globo metálico", "categoria": "Globos", "evento": "Cumpleaños", "precio": 12.0, "stock": 80},
            {"codigo": "R003", "nombre": "Cinta decorativa", "categoria": "Decoración", "evento": "Matrimonio", "precio": 8.5, "stock": 50},
            {"codigo": "R004", "nombre": "Caja sorpresa", "categoria": "Regalos", "evento": "Día de la Madre", "precio": 35.0, "stock": 25},
            {"codigo": "R005", "nombre": "Taza personalizada", "categoria": "Regalos", "evento": "Día del Profesor", "precio": 18.0, "stock": 30},
            {"codigo": "R006", "nombre": "Guirnalda de colores", "categoria": "Decoración", "evento": "Cumpleaños", "precio": 15.0, "stock": 40},
            {"codigo": "R007", "nombre": "Bolsa para sorpresa", "categoria": "Fiesta infantil", "evento": "Cumpleaños", "precio": 2.0, "stock": 100},
            {"codigo": "R008", "nombre": "Adorno para torta", "categoria": "Accesorios", "evento": "Cumpleaños", "precio": 10.0, "stock": 35},
            {"codigo": "R009", "nombre": "Set de decoración", "categoria": "Decoración", "evento": "Día del Padre", "precio": 28.0, "stock": 22},
            {"codigo": "R010", "nombre": "Recuerdo para matrimonio", "categoria": "Recuerdos", "evento": "Matrimonio", "precio": 6.0, "stock": 60}
        ]
        productos.extend(base)
        guardar_datos(ARCH_PRODUCTOS, productos)


def buscar_codigo(productos, codigo):
    """Busca un producto por su código."""
    for producto in productos:
        if producto["codigo"].lower() == codigo.lower():
            return producto
    return None


def registrar_producto(productos):
    """Registra un producto nuevo en el catálogo."""
    print("\n--- REGISTRAR PRODUCTO ---")

    codigo = leer_texto("Código: ")

    if buscar_codigo(productos, codigo):
        print("Ya existe un producto con ese código.")
        return

    nombre = leer_texto("Nombre del producto: ")
    categoria = leer_texto("Categoría: ")
    evento = leer_texto("Evento sugerido: ")
    precio = leer_float("Precio: ", 0.01)
    stock = leer_entero("Stock inicial: ", 0)

    producto = {
        "codigo": codigo,
        "nombre": nombre,
        "categoria": categoria,
        "evento": evento,
        "precio": precio,
        "stock": stock
    }

    productos.append(producto)
    guardar_datos(ARCH_PRODUCTOS, productos)

    print("Producto registrado correctamente.")


def listar_productos(productos):
    """Muestra todos los productos registrados."""
    print("\n--- CATÁLOGO PIÑATERÍA REY ---")

    if not productos:
        print("No hay productos registrados.")
        return

    print(f"{'CÓDIGO':<8} {'PRODUCTO':<28} {'CATEGORÍA':<18} {'EVENTO':<18} {'PRECIO':<10} {'STOCK':<8}")
    print("-" * 95)

    for p in productos:
        print(
            f"{p['codigo']:<8} "
            f"{p['nombre']:<28} "
            f"{p['categoria']:<18} "
            f"{p['evento']:<18} "
            f"S/ {p['precio']:<7.2f} "
            f"{p['stock']:<8}"
        )


def registrar_venta(productos, ventas):
    """Registra una venta y descuenta el stock."""
    print("\n--- REGISTRAR VENTA ---")

    codigo = leer_texto("Código del producto: ")
    producto = buscar_codigo(productos, codigo)

    if producto is None:
        print("Producto no encontrado.")
        return

    print(f"Producto: {producto['nombre']}")
    print(f"Precio: S/ {producto['precio']:.2f}")
    print(f"Stock disponible: {producto['stock']}")

    cantidad = leer_entero("Cantidad vendida: ", 1)

    if cantidad > producto["stock"]:
        print("Stock insuficiente.")
        return

    total = cantidad * producto["precio"]
    producto["stock"] -= cantidad

    venta = {
        "fecha": fecha_actual(),
        "codigo": producto["codigo"],
        "producto": producto["nombre"],
        "cantidad": cantidad,
        "evento": producto["evento"],
        "total": total
    }

    ventas.append(venta)

    guardar_datos(ARCH_PRODUCTOS, productos)
    guardar_datos(ARCH_VENTAS, ventas)

    print("Venta registrada correctamente.")
    print(f"Total a pagar: S/ {total:.2f}")


def registrar_pedido(pedidos):
    """Registra un pedido para un evento."""
    print("\n--- REGISTRAR PEDIDO PARA EVENTO ---")

    cliente = leer_texto("Nombre del cliente: ")
    tipo_evento = leer_texto("Tipo de evento: ")
    fecha_evento = leer_texto("Fecha del evento: ")
    descripcion = leer_texto("Detalle del pedido: ")
    anticipo = leer_float("Anticipo recibido: ", 0.0)

    pedido = {
        "fecha_registro": fecha_actual(),
        "cliente": cliente,
        "tipo_evento": tipo_evento,
        "fecha_evento": fecha_evento,
        "detalle": descripcion,
        "anticipo": anticipo,
        "estado": "Pendiente"
    }

    pedidos.append(pedido)
    guardar_datos(ARCH_PEDIDOS, pedidos)

    print("Pedido registrado correctamente.")


def buscar_producto(productos):
    """Busca productos por código, nombre, categoría o evento."""
    print("\n--- BUSCAR PRODUCTO ---")

    texto = leer_texto("Ingrese código, nombre, categoría o evento: ").lower()
    encontrados = []

    for p in productos:
        if (
            texto in p["codigo"].lower()
            or texto in p["nombre"].lower()
            or texto in p["categoria"].lower()
            or texto in p["evento"].lower()
        ):
            encontrados.append(p)

    if not encontrados:
        print("No se encontraron coincidencias.")
    else:
        print("\nProductos encontrados:")
        for p in encontrados:
            print(
                f"{p['codigo']} - {p['nombre']} - {p['categoria']} - "
                f"{p['evento']} - S/ {p['precio']:.2f} - Stock: {p['stock']}"
            )


def generar_reporte(productos, ventas, pedidos):
    """Genera reporte de ventas, pedidos y productos con stock bajo."""
    print("\n--- REPORTE GENERAL ---")

    total_ventas = sum(v["total"] for v in ventas)

    print(f"Ventas registradas: {len(ventas)}")
    print(f"Pedidos registrados: {len(pedidos)}")
    print(f"Monto total vendido: S/ {total_ventas:.2f}")

    print("\nProductos con stock bajo:")

    hay_bajo = False

    for p in productos:
        if p["stock"] <= 5:
            hay_bajo = True
            print(f"- {p['nombre']} | Stock: {p['stock']}")

    if not hay_bajo:
        print("No hay productos con stock bajo.")


def cargar_ventas_simuladas(productos, ventas):
    """Genera 50 ventas simuladas para probar el sistema."""
    print("\n--- CARGAR 50 VENTAS SIMULADAS ---")

    if not productos:
        print("No existen productos para simular.")
        return

    contador = 0
    intentos = 0

    while contador < 50 and intentos < 200:
        intentos += 1
        producto = random.choice(productos)

        if producto["stock"] <= 0:
            continue

        cantidad = random.randint(1, 2)

        if cantidad <= producto["stock"]:
            total = cantidad * producto["precio"]
            producto["stock"] -= cantidad

            venta = {
                "fecha": fecha_actual(),
                "codigo": producto["codigo"],
                "producto": producto["nombre"],
                "cantidad": cantidad,
                "evento": producto["evento"],
                "total": total
            }

            ventas.append(venta)
            contador += 1

    guardar_datos(ARCH_PRODUCTOS, productos)
    guardar_datos(ARCH_VENTAS, ventas)

    print(f"Se generaron {contador} ventas simuladas.")


def mostrar_menu():
    """Muestra el menú principal del sistema."""
    print("\n===== PIÑATERÍA REY =====")
    print("1. Registrar producto")
    print("2. Listar productos")
    print("3. Registrar venta")
    print("4. Registrar pedido")
    print("5. Buscar producto")
    print("6. Generar reporte")
    print("7. Cargar 50 ventas simuladas")
    print("8. Salir")


def main():
    """Función principal del programa."""
    productos = cargar_datos(ARCH_PRODUCTOS)
    ventas = cargar_datos(ARCH_VENTAS)
    pedidos = cargar_datos(ARCH_PEDIDOS)

    inicializar_catalogo(productos)

    while True:
        mostrar_menu()
        opcion = leer_entero("Seleccione una opción: ", 1)

        if opcion == 1:
            registrar_producto(productos)
        elif opcion == 2:
            listar_productos(productos)
        elif opcion == 3:
            registrar_venta(productos, ventas)
        elif opcion == 4:
            registrar_pedido(pedidos)
        elif opcion == 5:
            buscar_producto(productos)
        elif opcion == 6:
            generar_reporte(productos, ventas, pedidos)
        elif opcion == 7:
            cargar_ventas_simuladas(productos, ventas)
        elif opcion == 8:
            guardar_datos(ARCH_PRODUCTOS, productos)
            guardar_datos(ARCH_VENTAS, ventas)
            guardar_datos(ARCH_PEDIDOS, pedidos)
            print("Datos guardados. Fin del sistema.")
            break
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()
