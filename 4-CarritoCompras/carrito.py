class Carrito:
    def __init__(self):
        # Inicializa el carrito con un diccionario vacío para artículos y un total de 0.
        self.articulos = {}
        self.total = 0.0

    def agregar_producto(self, producto, cantidad):
        # Agrega un producto al carrito o incrementa la cantidad si ya está presente.
        if producto.id in self.articulos:
            self.articulos[producto.id]['cantidad'] += cantidad
        else:
            self.articulos[producto.id] = {'producto': producto, 'cantidad': cantidad}
        # Recalcula el total del carrito cada vez que se añade un producto.
        self.calcular_total()

    def calcular_total(self):
        # Calcula el total del carrito sumando el precio de cada producto multiplicado por su cantidad.
        total = 0.0
        for item in self.articulos.values():
            total += item['producto'].precio * item['cantidad']
        self.total = total

    def total_articulos(self):
        # Devuelve el número total de artículos en el carrito.
        return sum(item['cantidad'] for item in self.articulos.values())

    def vaciar_carrito(self):
        # Vacía el carrito y restablece el total a 0.
        self.articulos.clear()
        self.total = 0.0
