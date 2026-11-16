import time
import random
def hay_comprobantes_repetidos_por_pares(comprobantes):
    """Busca repetidos comparando cada par de elementos."""
    for i in range(len(comprobantes)):
        for j in range(i + 1, len(comprobantes)):
            if comprobantes[i] == comprobantes[j]:
                return True
    return False
def hay_comprobantes_repetidos_curado(comprobantes):
    """Trabaja sobre una copia para no modificar la lista original."""
    copia = comprobantes.copy()
    copia.sort()

    for i in range(len(copia) - 1):
        if copia[i] == copia[i + 1]:
            return True
    return False
def generar_sin_repetidos(n, semilla=77):
    datos = list(range(1000, 1000 + n))
    azar = random.Random(semilla)
    azar.shuffle(datos)
    return datos
def probar_casos():
    casos = [
        ([1010, 1003, 1009, 1003, 1005], True, "Repetido en el medio"),
        ([1010, 1003, 1009, 1004, 1005], False, "Sin repetidos"),
        ([], False, "Lista vacía"),
        ([1008], False, "Un solo elemento"),
        ([1004, 1001, 1002, 1006, 1004], True, "Repetido en los extremos")
    ]
    for datos, esperado, descripcion in casos:
        resultado = hay_comprobantes_repetidos_curado(datos)
        print(descripcion, "| Esperado:", esperado,
              "| Resultado:", resultado)
if __name__ == "__main__":
    probar_casos()
