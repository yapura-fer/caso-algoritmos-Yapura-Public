# Fernando Yapura Ignacio
# EVALUACION INTEGRADORA - VARIANTE B
# COMPRAS DE UNA ESCUELA
import random
import time
# ==========================================
# CLASE UTIL
# ==========================================
class Util:
    def __init__(self, codigo, costo_bs, utilidad):
        self.codigo = codigo
        self.costo_bs = costo_bs
        self.utilidad = utilidad
# ==========================================
# SOLUCION INGENUA
# Prueba todos los subconjuntos
# Complejidad: O(n * 2^n)
# ==========================================
class CompradorIngenuo:
    def __init__(self):
        self.elegidos = []
    def Elegir(self, utiles, presupuesto_bs):
        n = len(utiles)
        mejor = 0
        mejor_mascara = 0
        for mascara in range(1 << n):
            costo = 0
            utilidad = 0

            for i in range(n):
                if mascara & (1 << i):
                    costo += utiles[i].costo_bs
                    utilidad += utiles[i].utilidad

            if costo <= presupuesto_bs and utilidad > mejor:
                mejor = utilidad
                mejor_mascara = mascara

        self.elegidos = []

        for i in range(n):
            if mejor_mascara & (1 << i):
                self.elegidos.append(utiles[i].codigo)

        return mejor, self.elegidos.copy()

    def EstaEnLaCompra(self, codigo):
        return codigo in self.elegidos
# ==========================================
# SOLUCION MEJORADA
# Programacion dinamica - Mochila 0/1
# Complejidad: O(n * B)
# ==========================================
class CompradorMejorado:
    def __init__(self):
        self.elegidos = set()
    def Elegir(self, utiles, presupuesto_bs):
        self.elegidos.clear()
        n = len(utiles)
        if presupuesto_bs < 0:
            raise ValueError("El presupuesto no puede ser negativo")
        if n == 0:
            return 0, []
        for util in utiles:
            if util.costo_bs < 0 or util.utilidad < 0:
                raise ValueError("Costo y utilidad deben ser no negativos")
        # dp[b] guarda la mejor utilidad con presupuesto b
        dp = [0] * (presupuesto_bs + 1)

        # Guarda las decisiones para reconstruir la compra
        decisiones = [
            bytearray(presupuesto_bs + 1)
            for _ in range(n)
        ]

        # Procesar cada útil
        for i in range(n):

            costo = utiles[i].costo_bs
            utilidad = utiles[i].utilidad

            # Recorrer de mayor a menor para no repetir el útil
            for b in range(presupuesto_bs, costo - 1, -1):

                nueva_utilidad = dp[b - costo] + utilidad

                if nueva_utilidad > dp[b]:

                    dp[b] = nueva_utilidad
                    decisiones[i][b] = 1

        # Reconstruir los útiles seleccionados
        presupuesto_restante = presupuesto_bs
        codigos = []

        for i in range(n - 1, -1, -1):

            if decisiones[i][presupuesto_restante]:

                util = utiles[i]

                codigos.append(util.codigo)
                self.elegidos.add(util.codigo)

                presupuesto_restante -= util.costo_bs

        return dp[presupuesto_bs], codigos

    def EstaEnLaCompra(self, codigo):
        return codigo in self.elegidos
# ==========================================
# CREAR LISTAS DE UTILES
# ==========================================
def Lote(*datos):
    return [
        Util(codigo, costo, utilidad)
        for codigo, costo, utilidad in datos
    ]
# ==========================================
# CASOS DE PRUEBA
# ==========================================
Casos = [
    (
        "el voraz se equivoca",
        Lote(
            ("U1", 20, 120),
            ("U2", 40, 200),
            ("U3", 60, 240)
        ),
        100,
        440,
        ["U2", "U3"]
    ),

    (
        "cuatro utiles",
        Lote(
            ("U1", 4, 6),
            ("U2", 6, 8),
            ("U3", 8, 10),
            ("U4", 10, 12)
        ),
        16,
        20,
        ["U2", "U4"]
    ),

    (
        "presupuesto cero",
        Lote(
            ("U1", 5, 10),
            ("U2", 7, 12)
        ),
        0,
        0,
        []
    ),

    (
        "sin utiles",
        Lote(),
        30,
        0,
        []
    ),

    (
        "nada cabe",
        Lote(
            ("U1", 80, 90),
            ("U2", 100, 100)
        ),
        60,
        0,
        []
    ),

    (
        "entran todos",
        Lote(
            ("U1", 10, 20),
            ("U2", 14, 24),
            ("U3", 6, 8)
        ),
        200,
        52,
        ["U1", "U2", "U3"]
    )
]
# ==========================================
# EJECUTAR PRUEBAS
# ==========================================
def Probar(titulo, fabrica):

    bien = 0
    total = 0

    for que, utiles, presupuesto, esperada, codigos in Casos:

        comprador = fabrica()

        utilidad, elegidos = comprador.Elegir(
            utiles, presupuesto
        )

        total += 1

        if (
            utilidad == esperada
            and sorted(elegidos) == sorted(codigos)
        ):
            bien += 1
        else:
            print("ERROR en:", que)
            print("Esperado:", esperada, codigos)
            print("Obtenido:", utilidad, elegidos)

    comprador = fabrica()

    comprador.Elegir(
        Casos[0][1],
        Casos[0][2]
    )

    total += 2

    if comprador.EstaEnLaCompra("U2"):
        bien += 1
    else:
        print("ERROR: U2 deberia estar en la compra")

    if not comprador.EstaEnLaCompra("U1"):
        bien += 1
    else:
        print("ERROR: U1 no deberia estar en la compra")

    print(f"{titulo}: {bien} de {total} pruebas correctas")
# ==========================================
# GENERAR CARGA ALEATORIA
# ==========================================
def EjecutarCarga(comprador, n):

    azar = random.Random(n + 1000)

    utiles = [
        Util(
            "K" + str(i),
            azar.randint(4, 49),
            azar.randint(10, 99)
        )
        for i in range(n)
    ]

    presupuesto = sum(
        u.costo_bs for u in utiles
    ) // 3

    utilidad, codigos = comprador.Elegir(
        utiles, presupuesto
    )

    return utilidad
# ==========================================
# CARGA CON PRESUPUESTO ESPECIFICO
# ==========================================
def EjecutarCargaConPresupuesto(comprador, n, presupuesto):

    azar = random.Random(n + 1000)

    utiles = [
        Util(
            "K" + str(i),
            azar.randint(4, 49),
            azar.randint(10, 99)
        )
        for i in range(n)
    ]

    utilidad, codigos = comprador.Elegir(
        utiles, presupuesto
    )

    return utilidad

# ==========================================
# MEDICIONES
# 1 calentamiento + 3 corridas
# ==========================================

def Medir(n):

    print("\n================================")
    print("CANTIDAD DE UTILES:", n)
    print("================================")

    # Calentamiento
    resultado_a = EjecutarCarga(
        CompradorIngenuo(), n
    )

    resultado_b = EjecutarCarga(
        CompradorMejorado(), n
    )

    if resultado_a != resultado_b:
        print("ERROR: las utilidades son diferentes")
        return None

    tiempos_a = []
    tiempos_b = []

    print("Utilidad verificada:", resultado_a)

    for i in range(3):

        reloj = time.perf_counter()

        a = EjecutarCarga(
            CompradorIngenuo(), n
        )

        tiempo_a = time.perf_counter() - reloj

        reloj = time.perf_counter()

        b = EjecutarCarga(
            CompradorMejorado(), n
        )

        tiempo_b = time.perf_counter() - reloj

        if a != b:
            print("ERROR: resultados diferentes")
            return None

        tiempos_a.append(tiempo_a)
        tiempos_b.append(tiempo_b)

        print(
            f"Corrida {i + 1}: "
            f"Ingenuo={tiempo_a:.6f}s | "
            f"Mejorado={tiempo_b:.6f}s"
        )

    promedio_a = sum(tiempos_a) / 3
    promedio_b = sum(tiempos_b) / 3

    print("Promedio ingenuo:", round(promedio_a, 6), "s")
    print("Promedio mejorado:", round(promedio_b, 6), "s")

    return promedio_a, promedio_b, resultado_a


# ==========================================
# PRUEBA CON 1000 UTILES
# ==========================================

def PruebaGrande():

    print("\n================================")
    print("PRUEBA CON 1000 UTILES")
    print("================================")

    reloj = time.perf_counter()

    utilidad = EjecutarCargaConPresupuesto(
        CompradorMejorado(),
        1000,
        10000
    )

    tiempo = time.perf_counter() - reloj

    print("Cantidad de utiles: 1000")
    print("Presupuesto: 10000 Bs")
    print("Utilidad obtenida:", utilidad)
    print("Tiempo:", round(tiempo, 6), "segundos")


# ==========================================
# PROGRAMA PRINCIPAL
# ==========================================

def Main():

    print("=" * 55)
    print("EVALUACION INTEGRADORA - VARIANTE B")
    print("COMPRAS DE UNA ESCUELA")
    print("=" * 55)

    print("\nPRUEBAS DE FUNCIONAMIENTO")

    Probar(
        "CompradorIngenuo",
        CompradorIngenuo
    )

    Probar(
        "CompradorMejorado",
        CompradorMejorado
    )

    # Cuatro tamaños de medición
    tamanos = [14, 16, 18, 20]

    resultados = []

    print("\nRESULTADOS DE LAS MEDICIONES")

    for n in tamanos:

        resultado = Medir(n)

        if resultado is not None:
            resultados.append((n, resultado))

    # Mostrar tabla de promedios y cocientes
    print("\n================================")
    print("TABLA FINAL DE MEDICIONES")
    print("================================")

    anterior_a = None
    anterior_b = None

    for n, datos in resultados:

        promedio_a, promedio_b, utilidad = datos

        if anterior_a is None:
            factor_a = "-"
            factor_b = "-"
        else:
            factor_a = round(promedio_a / anterior_a, 2)
            factor_b = round(promedio_b / anterior_b, 2)

        print(
            f"n={n} | "
            f"Ingenuo={promedio_a:.6f}s | "
            f"Mejorado={promedio_b:.6f}s | "
            f"Utilidad={utilidad} | "
            f"Factor ingenuo={factor_a} | "
            f"Factor mejorado={factor_b}"
        )

        anterior_a = promedio_a
        anterior_b = promedio_b

    # Prueba grande
    PruebaGrande()

    print("\n================================")
    print("PROGRAMA FINALIZADO")
    print("================================")


if __name__ == "__main__":
    Main()
