# Fernando Yapura Ignacio
# PARCIAL 1 - VARIANTE B
# Registro de comprobantes
import random
import time
# SOLUCION ORIGINAL: COMPARACION POR PARES
def hay_comprobantes_repetidos_por_pares(comprobantes):
    for a in range(len(comprobantes)):
        for b in range(a + 1, len(comprobantes)):
            if comprobantes[a] == comprobantes[b]:
                return True
    return False
# TU CURA: completa esta funcion utilizando un conjunto (set).
def hay_comprobantes_repetidos_curado(comprobantes):
    vistos = set()

    for dato in comprobantes:
        if dato in vistos:
            return True
        vistos.add(dato)
    return False
# GENERAR LISTA SIN REPETIDOS
def generar_sin_repetidos(n, semilla=77):
    datos = list(range(1000, 1000 + n))
    azar = random.Random(semilla)
    azar.shuffle(datos)
    return datos
# CINCO CASOS DE PRUEBA
casos = [
    ([1010, 1003, 1009, 1003, 1005], True, "Repetido en el medio"),
    ([1010, 1003, 1009, 1004, 1005], False, "Sin repetidos"),
    ([], False, "Lista vacia"),
    ([1008], False, "Un solo elemento"),
    ([1004, 1001, 1002, 1006, 1004], True, "Repetido en los extremos")
]
def probar():
    print("\n--- CINCO CASOS DE PRUEBA ---")
    for datos, esperado, nombre in casos:
        lenta = hay_comprobantes_repetidos_por_pares(datos)
        try:
            curada = hay_comprobantes_repetidos_curado(datos)
            resultado = str(curada)
        except NotImplementedError:
            resultado = "Pendiente"

        print(nombre, "| Esperado:", esperado,
              "| Por pares:", lenta, "| Cura:", resultado)
if __name__ == "__main__":
    probar()
# ==========================================
# MEDICION DE RENDIMIENTO DE LOS ALGORITMOS
# ==========================================
import time
import random
def generar_lista_medicion(n, semilla=77):
    """Genera una lista desordenada sin elementos repetidos."""
    datos = list(range(1000, 1000 + n))
    azar = random.Random(semilla)
    azar.shuffle(datos)
    return datos
def medir_tiempo(funcion, datos):
    """Devuelve el tiempo de ejecución en segundos."""
    inicio = time.perf_counter()
    funcion(datos)
    fin = time.perf_counter()
    return fin - inicio
def promedio_tres(tiempos):
    return sum(tiempos) / len(tiempos)
def ejecutar_mediciones():
    n = 1000
    tamanos = [n, 2*n, 4*n, 8*n]
    resultados = []
    print("\n======================================")
    print("       MEDICION DE ALGORITMOS")
    print("======================================")
    for tamano in tamanos:
        datos = generar_lista_medicion(tamano)
        # Una ejecución de calentamiento por algoritmo
        hay_comprobantes_repetidos_por_pares(datos)
        hay_comprobantes_repetidos_curado(datos)
        tiempos_original = []
        tiempos_curado = []
        # Tres ejecuciones medidas
        for repeticion in range(3):
            tiempos_original.append(
                medir_tiempo(hay_comprobantes_repetidos_por_pares, datos)
            )
            tiempos_curado.append(
                medir_tiempo(hay_comprobantes_repetidos_curado, datos)
            )
        promedio_original = promedio_tres(tiempos_original)
        promedio_curado = promedio_tres(tiempos_curado)
        resultados.append((
            tamano,
            promedio_original,
            promedio_curado
        ))
    print("\nTAMAÑO | ORIGINAL (s) | OPTIMIZADO (s) | VECES ORIGINAL | VECES OPTIMIZADO")
    anterior_original = None
    anterior_curado = None
    for tamano, original, curado in resultados:
        if anterior_original is None:
            veces_original = "-"
            veces_curado = "-"
        else:
            veces_original = f"{original / anterior_original:.2f}"
            veces_curado = f"{curado / anterior_curado:.2f}"
        print(
            f"{tamano:6} | "
            f"{original:12.6f} | "
            f"{curado:14.6f} | "
            f"{veces_original:14} | "
            f"{veces_curado}"
        )
        anterior_original = original
        anterior_curado = curado
    print("\nMediciones finalizadas.")
    print("Los tiempos corresponden al promedio de tres ejecuciones.")
# Ejecutar las mediciones
ejecutar_mediciones()
