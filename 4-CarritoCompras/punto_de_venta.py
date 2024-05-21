from producto import Producto
from carrito import Carrito

class PuntoDeVenta:
    def __init__(self):
        # Inicializa el punto de venta con una lista de productos y un registro de ventas.
        self.productos = []
        self.ventas = []
        self.piezas_vendidas = 0
        self.carrito_actual = None

    def mostrar_productos(self):
        # Imprime la lista de productos disponibles en el punto de venta.
        print("\nLista de productos disponibles:")
        for producto in self.productos:
            print(f"ID: {producto.id}, Nombre: {producto.nombre}, Stock: {producto.cantidad_en_stock}, Precio: ${producto.precio:.2f}")
        print()

    def iniciar_venta(self):
        # Crea un nuevo carrito para la venta actual.
        self.carrito_actual = Carrito()

    def agregar_producto_a_venta(self, producto_id, cantidad):
        # Busca el producto por ID y, si existe, intenta agregarlo al carrito de la venta actual.
        producto = next((p for p in self.productos if p.id == producto_id), None)
        if producto:
            cantidad_agregada = producto.reducir_stock(cantidad)
            if cantidad_agregada > 0:
                self.carrito_actual.agregar_producto(producto, cantidad_agregada)
                return True, f"Se han agregado {cantidad_agregada} artículos a tu carrito."
            return False, "No hay stock disponible."
        return False, "Producto no encontrado"

    def finalizar_venta(self):
        # Finaliza la venta actual, imprimiendo el total y agregando el total a las ventas registradas.
        if self.carrito_actual:
            total = self.carrito_actual.total
            num_articulos = self.carrito_actual.total_articulos()
            self.piezas_vendidas += num_articulos
            self.ventas.append(total)
            print(f"\nVenta realizada exitosamente:\nImporte total de venta: ${total:.2f}\nCantidad de artículos: {num_articulos}\n")
            self.carrito_actual = None

    def agregar_producto(self, id, nombre, precio, stock):
        # Añade un nuevo producto al inventario solo si el ID no está en uso.
        if any(p.id == id for p in self.productos):
            return False
        self.productos.append(Producto(id, nombre, precio, stock))
        return True

    def reporte_general(self):
        # Imprime un reporte general de las ventas y productos vendidos.
        print(f"\nCantidad de ventas: {len(self.ventas)}")
        print(f"Importe total de ventas: ${sum(self.ventas):.2f}")
        print(f"Cantidad de artículos: {len(self.productos)}")
        print(f"Total de piezas vendidas: {self.piezas_vendidas}\n")
