
Fernando Yapura Ignacio
# PARCIAL 1 - VARIANTE B
## P1.3 - Elección del algoritmo
### 1. Descripción del problema
Un almacén dispone de 250.000 códigos desordenados y necesita realizar 8.000 consultas diarias para verificar si determinados códigos existen en su listado.
Se debe elegir un algoritmo que permita realizar las consultas de manera eficiente, considerando que la memoria es limitada y no se desea duplicar el listado.
### 2. Alternativa 1: Búsqueda secuencial
La búsqueda secuencial revisa los elementos uno por uno hasta encontrar el código o llegar al final del listado.
- Complejidad por consulta: O(n).
- Cantidad de códigos: 250.000.
- Consultas diarias: 8.000.
Costo aproximado en el peor caso:
250.000 × 8.000 = 2.000.000.000 comparaciones.
### 3. Alternativa 2: Ordenamiento eficiente y búsqueda binaria
Esta alternativa ordena el listado una sola vez mediante un algoritmo eficiente y después utiliza búsqueda binaria para encontrar los códigos.
- Ordenamiento: O(n log n).
- Búsqueda binaria: O(log n).
- El ordenamiento se realiza una sola vez.
Usando log₂(250.000) ≈ 17,93:
Ordenamiento aproximado:
250.000 × 17,93 ≈ 4.482.892 operaciones.
Consultas aproximadas:
8.000 × 17,93 ≈ 143.440 operaciones.
Costo total aproximado:
4.482.892 + 143.440 = 4.626.332 operaciones.
### 4. Alternativa 3: Ordenamiento cuadrático y búsqueda binaria
Esta alternativa utiliza un algoritmo de ordenamiento cuadrático y después búsqueda binaria.
- Ordenamiento: O(n²).
- Búsqueda binaria: O(log n).
Costo aproximado del ordenamiento:
250.000² / 2 = 31.250.000.000 comparaciones.
El costo del ordenamiento es demasiado elevado para esta cantidad de datos.
### 5. Comparación de alternativas
La búsqueda secuencial necesita aproximadamente 2.000 millones de comparaciones en el peor caso.
El ordenamiento eficiente seguido de búsqueda binaria necesita aproximadamente 4,63 millones de operaciones estimadas.
El ordenamiento cuadrático resulta demasiado costoso debido a su crecimiento O(n²).
### 6. Elección del algoritmo
La alternativa recomendada es utilizar un ordenamiento eficiente y búsqueda binaria.
Esta opción permite ordenar el listado una sola vez y realizar posteriormente consultas mucho más rápidas.
Para respetar la limitación de memoria, se debe utilizar un método de ordenamiento que trabaje sobre el mismo listado, sin crear una segunda copia completa.
### 7. Punto de cambio
Para comparar la búsqueda secuencial con el ordenamiento eficiente y la búsqueda binaria, se puede estimar el punto de equilibrio:
4.482.892 / (250.000 - 17,93) ≈ 18 consultas.
Esto significa que, bajo este modelo simplificado de operaciones, a partir de aproximadamente 18 consultas convendría ordenar primero y después utilizar búsqueda binaria.
### 8. Evidencia experimental
La decisión se complementará con los resultados de las mediciones realizadas en P1.2, comparando el crecimiento del algoritmo original y el optimizado.


