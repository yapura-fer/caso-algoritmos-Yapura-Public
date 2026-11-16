
import random
import time
import csv
from statistics import mean

# ==========================================
# PRACTICA C5: TORNEO DE ORDENAMIENTOS
# PROYECTO: TIENDA DE PRODUCTOS DXN
# ==========================================

# Cantidades crecientes de datos
TAMANOS = [100, 500, 1000, 2000, 4000]

REPETICIONES = 3
CALENTAMIENTO = 3

# ------------------------------------------
# 1. ORDENAMIENTO BURBUJA
# Algoritmo cuadratico O(n^2)
# ------------------------------------------

def burbuja(lista):
    n = len(lista)

    for i in range(n - 1):
        hubo_cambio = False

        for j in range(n - 1 - i):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                hubo_cambio = True

        if not hubo_cambio:
            break

    return lista


# ------------------------------------------
# 2. MERGESORT
# Algoritmo O(n log n)
# ------------------------------------------

def merge_sort(lista):

    if len(lista) <= 1:
        return lista

    medio = len(lista) // 2

    izquierda = merge_sort(lista[:medio])
    derecha = merge_sort(lista[medio:])

    resultado = []
    i = 0
    j = 0

    while i < len(izquierda) and j < len(derecha):

        if izquierda[i] <= derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1

    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])

    return resultado


# ------------------------------------------
# 3. QUICKSORT
# Promedio O(n log n)
# ------------------------------------------

def quick_sort(lista):

    def ordenar(izquierda, derecha):

        if izquierda >= derecha:
            return

        pivote = lista[(izquierda + derecha) // 2]

        i = izquierda
        j = derecha

        while i <= j:

            while lista[i] < pivote:
                i += 1

            while lista[j] > pivote:
                j -= 1

            if i <= j:
                lista[i], lista[j] = lista[j], lista[i]
                i += 1
                j -= 1

        if izquierda < j:
            ordenar(izquierda, j)

        if i < derecha:
            ordenar(i, derecha)

    ordenar(0, len(lista) - 1)

    return lista


# ------------------------------------------
# 4. PREPARAR ALGORITMOS
# ------------------------------------------

algoritmos = {
    "Burbuja": burbuja,
    "MergeSort": merge_sort,
    "QuickSort": quick_sort
}

random.seed(42)

resultados = []

# ------------------------------------------
# 5. CALENTAMIENTO
# ------------------------------------------

datos_calentamiento = [
    random.randint(1, 100000) for _ in range(100)
]

for _ in range(CALENTAMIENTO):
    for algoritmo in algoritmos.values():
        copia = datos_calentamiento.copy()
        algoritmo(copia)


# ------------------------------------------
# 6. TORNEO DE ORDENAMIENTOS
# ------------------------------------------

print("\n==========================================")
print(" TORNEO DE ORDENAMIENTOS - TIENDA DXN")
print("==========================================")

for cantidad in TAMANOS:

    datos = [
        random.randint(1, 100000)
        for _ in range(cantidad)
    ]

    tiempos = {
        "Burbuja": [],
        "MergeSort": [],
        "QuickSort": []
    }

    for nombre, algoritmo in algoritmos.items():

        for repeticion in range(REPETICIONES):

            # Copia fuera del tiempo medido
            copia = datos.copy()

            inicio = time.perf_counter()

            resultado = algoritmo(copia)

            fin = time.perf_counter()

            tiempo = fin - inicio

            assert resultado == sorted(datos), (
                f"Error en {nombre}"
            )

            tiempos[nombre].append(tiempo)

    promedios = {
        nombre: mean(lista)
        for nombre, lista in tiempos.items()
    }

    resultados.append({
        "Cantidad": cantidad,
        "Burbuja": promedios["Burbuja"],
        "MergeSort": promedios["MergeSort"],
        "QuickSort": promedios["QuickSort"]
    })


# ------------------------------------------
# 7. MOSTRAR TABLA DE RESULTADOS
# ------------------------------------------

print("\nRESULTADOS PROMEDIO (SEGUNDOS)")
print("-" * 75)

print(
    f"{'Datos':>8} | {'Burbuja':>14} | "
    f"{'MergeSort':>14} | {'QuickSort':>14}"
)

print("-" * 75)

for fila in resultados:

    print(
        f"{fila['Cantidad']:>8} | "
        f"{fila['Burbuja']:>14.6f} | "
        f"{fila['MergeSort']:>14.6f} | "
        f"{fila['QuickSort']:>14.6f}"
    )

print("-" * 75)


# ------------------------------------------
# 8. GUARDAR RESULTADOS EN CSV
# ------------------------------------------

with open(
    "resultados_c5.csv",
    "w",
    newline="",
    encoding="utf-8"
) as archivo:

    campos = [
        "Cantidad",
        "Burbuja",
        "MergeSort",
        "QuickSort"
    ]

    escritor = csv.DictWriter(
        archivo,
        fieldnames=campos
    )

    escritor.writeheader()
    escritor.writerows(resultados)


# ------------------------------------------
# 9. CONCLUSION AUTOMATICA
# ------------------------------------------

ultimo = resultados[-1]

mas_rapido = min(
    ["Burbuja", "MergeSort", "QuickSort"],
    key=lambda nombre: ultimo[nombre]
)

print("\nCONCLUSION DEL TORNEO")
print("------------------------------------------")
print(
    f"Con {ultimo['Cantidad']} datos, "
    f"el algoritmo mas rapido fue: {mas_rapido}"
)

print("\nArchivo generado: resultados_c5.csv")
print("Practica C5 finalizada.")
print("==========================================")
