
# MEDICION DE RENDIMIENTO – TIENDA DXN

## 1. Objetivo

Comparar el rendimiento del registro de ventas y la actualización de existencias de una tienda DXN utilizando dos estructuras de datos: una lista desordenada y un diccionario.

El propósito es comprobar cuál de las dos estructuras permite procesar las ventas de manera más rápida cuando aumenta la cantidad de productos.

## 2. Protocolo de medición

Para realizar las pruebas se utilizó Python y la función `time.perf_counter()`.

El procedimiento fue el siguiente:

- Se probaron cuatro tamaños: 50, 100, 200 y 400 productos.
- Se generaron 20 ventas por cada producto.
- Se realizó una ejecución de calentamiento para cada estructura y tamaño.
- Se realizaron tres repeticiones por cada prueba.
- Se calculó el promedio de los tres tiempos obtenidos.
- Se midió únicamente el procesamiento de las ventas. La preparación y copia de las estructuras se realizó fuera del tiempo medido.
- Se comprobó que ambas soluciones obtuvieran el mismo importe total de ventas.

## 3. Resultados de las mediciones

| Productos | Lista (segundos) | Factor lista | Diccionario (segundos) | Factor diccionario |
|---:|---:|---:|---:|---:|
| 50 | 0.00107013 | — | 0.00018107 | — |
| 100 | 0.00388770 | 3.63x | 0.00041520 | 2.29x |
| 200 | 0.01478077 | 3.80x | 0.00069527 | 1.67x |
| 400 | 0.05564833 | 3.76x | 0.00137837 | 1.98x |

## 4. Análisis de los resultados

Los resultados muestran que la lista desordenada necesita más tiempo para procesar las ventas a medida que aumenta la cantidad de productos.

En cambio, el diccionario presenta tiempos menores porque permite buscar los productos directamente mediante su código.

En la prueba de 400 productos, la lista tardó aproximadamente 0.05564833 segundos, mientras que el diccionario tardó 0.00137837 segundos.

Esto demuestra que el diccionario tuvo un mejor rendimiento en las pruebas realizadas.

## 5. Conclusión

Los resultados muestran que el diccionario fue más rápido que la lista desordenada en los cuatro tamaños probados.

Esto se relaciona con la complejidad O(n) de la búsqueda lineal frente a O(1) promedio de la búsqueda mediante diccionario.

Al duplicar los productos, el tiempo de la lista aumentó aproximadamente entre 3.6 y 3.8 veces, mientras que el diccionario presentó un crecimiento menor.

Sin embargo, las mediciones pueden presentar ruido por el funcionamiento de la computadora y otros procesos ejecutados durante las pruebas.
