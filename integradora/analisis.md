# Fernando Yapura Ignacio
# ANÁLISIS DEL PROBLEMA – EVALUACIÓN INTEGRADORA VARIANTE B
## 1. Análisis de la solución ingenua
La solución ingenua utiliza la fuerza bruta para encontrar la mejor combinación de útiles escolares. Para ello, genera y revisa todos los subconjuntos posibles de útiles, comprobando cuáles no superan el presupuesto y calculando su utilidad.
Si existen n útiles, se deben revisar 2^n combinaciones. Además, para cada combinación se recorren los útiles para calcular su costo y utilidad.
**Complejidad temporal:**
O(n × 2^n)
**Complejidad espacial:**
O(n), considerando las estructuras auxiliares utilizadas.
Esta solución encuentra la respuesta correcta, pero se vuelve muy lenta cuando aumenta la cantidad de útiles.
## 2. Análisis de la recurrencia
La cantidad de subconjuntos se duplica cada vez que se agrega un nuevo útil.
La recurrencia para contar las combinaciones es:
T(n) = 2T(n - 1) + 1
Al desarrollar la recurrencia se obtiene un crecimiento exponencial:
T(n) = O(2^n)
El teorema maestro clásico no se aplica directamente a esta recurrencia porque su forma utiliza subproblemas de tamaño n/b, mientras que aquí se utiliza n - 1.
Por esta razón, se resuelve mediante el desarrollo de la recurrencia.
## 3. Por qué no funciona correctamente el método voraz
El método voraz selecciona primero el útil que parece ofrecer la mejor utilidad en relación con su costo. Sin embargo, esta decisión no garantiza encontrar la combinación óptima.
Ejemplo:
| Útil | Costo | Utilidad | Utilidad/costo |
|---|---:|---:|---:|
| U1 | 20 Bs | 120 | 6 |
| U2 | 40 Bs | 200 | 5 |
| U3 | 60 Bs | 240 | 4 |
Presupuesto disponible: 100 Bs.
El método voraz seleccionaría U1 y U2 porque tienen una mejor relación de utilidad y costo. Su resultado sería:
- Costo total: 60 Bs.
- Utilidad total: 320.
Sin embargo, la combinación U2 y U3 obtiene:
- Costo total: 100 Bs.
- Utilidad total: 440.
Por lo tanto, el método voraz no encuentra la mejor solución en este caso.
## 4. Estrategia de solución mejorada
Para resolver el problema se utilizó la programación dinámica, mediante el algoritmo de mochila 0/1.
Esta estrategia calcula las mejores utilidades posibles para diferentes cantidades de presupuesto, evitando repetir cálculos innecesarios.
Se utiliza un arreglo `dp`, donde se guarda la mejor utilidad que se puede conseguir con cada presupuesto.
La fórmula principal es:
`dp[b] = max(dp[b], dp[b - costo] + utilidad)`
El recorrido del presupuesto se realiza de mayor a menor para evitar que un mismo útil sea seleccionado más de una vez.
También se utiliza una matriz de decisiones para reconstruir los útiles seleccionados al finalizar el cálculo.
**Complejidad temporal:**
O(n × B), donde n es la cantidad de útiles y B es el presupuesto.
**Complejidad espacial:**
O(n × B), debido a la matriz de decisiones, además del arreglo de programación dinámica.
Esta solución es mucho más eficiente que la fuerza bruta cuando el presupuesto no es demasiado grande.
## 5. Mejora de la consulta EstaEnLaCompra
En la solución ingenua se utiliza una lista para guardar los códigos seleccionados. Para comprobar si un código está en la compra, se debe recorrer la lista hasta encontrarlo.
Su complejidad es O(n).
En la solución mejorada se utiliza un conjunto (`set`) de Python. Esta estructura permite consultar si un código existe de manera mucho más rápida.
Su complejidad promedio de búsqueda es O(1).
Por esta razón, el uso de `set` mejora las consultas repetidas de pertenencia.
## 6. Conclusión del análisis
La solución ingenua permite encontrar la respuesta correcta, pero su tiempo de ejecución aumenta rápidamente debido a que revisa todas las combinaciones posibles.
La programación dinámica permite resolver el problema de manera más eficiente, mientras que el conjunto `set` mejora las consultas de pertenencia.
Las pruebas y mediciones realizadas permiten comprobar que la solución mejorada funciona correctamente y presenta un rendimiento superior.
