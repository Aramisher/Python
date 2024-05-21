from punto_de_venta import PuntoDeVenta

def main():
    # Inicializa el sistema de punto de venta.
    pdv = PuntoDeVenta()
    # Agrega un producto inicial al sistema.
    pdv.agregar_producto(1, "Silla de madera", 550.50, 5)

    # Ciclo principal del programa.
    while True:
        print("\nCarrito de compras:")
        print("A. Listar productos")
        print("B. Agregar producto")
        print("C. Realizar venta")
        print("S. Salir")

        # Recoge la opción del usuario.
        opcion = input("Elige una opción: ").strip().upper()
        if opcion == 'A':
            # Muestra los productos disponibles.
            pdv.mostrar_productos()
        elif opcion == 'B':
            # Permite al usuario agregar un producto nuevo.
            while True:
                id = int(input("ID: "))
                # Verifica que el ID del producto no esté en uso.
                if not pdv.agregar_producto(id, "", 0, 0):  
                    print("Este ID ya está en uso, por favor usa un ID diferente.")
                else:
                    pdv.productos.pop()  
                    break
            nombre = input("Nombre del producto: ")
            stock = int(input("Stock: "))
            precio = float(input("Precio: "))
            pdv.agregar_producto(id, nombre, precio, stock)
            print("Producto agregado exitosamente al catálogo")
        elif opcion == 'C':
            # Inicia un proceso de venta.
            pdv.iniciar_venta()
            while True:
                pdv.mostrar_productos()
                prod_id = int(input("Ingresa código de producto: "))
                cant = int(input("Cantidad: "))
                success, message = pdv.agregar_producto_a_venta(prod_id, cant)
                print(message)
                cont = input("Terminar ventas (N) o agregar producto (S): ").strip().upper()
                if cont == 'N':
                    pdv.finalizar_venta()
                    break
        elif opcion == 'S':
            # Imprime el reporte general y sale del programa.
            pdv.reporte_general()
            break

if __name__ == "__main__":
    main()
