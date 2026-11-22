# Fernando Yapura Ignacio
# PARCIAL 2 - VARIANTE A
# Sistema de turnos de una clinica
import heapq
import time
# SOLUCION INGENUA
class GestorIngenuo:
    def __init__(self):
        self.lista = []
        self.llegadas = 0
    def Registrar(self, nombre, urgencia):
        self.lista.append((urgencia, self.llegadas, nombre))
        self.llegadas += 1
    def AtenderSiguiente(self):
        if len(self.lista) == 0:
            return None
        mejor = 0
        for i in range(1, len(self.lista)):
            p = self.lista[i]
            m = self.lista[mejor]
            if p[0] < m[0] or (p[0] == m[0] and p[1] < m[1]):
                mejor = i
        paciente = self.lista.pop(mejor)
        return paciente[2]
    def EstaEsperando(self, nombre):
        for p in self.lista:
            if p[2] == nombre:
                return True
        return False
    @property
    def Esperando(self):
        return len(self.lista)
# SOLUCION MEJORADA
class GestorMejorado:
    def __init__(self):
        self.cola = []
        self.activos = set()
        self.llegadas = 0
    def Registrar(self, nombre, urgencia):
        heapq.heappush(
            self.cola,
            (urgencia, self.llegadas, nombre)
        )
        self.activos.add(nombre)
        self.llegadas += 1
    def AtenderSiguiente(self):
        if len(self.cola) == 0:
            return None
        urgencia, llegada, nombre = heapq.heappop(self.cola)
        self.activos.remove(nombre)
        return nombre
    def EstaEsperando(self, nombre):
        return nombre in self.activos
    @property
    def Esperando(self):
        return len(self.activos)
# GUION DE PRUEBAS 
Guion = [
    ("registrar", "Ana", 3, ""),
    ("registrar", "Beto", 1, ""),
    ("registrar", "Carla", 3, ""),
    ("registrar", "Diego", 2, ""),
    ("esperando", "", 0, "4"),
    ("esta", "Beto", 0, "True"),
    ("esta", "Zoe", 0, "False"),
    ("atender", "", 0, "Beto"),
    ("esta", "Beto", 0, "False"),
    ("atender", "", 0, "Diego"),
    ("registrar", "Elena", 1, ""),
    ("atender", "", 0, "Elena"),
    ("atender", "", 0, "Ana"),
    ("atender", "", 0, "Carla"),
    ("atender", "", 0, "(nadie)"),
    ("esperando", "", 0, "0")
]
def Ejecutar(g, op, arg, urg):
    if op == "registrar":
        g.Registrar(arg, urg)
        return ""
    elif op == "atender":
        return g.AtenderSiguiente() or "(nadie)"
    elif op == "esta":
        return str(g.EstaEsperando(arg))
    else:
        return str(g.Esperando)
def Probar(titulo, gestor):
    bien = 0
    total = 0
    for op, arg, urg, esperado in Guion:
        obtenido = Ejecutar(gestor, op, arg, urg)
        if op == "registrar":
            continue
        total += 1
        if obtenido == esperado:
            bien += 1
        else:
            print("MAL:", op, arg,
                  "Esperado:", esperado,
                  "Obtenido:", obtenido)
    print(titulo, ":", bien, "de", total,
          "pasos correctos")
# CARGA ORIGINAL
def EjecutarCarga(g, n):
    for i in range(n):
        urgencia = int((i * 7919) % 5) + 1
        g.Registrar("P" + str(i), urgencia)
    control = 0
    for i in range(n):
        control += len(g.AtenderSiguiente())
    return control
# MEDICION
def Medir(Gestor, n):
    # Calentamiento
    EjecutarCarga(Gestor(), n)
    tiempos = []
    # Tres corridas medidas
    for i in range(3):
        gestor = Gestor()
        inicio = time.perf_counter()
        EjecutarCarga(gestor, n)
        fin = time.perf_counter()
        tiempos.append(fin - inicio)
    promedio = sum(tiempos) / 3
    return tiempos, promedio
# COMPARACION
def Comparar():
    tamanos = [4000, 8000, 16000]
    anteriores = {
        "Ingenuo": None,
        "Mejorado": None
    }
    print("\n======================================")
    print("      MEDICION DE RENDIMIENTO")
    print("======================================")
    for n in tamanos:
        print("\nPACIENTES:", n)
        for nombre, clase in [
            ("Ingenuo", GestorIngenuo),
            ("Mejorado", GestorMejorado)
        ]:
            tiempos, promedio = Medir(clase, n)
            factor = "-"
            if anteriores[nombre] is not None:
                factor = round(
                    promedio / anteriores[nombre], 2
                )
            anteriores[nombre] = promedio
            print("\n", nombre)
            print("Corrida 1:", round(tiempos[0], 6))
            print("Corrida 2:", round(tiempos[1], 6))
            print("Corrida 3:", round(tiempos[2], 6))
            print("Promedio:", round(promedio, 6))
            print("Factor:", factor)
if __name__ == "__main__":
    print("PARCIAL 2 - VARIANTE A")
    print("SISTEMA DE TURNOS DE UNA CLINICA")
    print("\n--- PRUEBAS ---")
    Probar("GestorIngenuo", GestorIngenuo())
    Probar("GestorMejorado", GestorMejorado())
    Comparar()
