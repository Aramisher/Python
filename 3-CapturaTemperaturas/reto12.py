import statistics

def captura_temperaturas(mes):
    """Captura las temperaturas para el mes dado."""
    # Diccionario que contiene la cantidad de días de cada mes
    n_temperaturas = {"enero": 31, "febrero": 28, "marzo": 31, "abril": 30, "mayo": 31, "junio": 30,
                      "julio": 31, "agosto": 31, "septiembre": 30, "octubre": 31, "noviembre": 30, "diciembre": 31}

    # Lista para almacenar las temperaturas capturadas
    temperaturas = []

    # Captura las temperaturas día a día
    for i in range(n_temperaturas[mes]):
        temp = float(input(f"Ingrese la temperatura del día {i + 1} para {mes}: "))
        temperaturas.append(temp)

    return temperaturas

def calcula_estadisticas(temperaturas):
    """Calcula y devuelve las estadísticas de una lista de temperaturas."""
    # Calcula el promedio de las temperaturas
    promedio = sum(temperaturas) / len(temperaturas)

    # Calcula la mediana de las temperaturas
    mediana = statistics.median(temperaturas)

    # Calcula la moda de las temperaturas
    moda = statistics.mode(temperaturas)

    # Obtiene la temperatura máxima
    max_temp = max(temperaturas)

    # Obtiene la temperatura mínima
    min_temp = min(temperaturas)

    return promedio, mediana, moda, max_temp, min_temp

def reporte(meses, todas_temperaturas):
    """Genera un reporte final con el resumen de todas las operaciones."""
    # Total de meses capturados
    total_meses = len(meses)

    # Encuentra la mayor temperatura global
    max_global = max(todas_temperaturas)

    # Calcula el promedio global de todas las temperaturas capturadas
    promedio_global = sum(todas_temperaturas) / len(todas_temperaturas)

    return total_meses, max_global, promedio_global

def main():
    # Variable para controlar el ciclo
    continuar = True

    # Listas para almacenar los meses y todas las temperaturas
    meses = []
    todas_temperaturas = []

    while continuar:
        # Captura el mes
        mes = input("Ingrese el mes para capturar las temperaturas: ").lower()

        # Captura las temperaturas del mes ingresado
        temperaturas = captura_temperaturas(mes)

        # Calcula las estadísticas de las temperaturas capturadas
        promedio, mediana, moda, max_temp, min_temp = calcula_estadisticas(temperaturas)

        # Imprime las estadísticas
        print(f"Promedio de temperaturas: {promedio:.2f}")
        print(f"Mediana de temperaturas: {mediana:.2f}")
        print(f"Moda de temperaturas: {moda:.2f}")
        print(f"Temperatura máxima: {max_temp:.2f}")
        print(f"Temperatura mínima: {min_temp:.2f}")

        # Agrega el mes a la lista de meses
        meses.append(mes)

        # Agrega todas las temperaturas capturadas a la lista global
        todas_temperaturas.extend(temperaturas)

        # Pregunta al usuario si desea continuar capturando temperaturas
        respuesta = input("¿Desea continuar capturando temperaturas? (s/n): ").lower()
        if respuesta != 's':
            continuar = False

    # Genera el reporte final
    total_meses, max_global, promedio_global = reporte(meses, todas_temperaturas)

    # Imprime el reporte final
    print(f"{total_meses} meses capturados")
    print(f"Mayor temperatura de todos los meses capturados: {max_global:.2f}")
    print(f"Promedio de todas las temperaturas capturadas: {promedio_global:.2f}")

# Ejecuta la función principal
main()
