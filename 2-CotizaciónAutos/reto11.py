def cotizacion_renta_automoviles():
    # Función para calcular la cotización de renta de automóviles
    
    # Mensaje de inicio
    print("Renta de Autos - Cotización de Servicio")
    
    # Precios por modelo y año
    precios_modelo = {
        2017: 550,
        2018: 590,
        2019: 650,
        2020: 700,
        2021: 750
    }
    
    # Mostrar modelos disponibles y sus precios
    print("\nModelos disponibles y sus precios diarios:")
    for modelo, precio in precios_modelo.items():
        print(f"Modelo {modelo}: ${precio:.2f} por día")
    
    # Loop principal para recibir múltiples cotizaciones
    while True:
        # Loop para validar el número de licencia
        while True:
            numero_licencia = input("\nIndica tu número de licencia (debe ser un número de 6 dígitos): ")
            if numero_licencia.isdigit() and len(numero_licencia) == 6:
                break
            else:
                print("Número de licencia inválido. Asegúrate de que sean exactamente 6 dígitos.")

        # Obtener la cantidad de días de renta y la edad del cliente
        dias_renta = int(input("Indica la cantidad de días de renta: "))
        edad = int(input("Indica tu edad: "))
        
        # Loop para validar el modelo seleccionado
        while True:
            modelo = int(input("Indica modelo de automóvil: "))
            if modelo in precios_modelo:
                break
            else:
                print("Modelo no disponible. Por favor elige uno de los modelos listados.")

        # Calcular costos y total
        costo_diario = precios_modelo[modelo]
        subtotal = costo_diario * dias_renta
        total = subtotal
        mensaje_adicional = ""

        # Calcular seguro adicional si el cliente es menor de edad
        if 15 <= edad <= 17:
            seguro = subtotal * 0.8
            total += seguro
            mensaje_adicional += f"Cliente tipo: menor de edad\nSeguro menor edad: ${seguro:,.2f}\n** Una vez entregada la unidad se reembolsa el seguro menor edad."

        # Imprimir información de la cotización
        print(f"\nEstimado cliente con número de licencia: {numero_licencia}")
        if dias_renta < 3:
            mensaje_adicional += "\n** Estimado usuario la renta mínima es de 3 días por lo que su cotización no es válida."
        
        print(f"Subtotal: ${subtotal:,.2f}")
        if mensaje_adicional:
            print(mensaje_adicional)
        print(f"Total a pagar: ${total:,.2f}")

        # Preguntar si se desea realizar otra cotización
        print("\n¿Desea realizar otra cotización? (sí/no)")
        continuar = input().lower()
        if continuar not in ['sí', 'si', 's', 'yes', 'y']:
            break

cotizacion_renta_automoviles()
