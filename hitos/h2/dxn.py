
# ============================================================
# HITO H2 - CASO INTEGRADOR
# REGISTRO DE VENTAS Y CONTROL DE INVENTARIO - TIENDA DXN
# Comparacion: Lista desordenada vs Diccionario
# ============================================================

import time
import math
from pathlib import Path


# ------------------------------------------------------------
# 1. GENERAR PRODUCTOS DE PRUEBA
# ------------------------------------------------------------

def generar_productos(cantidad):
    productos = []

    for i in range(1, cantidad + 1):
        producto = {
            "codigo": f"DXN{i:04d}",
            "nombre": f"Producto DXN {i}",
            "precio": 15.0 + (i % 20) * 2.5,
            "stock": 1000000
        }

        productos.append(producto)

    return productos


# ------------------------------------------------------------
# 2. GENERAR VENTAS DE PRUEBA
# ------------------------------------------------------------

def generar_ventas(cantidad_productos):
    ventas = []

    # Se generan 20 ventas por cada producto del inventario.
    for i in range(cantidad_productos * 20):
        indice = (i * 7) % cantidad_productos
        codigo = f"DXN{indice + 1:04d}"
        cantidad = (i % 3) + 1

        ventas.append((codigo, cantidad))

    return ventas


# ------------------------------------------------------------
# 3. SOLUCION INGENUA: LISTA DESORDENADA
# ------------------------------------------------------------

def procesar_ventas_lista(productos, ventas):
    total_ventas = 0.0

    for codigo, cantidad in ventas:

        # Buscar recorriendo la lista.
        encontrado = None

        for producto in productos:
            if producto["codigo"] == codigo:
                encontrado = producto
                break

        if encontrado is None:
            raise ValueError("Producto no encontrado")

        # Calcular el importe.
        importe = encontrado["precio"] * cantidad
        total_ventas += importe

        # Actualizar existencias.
        encontrado["stock"] -= cantidad

    return total_ventas


# ------------------------------------------------------------
# 4. SOLUCION MEJORADA: DICCIONARIO
# ------------------------------------------------------------

def procesar_ventas_diccionario(productos, ventas):
    total_ventas = 0.0

    # Buscar directamente por codigo.
    for codigo, cantidad in ventas:

        producto = productos.get(codigo)

        if producto is None:
            raise ValueError("Producto no encontrado")

        # Calcular el importe.
        importe = producto["precio"] * cantidad
        total_ventas += importe

        # Actualizar existencias.
        producto["stock"] -= cantidad

    return total_ventas


# ------------------------------------------------------------
# 5. PREPARAR LAS ESTRUCTURAS
# ------------------------------------------------------------

def preparar_lista(productos):
    return [producto.copy() for producto in productos]


def preparar_diccionario(productos):
    return {
        producto["codigo"]: producto.copy()
        for producto in productos
    }


# ------------------------------------------------------------
# 6. MEDIR EL TIEMPO DE EJECUCION
# ------------------------------------------------------------

def medir_lista(productos, ventas):
    datos = preparar_lista(productos)

    inicio = time.perf_counter()

    resultado = procesar_ventas_lista(datos, ventas)

    fin = time.perf_counter()

    return fin - inicio, resultado


def medir_diccionario(productos, ventas):
    datos = preparar_diccionario(productos)

    inicio = time.perf_counter()

    resultado = procesar_ventas_diccionario(datos, ventas)

    fin = time.perf_counter()

    return fin - inicio, resultado


# ------------------------------------------------------------
# 7. FUNCIONES AUXILIARES
# ------------------------------------------------------------

def promedio(tiempos):
    return sum(tiempos) / len(tiempos)


def factor_crecimiento(actual, anterior):
    if anterior is None or anterior == 0:
        return "—"

    return f"{actual / anterior:.2f}x"


# ------------------------------------------------------------
# 8. EJECUTAR LAS PRUEBAS
# ------------------------------------------------------------

def ejecutar_pruebas():

    tamanos = [50, 100, 200, 400]

    resultados = []

    print("=" * 65)
    print(" HITO H2 - TIENDA DE PRODUCTOS DXN")
    print(" COMPARACION DE ESTRUCTURAS DE DATOS")
    print("=" * 65)

    for cantidad in tamanos:

        print(f"\nCantidad de productos: {cantidad}")

        productos = generar_productos(cantidad)
        ventas = generar_ventas(cantidad)

        # CALENTAMIENTO
        medir_lista(productos, ventas)
        medir_diccionario(productos, ventas)

        tiempos_lista = []
        tiempos_diccionario = []

        # TRES REPETICIONES
        for repeticion in range(3):

            tiempo_l, total_l = medir_lista(productos, ventas)
            tiempo_d, total_d = medir_diccionario(productos, ventas)

            # Verificar que ambas soluciones hagan el mismo trabajo.
            if not math.isclose(total_l, total_d, rel_tol=1e-12):
                raise RuntimeError("Los resultados no coinciden")

            tiempos_lista.append(tiempo_l)
            tiempos_diccionario.append(tiempo_d)

            print(f"Repeticion {repeticion + 1}:")
            print(f"  Lista:       {tiempo_l:.8f} segundos")
            print(f"  Diccionario: {tiempo_d:.8f} segundos")

        media_lista = promedio(tiempos_lista)
        media_diccionario = promedio(tiempos_diccionario)

        resultados.append({
            "cantidad": cantidad,
            "lista": media_lista,
            "diccionario": media_diccionario
        })

        print(f"Promedio lista:       {media_lista:.8f} segundos")
        print(f"Promedio diccionario: {media_diccionario:.8f} segundos")

    return resultados


# ------------------------------------------------------------
# 9. GENERAR EL ARCHIVO medicion.md
# ------------------------------------------------------------

def generar_informe(resultados):

    lineas = []

    lineas.append("# MEDICION DE RENDIMIENTO - TIENDA DXN")
    lineas.append("")
    lineas.append("## 1. Objetivo")
    lineas.append("")
    lineas.append(
        "Comparar el rendimiento del registro de ventas y la "
        "actualizacion de existencias utilizando una lista "
        "desordenada y un diccionario."
    )
    lineas.append("")
    lineas.append("## 2. Protocolo de medicion")
    lineas.append("")
    lineas.append("- Se probaron 50, 100, 200 y 400 productos.")
    lineas.append("- Se genero la misma cantidad de ventas por producto: 20.")
    lineas.append("- Se realizo una ejecucion de calentamiento.")
    lineas.append("- Se realizaron tres repeticiones por cada estructura.")
    lineas.append("- Se calculo el promedio de los tres tiempos.")
    lineas.append(
        "- La preparacion y copia de las estructuras se realizo "
        "fuera del tiempo medido."
    )
    lineas.append(
        "- Se utilizo time.perf_counter() para medir el tiempo."
    )
    lineas.append("")
    lineas.append("## 3. Resultados")
    lineas.append("")
    lineas.append(
        "| Productos | Lista (s) | Crecimiento lista | "
        "Diccionario (s) | Crecimiento diccionario |"
    )
    lineas.append(
        "|---:|---:|---:|---:|---:|"
    )

    anterior_lista = None
    anterior_diccionario = None

    for resultado in resultados:

        cantidad = resultado["cantidad"]
        lista = resultado["lista"]
        diccionario = resultado["diccionario"]

        factor_l = factor_crecimiento(lista, anterior_lista)
        factor_d = factor_crecimiento(
            diccionario, anterior_diccionario
        )

        lineas.append(
            f"| {cantidad} | {lista:.8f} | {factor_l} | "
            f"{diccionario:.8f} | {factor_d} |"
        )

        anterior_lista = lista
        anterior_diccionario = diccionario

    lineas.append("")
    lineas.append("## 4. Conclusion")
    lineas.append("")

    ultimo = resultados[-1]

    if ultimo["lista"] > ultimo["diccionario"]:
        diferencia = (
            ultimo["lista"] / ultimo["diccionario"]
        )

        lineas.append(
            f"En la prueba de {ultimo['cantidad']} productos, "
            f"la lista tardó aproximadamente {diferencia:.2f} "
            "veces más que el diccionario."
        )
        lineas.append(
            "Los resultados muestran la ventaja de utilizar "
            "un diccionario para buscar productos por código."
        )
    else:
        lineas.append(
            "En la última prueba los tiempos fueron similares "
            "o el diccionario no fue más rápido."
        )
        lineas.append(
            "Esto puede deberse al tamaño de los datos y al "
            "ruido de las mediciones."
        )

    lineas.append(
        "La diferencia se relaciona con el costo O(n) de la "
        "búsqueda lineal frente al costo promedio O(1) "
        "del diccionario."
    )
    lineas.append(
        "Los tiempos pueden variar por el procesador, otros "
        "procesos del equipo y el ruido de medición."
    )

    ruta = Path(__file__).with_name("medicion.md")

    ruta.write_text(
        "\n".join(lineas),
        encoding="utf-8"
    )

    print("\nInforme generado correctamente:")
    print(ruta)


# ------------------------------------------------------------
# 10. PROGRAMA PRINCIPAL
# ------------------------------------------------------------

if __name__ == "__main__":

    resultados = ejecutar_pruebas()

    generar_informe(resultados)

    print("\n" + "=" * 65)
    print(" PRUEBAS FINALIZADAS")
    print(" Se genero el archivo medicion.md")
    print("=" * 65)
