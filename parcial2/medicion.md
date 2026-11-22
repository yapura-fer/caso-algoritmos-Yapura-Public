Fernando Yapura Ignacio
# PARCIAL 2 - VARIANTE A
# P2.3 - MEDICIÓN DE RENDIMIENTO
## 1. Procedimiento
Para comparar los dos algoritmos utilicé el mismo sistema de turnos y la misma función EjecutarCarga.
Se realizaron tres pruebas con diferentes cantidades de pacientes, duplicando el tamaño en cada prueba:
- 4.000 pacientes.
- 8.000 pacientes.
- 16.000 pacientes.
Para cada tamaño se realizó una corrida de calentamiento y tres corridas medidas. Finalmente se calculó el promedio de los tres tiempos.
Se utilizó la función time.perf_counter() de Python para medir el tiempo de ejecución en segundos.
También se realizaron las pruebas del sistema y ambos algoritmos obtuvieron 11 de 11 pasos correctos.
## 2. Resultados de GestorIngenuo
| Pacientes | Corrida 1 | Corrida 2 | Corrida 3 | Promedio | Factor |
|---:|---:|---:|---:|---:|---:|
| 4.000 | 0.846063 | 0.829776 | 0.824799 | 0.833546 | — |
| 8.000 | 3.399015 | 3.465806 | 3.388919 | 3.417914 | 4.10 |
| 16.000 | 13.395642 | 13.759143 | 13.422423 | 13.525736 | 3.96 |

## 3. Resultados de GestorMejorado

| Pacientes | Corrida 1 | Corrida 2 | Corrida 3 | Promedio | Factor |
|---:|---:|---:|---:|---:|---:|
| 4.000 | 0.004084 | 0.004264 | 0.004040 | 0.004129 | — |
| 8.000 | 0.008752 | 0.010932 | 0.009340 | 0.009675 | 2.34 |
| 16.000 | 0.021253 | 0.018607 | 0.018390 | 0.019417 | 2.01 |
## 4. Análisis de los resultados
En las pruebas realizadas se observa una diferencia importante entre los dos algoritmos.
El GestorIngenuo pasó de 0.833546 segundos con 4.000 pacientes a 13.525736 segundos con 16.000 pacientes. Su tiempo aumentó aproximadamente cuatro veces cada vez que se duplicó la cantidad de pacientes.
El GestorMejorado pasó de 0.004129 segundos con 4.000 pacientes a 0.019417 segundos con 16.000 pacientes. Su crecimiento fue menor en comparación con el algoritmo ingenuo.
Los factores de crecimiento muestran que el GestorIngenuo tiene un comportamiento cercano a O(n²), mientras que el GestorMejorado presenta un comportamiento aproximado a O(n log n).
También se puede observar que el GestorMejorado es mucho más rápido en las tres pruebas realizadas.
## 5. Conclusión
Después de realizar las mediciones, pude comprobar que el GestorMejorado tiene un mejor rendimiento que el GestorIngenuo.
La solución ingenua utiliza una lista simple y necesita recorrer los pacientes para encontrar al más urgente, por eso su tiempo aumenta considerablemente cuando crece la cantidad de datos.
En cambio, la solución mejorada utiliza heapq y set, permitiendo registrar, atender y consultar pacientes de manera más eficiente.
Las pequeñas variaciones entre las corridas pueden deberse al procesador y a otros procesos que se ejecutan en la computadora durante las mediciones.
Por lo tanto, concluyo que la solución mejorada es más conveniente para administrar los turnos de una clínica cuando existe una gran cantidad de pacientes.
