
Fernando Yapura Ignacio
# PARCIAL 1 - VARIANTE B
## P1.3 - Elección del algoritmo
### Situación del problema
Un almacén dispone de 250.000 códigos desordenados y necesita realizar 8.000 consultas diarias para verificar si un código existe.
### Alternativa 1: Búsqueda secuencial
- Costo por consulta: O(n).
- Costo total aproximado: 8.000 × 250.000 = 2.000.000.000 comparaciones.
### Alternativa 2: Ordenamiento eficiente y búsqueda binaria
- Ordenamiento: O(n log n).
- Búsqueda binaria: O(log n) por consulta.
- Se debe considerar el costo de ordenar una sola vez y realizar después las consultas.
### Alternativa 3: Ordenamiento cuadrático y búsqueda binaria
- Ordenamiento: O(n²).
- Búsqueda binaria: O(log n) por consulta.
- El ordenamiento cuadrático resulta demasiado costoso para esta cantidad de datos.
### Elección
 indicar la alternativa elegida y justificarla con los resultados obtenidos en P1.2.
### Punto de cambio
calcular aproximadamente a partir de cuántas consultas conviene ordenar primero y después buscar.
### Evidencia
Se utilizarán las mediciones realizadas en P1.2 para justificar la elección.

