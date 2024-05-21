# Definición de variables y criterios para tornillo de acero inoxidable
diametro_cabeza_acero = 7  # en mm
altura_cabeza_acero = 3  # en mm
cuello_acero = 5  # en mm
rosca_acero = 6.5  # en cm

# Evaluación de criterios para tornillo de acero inoxidable
aceptacion_acero = (6.5 <= diametro_cabeza_acero <= 7.5) and (2.5 <= altura_cabeza_acero <= 3.5) and \
                   (4.5 <= cuello_acero <= 5.5) and (6 <= rosca_acero <= 7)

# Definición de variables y criterios para tornillo para hormigón
diametro_cabeza_hormigon = 6  # en mm
altura_cabeza_hormigon = 4  # en mm
cuello_hormigon = 4  # en mm
rosca_hormigon = 8.5  # en cm

# Evaluación de criterios para tornillo para hormigón
aceptacion_hormigon = (5.5 <= diametro_cabeza_hormigon <= 6.5) and (3.5 <= altura_cabeza_hormigon <= 4.5) and \
                      (3.5 <= cuello_hormigon <= 4.5) and (8 <= rosca_hormigon <= 9)

# Definición de variables y criterios para clavos galvanizados
cabeza_clavos = 4  # en mm
cana_clavos = 5.7  # en cm

# Evaluación de criterios para clavos galvanizados
aceptacion_clavos = (3.5 <= cabeza_clavos <= 4.5) and (5.5 <= cana_clavos <= 6)

# Escenarios y sus evaluaciones
escenarios = {
    "Acero": [
        {"diametro_cabeza": 7, "altura_cabeza": 3, "cuello": 5, "rosca": 6.5},
        {"diametro_cabeza": 7.6, "altura_cabeza": 3.1, "cuello": 5.1, "rosca": 6.9},
        {"diametro_cabeza": 6.4, "altura_cabeza": 2.9, "cuello": 4.9, "rosca": 6.1},
        {"diametro_cabeza": 7.2, "altura_cabeza": 3.3, "cuello": 5.3, "rosca": 6.8},
        {"diametro_cabeza": 7.1, "altura_cabeza": 3.4, "cuello": 5.6, "rosca": 7.1}
    ],
    "Hormigón": [
        {"diametro_cabeza": 6, "altura_cabeza": 4, "cuello": 4, "rosca": 8.5},
        {"diametro_cabeza": 6.6, "altura_cabeza": 4.1, "cuello": 4.2, "rosca": 9.1},
        {"diametro_cabeza": 5.4, "altura_cabeza": 3.4, "cuello": 3.4, "rosca": 7.9},
        {"diametro_cabeza": 6.1, "altura_cabeza": 4.3, "cuello": 4.4, "rosca": 8.6},
        {"diametro_cabeza": 6.5, "altura_cabeza": 4.5, "cuello": 4.5, "rosca": 8.8}
    ],
    "Clavos": [
        {"cabeza": 4, "cana": 5.7},
        {"cabeza": 4.5, "cana": 6},
        {"cabeza": 3.4, "cana": 5.4},
        {"cabeza": 4.1, "cana": 5.9},
        {"cabeza": 4.6, "cana": 6.1}
    ]
}

# Imprimir los resultados para cada escenario
for tipo, escenarios in escenarios.items():
    print(f"Resultados para {tipo}:")
    for i, escenario in enumerate(escenarios):
        if tipo == "Acero":
            resultado = (6.5 <= escenario["diametro_cabeza"] <= 7.5) and (2.5 <= escenario["altura_cabeza"] <= 3.5) and \
                        (4.5 <= escenario["cuello"] <= 5.5) and (6 <= escenario["rosca"] <= 7)
        elif tipo == "Hormigón":
            resultado = (5.5 <= escenario["diametro_cabeza"] <= 6.5) and (3.5 <= escenario["altura_cabeza"] <= 4.5) and \
                        (3.5 <= escenario["cuello"] <= 4.5) and (8 <= escenario["rosca"] <= 9)
        elif tipo == "Clavos":
            resultado = (3.5 <= escenario["cabeza"] <= 4.5) and (5.5 <= escenario["cana"] <= 6)
        
        print(f" Escenario {i+1}: {escenario}, Cumple con los criterios: {resultado}")
    print("---------------------------------------------------")
