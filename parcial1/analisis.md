Fernando Yapura Ignacio
# PARCIAL 1 - VARIANTE B
## P1.1 - Análisis de complejidad
### a) Análisis de los fragmentos
**F1:**
- Complejidad: O(n).
- Justificación: Recorre los n elementos una sola vez y realiza una comparación por elemento.
**F2:**
- Complejidad: O(n²).
- Justificación: Tiene dos ciclos anidados que recorren los elementos de la lista.
**F3:**
- Complejidad: O(log n).
- Justificación: En cada repetición, k se multiplica por 2, por lo que crece de forma exponencial.
**F4:**
- Complejidad: O(n log n).
- Justificación: El ciclo externo se ejecuta n veces y el interno divide k entre 3 hasta llegar a 1.
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

