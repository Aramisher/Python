class Producto:
    def __init__(self, id, nombre, precio, cantidad_en_stock):
        # Inicializa un objeto Producto con su ID, nombre, precio y cantidad en stock.
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.cantidad_en_stock = cantidad_en_stock

    def reducir_stock(self, cantidad):
        # Reduce la cantidad en stock del producto y devuelve la cantidad reducida.
        if cantidad <= self.cantidad_en_stock:
            self.cantidad_en_stock -= cantidad
            return cantidad
        else:
            # Si la cantidad deseada supera el stock disponible, reduce el stock a 0 y devuelve la cantidad originalmente disponible.
            temp = self.cantidad_en_stock
            self.cantidad_en_stock = 0
            return temp

    def aumentar_stock(self, cantidad):
        # Aumenta la cantidad en stock del producto.
        self.cantidad_en_stock += cantidad
