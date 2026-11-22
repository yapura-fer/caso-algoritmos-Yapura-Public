
# ESTRUCTURA DE DATOS – TIENDA DXN

## 1. Estructuras elegidas

Para optimizar el registro de ventas y el control de inventario de la tienda DXN se comparan dos estructuras de datos.

### 1.1. Solución ingenua: lista desordenada

Se utiliza una lista que almacena los productos sin un orden específico.

Para buscar un producto, el sistema debe recorrer los elementos uno por uno hasta encontrar el código solicitado.

Esta estructura es sencilla y permite registrar productos fácilmente, pero las búsquedas pueden tardar más cuando aumenta la cantidad de productos.

### 1.2. Solución mejorada: diccionario (dict)

Se utiliza un diccionario de Python, donde el código del producto funciona como clave y los datos del producto como valor.

Esta estructura permite localizar un producto directamente mediante su código, con un costo promedio O(1).

También facilita actualizar las cantidades disponibles después de cada venta.

## 2. Tabla de complejidad

| Operación | Lista desordenada | Diccionario |
|---|---|---|
| Buscar por clave | O(n) | O(1) promedio |
| Insertar | O(1) al final | O(1) promedio |
| Borrar por clave | O(n) | O(1) promedio |
| Encontrar el menor | O(n) | O(n) |
| Encontrar el siguiente | O(n log n) | O(n log n) |
| Buscar un rango | O(n log n) | O(n log n) |
| Recorrer en orden | O(n log n) | O(n log n) |
| Actualizar existencias | O(n) incluyendo búsqueda | O(1) promedio incluyendo búsqueda |

Nota: Para encontrar el siguiente, buscar un rango y recorrer en orden se considera ordenar los códigos antes de realizar la consulta. Por eso se utiliza O(n log n).

## 3. Justificación de la elección

Se elige el diccionario porque la tienda DXN necesita buscar productos constantemente durante el registro de ventas.

Con una lista desordenada, el sistema debe revisar los productos uno por uno para encontrar el código solicitado.

En cambio, con un diccionario, la búsqueda tiene un costo promedio O(1), lo que permite localizar directamente el producto.

Aunque ambas estructuras pueden realizar las operaciones de inventario, el diccionario es más conveniente para las búsquedas y actualizaciones frecuentes.

Las operaciones que necesitan ordenamiento se pueden realizar ordenando temporalmente los códigos cuando sea necesario.

## 4. Conclusión

El diccionario es la estructura más adecuada para este caso porque permite realizar búsquedas y actualizaciones de existencias de manera rápida.

Esto ayuda a optimizar el registro de ventas, reducir el tiempo de trabajo y mejorar el control de inventario de la tienda DXN.
