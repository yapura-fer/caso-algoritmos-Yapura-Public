Fernando Yapura Ignacio
# PARCIAL 2 - VARIANTE A
# P2.1 - ELECCIÓN DE ESTRUCTURAS
## 1. Estructuras elegidas
Para mejorar el sistema de turnos de la clínica elegí utilizar una cola de prioridad mediante heapq y un conjunto mediante set.
La cola de prioridad permite organizar a los pacientes según su urgencia. El paciente con urgencia 1 será atendido primero y el paciente con urgencia 5 al final.
Para resolver los empates se utiliza un contador de llegada. De esta manera, cuando dos pacientes tienen la misma urgencia, se atiende primero al que llegó antes.
El conjunto permite consultar rápidamente si un paciente todavía está esperando.
## 2. Tabla de operaciones
| Operación | Cantidad diaria | Estructura | Costo |
|---|---:|---|---|
| Registrar | 100.000 | Cola de prioridad | O(log n) |
| Atender siguiente | 100.000 | Cola de prioridad | O(log n) |
| EstaEsperando | 30.000 | Conjunto | O(1) promedio |
| Esperando | Según consultas | Contador de elementos | O(1) |
## 3. Comparación con la solución ingenua
Tomando como referencia 100.000 pacientes, la solución ingenua utiliza una lista simple. Para atender a cada paciente debe recorrer la lista buscando al más urgente y después eliminarlo.
Aproximadamente se realizan:
100.000 x 99.999 / 2 = 4.999.950.000 comparaciones.
En cambio, la solución mejorada utiliza una cola de prioridad. Registrar y atender tienen un costo O(log n).
Como log2(100.000) es aproximadamente 17, podemos estimar:
- Registro: 100.000 x 17 = 1.700.000 operaciones aproximadas.
- Atención: 100.000 x 17 = 1.700.000 operaciones aproximadas.
Total aproximado: 3.400.000 operaciones de niveles del heap.
Además, las 30.000 consultas de EstaEsperando utilizan un conjunto, con costo O(1) promedio por consulta.
## 4. Condición para cambiar de opinión
Cambiaría de estructura si el sistema necesitara modificar constantemente la urgencia de los pacientes que ya están esperando o consultar todos los pacientes ordenados. En ese caso consideraría utilizar un árbol ordenado u otra estructura especializada.
## 5. Conclusión
Elegí la cola de prioridad y el conjunto porque permiten organizar los turnos según la urgencia, respetar el orden de llegada y consultar rápidamente si un paciente sigue esperando.
Esta combinación reduce considerablemente el tiempo de ejecución cuando aumenta la cantidad de pacientes.
