
Fernando Yapura Ignacio
# PARCIAL 1 - VARIANTE B
## P1.1 - Análisis de complejidad
### a) Análisis de los fragmentos
**F1:**
- Complejidad: O(n).
- Justificación: El ciclo recorre los n elementos una sola vez. En cada iteración comprueba si el dato es par y, si corresponde, incrementa el contador.
**F2:**
- Complejidad: O(n²).
- Justificación: Contiene dos ciclos anidados que recorren los elementos. En el peor caso se realizan aproximadamente n × n operaciones.
**F3:**
- Complejidad: O(log n).
- Justificación: La variable k comienza en 1 y se multiplica por 2 en cada iteración. Por tanto, el número de repeticiones crece de forma logarítmica.
**F4:**
- Complejidad: O(n log n).
- Justificación: El ciclo externo se ejecuta n veces. En cada repetición, el ciclo interno divide k entre 3 hasta llegar a 1, realizando O(log n) operaciones.
### b) Análisis de recurrencias
**Recurrencia 1:**
T(n) = 4T(n/3) + n
- a = 4
- b = 3
- d = 1
- b^d = 3
- Comparación: a > b^d
- Resultado: Θ(n^(log₃ 4))

**Recurrencia 2:**

T(n) = 2T(n/2) + n²

- a = 2
- b = 2
- d = 2
- b^d = 4
- Comparación: a < b^d
- Resultado: Θ(n²)


