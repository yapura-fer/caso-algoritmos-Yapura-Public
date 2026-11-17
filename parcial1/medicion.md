
Fernando Yapura Ignacio
# PARCIAL 1 - VARIANTE B
## P1.2 - Corrección y medición de algoritmos
### 1. Objetivo
Implementar una solución optimizada para detectar comprobantes repetidos y comparar su rendimiento con el algoritmo original.
### 2. Lenguaje utilizado
- Lenguaje: Python 3.13.14
- Editor: Visual Studio Code
- Sistema operativo: Windows
### 3. Resultados de las pruebas funcionales
Se ejecutó el programa mediante el comando:
python python.py
Los cinco casos de prueba obtuvieron los resultados esperados.
| Caso de prueba | Esperado | Obtenido | Estado |
|---|---|---|---|
| Repetido en el medio | True | True | Correcto |
| Sin repetidos | False | False | Correcto |
| Lista vacía | False | False | Correcto |
| Un solo elemento | False | False | Correcto |
| Repetido en los extremos | True | True | Correcto |
### 4. Evidencia de ejecución
La ejecución en Visual Studio Code mostró:
Repetido en el medio | Esperado: True | Resultado: True
Sin repetidos | Esperado: False | Resultado: False
Lista vacía | Esperado: False | Resultado: False
Un solo elemento | Esperado: False | Resultado: False
Repetido en los extremos | Esperado: True | Resultado: True
### 5. Metodología de medición
Para comparar los algoritmos se deben utilizar listas sin elementos repetidos, porque así el algoritmo original debe revisar todos los pares antes de concluir que no existen duplicados.
Se deben utilizar cuatro tamaños de entrada: n, 2n, 4n y 8n.
Para cada tamaño se realizará:
- Una ejecución de calentamiento.
- Tres ejecuciones medidas.
- Cálculo del promedio de los tiempos.
### 6. Tabla de mediciones
|Tamaño|Original (s)| Optimizado(s)| Veces original |veces optimizado
| 1000 | 0.018699 | 0.000058 | -                    |-
| 2000 | 0.075340 | 0.000192 | 4.03                 |3.28
| 4000 | 0.327910 | 0.000341 | 4.35                 |1.78
| 8000| 1.232354 | 0.000736 | 3.76                  |2.16
### 7. Conclusiones
Las pruebas funcionales demostraron que el programa obtiene los cinco resultados esperados.
El algoritmo original tiene complejidad O(n²), debido a que compara los elementos mediante dos ciclos anidados.
La solución optimizada que utiliza un conjunto tiene un costo esperado de O(n), porque permite comprobar si un elemento ya fue registrado.
Los tiempos reales de ejecución y su comparación se completarán después de realizar las mediciones.

