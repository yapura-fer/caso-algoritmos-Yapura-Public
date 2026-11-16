
import time
from statistics import mean

# ==========================================
# PRACTICA C4: BUSQUEDA LINEAL VS BINARIA
# Tienda de productos DXN
# ==========================================

# 1. LISTA DE 50 PRODUCTOS
# Reemplazar estos nombres por los nombres
# reales de los productos de tu tienda.

productos = [
    f"Producto DXN {i:02d}" for i in range(1, 51)
]

# Ordenar los productos alfabéticamente.
productos_ordenados = sorted(productos)


# 2. BUSQUEDA LINEAL
def busqueda_lineal(lista, objetivo):
    for producto in lista:
        if producto == objetivo:
            return True
    return False


# 3. BUSQUEDA BINARIA
def busqueda_binaria(lista, objetivo):
    izquierda = 0
    derecha = len(lista) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2

        if lista[medio] == objetivo:
            return True

        elif lista[medio] < objetivo:
            izquierda = medio + 1

        else:
            derecha = medio - 1

    return False


# 4. CONFIGURACION DE LA MEDICION
NUM_BUSQUEDAS = 20000
CALENTAMIENTO = 2000
REPETICIONES = 3

# Se buscan productos existentes.
objetivos = [
    productos_ordenados[i % len(productos_ordenados)]
    for i in range(NUM_BUSQUEDAS)
]


# 5. CALENTAMIENTO
# Se ejecutan búsquedas antes de medir.
for i in range(CALENTAMIENTO):
    objetivo = productos_ordenados[i % len(productos_ordenados)]

    busqueda_lineal(productos_ordenados, objetivo)
    busqueda_binaria(productos_ordenados, objetivo)


# 6. FUNCION PARA MEDIR LOS TIEMPOS
def medir_tiempo(algoritmo, lista, objetivos):
    inicio = time.perf_counter_ns()

    for objetivo in objetivos:
        algoritmo(lista, objetivo)

    fin = time.perf_counter_ns()

    tiempo_total = fin - inicio

    # Tiempo promedio por búsqueda en microsegundos.
    tiempo_por_busqueda = (
        tiempo_total / len(objetivos) / 1000
    )

    return tiempo_por_busqueda


# 7. REALIZAR TRES MEDICIONES
tiempos_lineal = []
tiempos_binaria = []

for repeticion in range(REPETICIONES):

    tiempo_l = medir_tiempo(
        busqueda_lineal,
        productos_ordenados,
        objetivos
    )

    tiempo_b = medir_tiempo(
        busqueda_binaria,
        productos_ordenados,
        objetivos
    )

    tiempos_lineal.append(tiempo_l)
    tiempos_binaria.append(tiempo_b)


# 8. CALCULAR PROMEDIOS
promedio_lineal = mean(tiempos_lineal)
promedio_binaria = mean(tiempos_binaria)

# Cociente entre ambos promedios.
cociente = promedio_lineal / promedio_binaria


# 9. MOSTRAR RESULTADOS
print("\n========================================")
print(" PRACTICA C4 - TIENDA DE PRODUCTOS DXN")
print(" BUSQUEDA LINEAL VS BUSQUEDA BINARIA")
print("========================================")

print("\nCantidad de productos:", len(productos))
print("Búsquedas por repetición:", NUM_BUSQUEDAS)
print("Calentamiento:", CALENTAMIENTO)
print("Repeticiones:", REPETICIONES)

print("\nRESULTADOS DE LAS MEDICIONES")
print("----------------------------------------")
print("Repetición | Lineal (us) | Binaria (us)")
print("----------------------------------------")

for i in range(REPETICIONES):
    print(
        f"{i + 1:^10} | "
        f"{tiempos_lineal[i]:^11.4f} | "
        f"{tiempos_binaria[i]:^12.4f}"
    )

print("----------------------------------------")
print(
    f"{'PROMEDIO':^10} | "
    f"{promedio_lineal:^11.4f} | "
    f"{promedio_binaria:^12.4f}"
)

print("\nCOCIENTE DE TIEMPOS")
print("----------------------------------------")
print(f"Lineal / Binaria = {cociente:.2f}")

if cociente > 1:
    print(
        f"La búsqueda binaria fue {cociente:.2f} "
        "veces más rápida."
    )
elif cociente < 1:
    print("La búsqueda lineal fue más rápida en esta medición.")
else:
    print("Ambos algoritmos tuvieron el mismo tiempo.")

print("\n========================================")
print(" FIN DE LA PRACTICA C4")
print("========================================")
