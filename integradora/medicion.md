# Fernando Yapura Ignacio
# MEDICIÓN DE RENDIMIENTO – EVALUACIÓN INTEGRADORA VARIANTE B
## 1. Protocolo de medición
Para comparar la solución ingenua y la solución mejorada se realizaron pruebas utilizando diferentes cantidades de útiles escolares.
Se utilizaron los siguientes parámetros:
- Tamaños de entrada: 14, 16, 18 y 20 útiles.
- Una ejecución de calentamiento.
- Tres corridas de medición para cada algoritmo.
- Se calculó el promedio de las tres corridas.
- Se verificó que ambos algoritmos obtuvieran la misma utilidad máxima.
Los tiempos fueron medidos en segundos.
## 2. Resultados de las mediciones
### Resultados para 14 útiles
| Corrida | Ingenuo | Mejorado |
|---|---:|---:|
| 1 | 0.018907 s | 0.000276 s |
| 2 | 0.020588 s | 0.000142 s |
| 3 | 0.017761 s | 0.000133 s |
| **Promedio** | **0.019086 s** | **0.000184 s** |
Utilidad obtenida por ambos algoritmos: 498.
### Resultados para 16 útiles
| Corrida | Ingenuo | Mejorado |
|---|---:|---:|
| 1 | 0.084569 s | 0.000189 s |
| 2 | 0.081572 s | 0.000185 s |
| 3 | 0.082316 s | 0.000186 s |
| **Promedio** | **0.082819 s** | **0.000187 s** |
Utilidad obtenida por ambos algoritmos: 548.
### Resultados para 18 útiles
| Corrida | Ingenuo | Mejorado |
|---|---:|---:|
| 1 | 0.386182 s | 0.000227 s |
| 2 | 0.365915 s | 0.000225 s |
| 3 | 0.367648 s | 0.000224 s |
| **Promedio** | **0.373248 s** | **0.000225 s** |
Utilidad obtenida por ambos algoritmos: 527.
### Resultados para 20 útiles
| Corrida | Ingenuo | Mejorado |
|---|---:|---:|
| 1 | 1.647989 s | 0.000264 s |
| 2 | 1.625856 s | 0.000264 s |
| 3 | 1.624594 s | 0.000259 s |
| **Promedio** | **1.632813 s** | **0.000262 s** |
Utilidad obtenida por ambos algoritmos: 542.
## 3. Tabla general de mediciones
| Útiles (n) | Promedio ingenuo | Promedio mejorado | Utilidad | Factor ingenuo | Factor mejorado |
|---:|---:|---:|---:|---:|---:|
| 14 | 0.019086 s | 0.000184 s | 498 | - | - |
| 16 | 0.082819 s | 0.000187 s | 548 | 4.34 | 1.02 |
| 18 | 0.373248 s | 0.000225 s | 527 | 4.51 | 1.21 |
| 20 | 1.632813 s | 0.000262 s | 542 | 4.37 | 1.16 |
## 4. Análisis de los factores de crecimiento
El factor de crecimiento se obtiene dividiendo el tiempo promedio del tamaño actual entre el tiempo promedio del tamaño anterior.
En la solución ingenua se observa que:
- De 14 a 16 útiles, el tiempo aumenta aproximadamente 4.34 veces.
- De 16 a 18 útiles, aumenta aproximadamente 4.51 veces.
- De 18 a 20 útiles, aumenta aproximadamente 4.37 veces.
Esto demuestra que el tiempo de ejecución crece rápidamente cuando aumenta la cantidad de útiles, debido a que se revisan todas las combinaciones posibles.
En la solución mejorada:
- De 14 a 16 útiles, el factor es 1.02.
- De 16 a 18 útiles, el factor es 1.21.
- De 18 a 20 útiles, el factor es 1.16.
El crecimiento es mucho menor porque utiliza programación dinámica y evita revisar todos los subconjuntos.
## 5. Prueba con 1000 útiles
También se realizó una prueba con una cantidad mayor de útiles para comprobar el funcionamiento de la solución mejorada.
| Dato | Resultado |
|---|---:|
| Cantidad de útiles | 1000 |
| Presupuesto | 10000 Bs |
| Utilidad obtenida | 35040 |
| Tiempo de ejecución | 0.925107 segundos |
El algoritmo mejorado logró procesar los 1000 útiles en menos de un segundo, obteniendo una utilidad de 35040.
Esto demuestra que la programación dinámica puede resolver el problema con una cantidad considerable de útiles cuando el presupuesto es manejable.
## 6. ¿Qué pasaría si el presupuesto fuera 1.000.000.000 Bs?
Si el presupuesto aumentara a 1.000.000.000 Bs, la solución mejorada tendría problemas importantes de memoria y tiempo.
Esto sucede porque la programación dinámica utilizada depende tanto de la cantidad de útiles como del presupuesto.
Con 1000 útiles, la matriz de decisiones necesitaría aproximadamente:
1000 × 1.000.000.001 bytes.
Esto representa aproximadamente 1 terabyte de memoria solamente para las decisiones, sin contar el arreglo `dp` y las demás estructuras.
Por lo tanto, no sería práctico ejecutar esta solución con ese presupuesto.
Una alternativa sería utilizar otra estrategia, como una programación dinámica basada en la suma de utilidades, si los valores de utilidad permiten hacerlo de manera eficiente. También podrían estudiarse algoritmos aproximados o técnicas de optimización para presupuestos muy grandes.
## 7. Conclusión de las mediciones
Los resultados demuestran que la solución mejorada tiene un rendimiento muy superior a la solución ingenua.
Con 20 útiles, la solución ingenua necesitó en promedio 1.632813 segundos, mientras que la solución mejorada necesitó solamente 0.000262 segundos.
Además, ambas soluciones pasaron las 8 pruebas de funcionamiento y obtuvieron las mismas utilidades máximas para cada caso de medición.
La prueba de 1000 útiles también demuestra que la solución mejorada puede trabajar con entradas grandes cuando el presupuesto no supera los límites prácticos de memoria.
En conclusión, la programación dinámica es una alternativa mucho más eficiente que la fuerza bruta para este problema, aunque su rendimiento depende del tamaño del presupuesto.
