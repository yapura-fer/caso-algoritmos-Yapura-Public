# C6 – Elección argumentada del algoritmo de ordenamiento

## 1. Descripción del caso

El caso de estudio corresponde a una tienda dedicada a la comercialización de productos DXN, donde se manejan aproximadamente 50 variedades de productos y se registran alrededor de 30 ventas diarias.

Actualmente, el control de ventas y existencias se realiza manualmente. Por esta razón, se necesita seleccionar un algoritmo de ordenamiento que permita organizar los datos de manera eficiente y facilitar la administración del inventario.

## 2. Algoritmos evaluados

En la práctica C5 se compararon tres algoritmos:

- **Burbuja (Bubble Sort):** es sencillo de implementar, pero tiene una complejidad temporal O(n²), por lo que puede tardar más cuando aumenta la cantidad de datos.
- **MergeSort:** utiliza la estrategia de dividir y combinar. Su complejidad es O(n log n), ofreciendo un rendimiento eficiente con cantidades grandes de información.
- **QuickSort:** utiliza un elemento pivote para dividir los datos. Su rendimiento promedio es O(n log n), aunque en el peor caso puede llegar a O(n²).

## 3. Algoritmo seleccionado

Se selecciona **QuickSort** como alternativa para ordenar los registros de productos de la tienda DXN.

La elección se fundamenta en su buen rendimiento promedio, su eficiencia para ordenar cantidades crecientes de datos y su implementación práctica para organizar información como nombres de productos, precios y cantidades disponibles.

## 4. Evidencia de la elección

La evidencia utilizada corresponde a las mediciones realizadas en la práctica C5, donde se compararon Bubble Sort, MergeSort y QuickSort con 100, 500, 1000, 2000 y 4000 datos.

Se realizaron tres repeticiones por cada tamaño y se calculó el tiempo promedio de ejecución.

**Tabla de evidencia:**

| Cantidad de datos | Bubble Sort | MergeSort | QuickSort |
|---:|---:|---:|---:|
| 100 | Pendiente | Pendiente | Pendiente |
| 500 | Pendiente | Pendiente | Pendiente |
| 1000 | Pendiente | Pendiente | Pendiente |
| 2000 | Pendiente | Pendiente | Pendiente |
| 4000 | Pendiente | Pendiente | Pendiente |

Los tiempos se completarán con los resultados reales obtenidos en la práctica C5. No se deben utilizar valores inventados.

## 5. Justificación

QuickSort es una alternativa adecuada porque permite ordenar grandes cantidades de datos con un rendimiento promedio de O(n log n). Esto puede ayudar a organizar los productos de la tienda por nombre, precio o cantidad disponible.

Además, evita utilizar un algoritmo cuadrático como Bubble Sort cuando el volumen de información aumenta.

## 6. Conclusión

La selección de QuickSort se fundamenta en su eficiencia promedio y en su capacidad para ordenar datos de manera rápida. Su utilización puede contribuir a mejorar la organización del inventario y facilitar la consulta de productos en la tienda DXN.

La elección definitiva debe respaldarse con los tiempos reales obtenidos en la práctica C5, verificando si QuickSort fue efectivamente más rápido que MergeSort en las pruebas realizadas.
