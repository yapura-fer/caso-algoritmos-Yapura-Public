# PRACTICA C5: TORNEO DE ORDENAMIENTOS

**Proyecto:** Optimización de la tienda de productos DXN  
**Lenguaje:** Python  
**Algoritmos comparados:** Burbuja, MergeSort y QuickSort.

## 1. Objetivo

Comparar el rendimiento de tres algoritmos de ordenamiento utilizando diferentes cantidades de datos para identificar cuál ofrece un mejor tiempo de ejecución.

## 2. Descripción de los algoritmos

- **Burbuja:** compara elementos consecutivos e intercambia sus posiciones cuando están desordenados. Su complejidad es O(n²).
- **MergeSort:** divide los datos en partes pequeñas, las ordena y luego las combina. Su complejidad es O(n log n).
- **QuickSort:** selecciona un pivote y organiza los elementos menores y mayores a su alrededor. Su rendimiento promedio es O(n log n).

## 3. Protocolo de medición

1. Se prepararon conjuntos de 100, 500, 1.000, 2.000 y 4.000 datos.
2. Se utilizó el mismo conjunto de datos para los tres algoritmos en cada tamaño.
3. Se realizaron tres ejecuciones de calentamiento.
4. Se midió el tiempo de ejecución de cada algoritmo.
5. Se realizaron tres repeticiones por algoritmo y tamaño.
6. Se calculó el promedio de los tiempos obtenidos.
7. Se verificó que los tres algoritmos produjeran resultados ordenados correctamente.

## 4. Tabla de resultados

Completar con los resultados obtenidos al ejecutar el programa `torneo.py`.

| Cantidad de datos | Burbuja (s) | MergeSort (s) | QuickSort (s) |
|---:|---:|---:|---:|
| 100 | Pendiente | Pendiente | Pendiente |
| 500 | Pendiente | Pendiente | Pendiente |
| 1.000 | Pendiente | Pendiente | Pendiente |
| 2.000 | Pendiente | Pendiente | Pendiente |
| 4.000 | Pendiente | Pendiente | Pendiente |

## 5. Análisis de resultados

Los resultados permiten observar cómo cambia el tiempo de ejecución cuando aumenta la cantidad de datos.

La búsqueda y organización de información en una tienda requiere algoritmos eficientes, especialmente cuando se incrementa el número de registros.

## 6. Conclusiones

El algoritmo Burbuja es sencillo de implementar, pero su tiempo de ejecución aumenta considerablemente cuando crece la cantidad de datos.

MergeSort y QuickSort ofrecen un mejor rendimiento promedio para conjuntos de datos grandes, porque utilizan estrategias más eficientes de ordenamiento.

Para mi tienda DXN, considero conveniente utilizar MergeSort o QuickSort para organizar grandes cantidades de registros de ventas y productos, evitando demoras innecesarias.

## 7. Aplicación en la tienda DXN

Esta práctica permitirá identificar qué algoritmo resulta más conveniente para organizar información de productos, cantidades disponibles y registros de ventas, contribuyendo a mejorar la administración de la tienda.
