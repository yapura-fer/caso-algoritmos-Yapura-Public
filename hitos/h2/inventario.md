
# INVENTARIO DEL CASO – TIENDA DE PRODUCTOS DXN

## 1. Descripción del caso

El proceso que deseo optimizar es el registro y control de ventas de una tienda de productos DXN.

La tienda se dedica a la comercialización de diferentes variedades de productos de la marca DXN. Actualmente cuenta con aproximadamente 50 variedades de productos, con diferentes presentaciones, cantidades y precios.

El registro de las ventas se realiza completamente de forma manual. Diariamente se venden aproximadamente 30 productos y cada registro tarda alrededor de 5 minutos, lo que representa aproximadamente 150 minutos diarios dedicados únicamente al registro de ventas.

El control de las existencias también se realiza manualmente. Este procedimiento puede ocasionar errores en las cantidades, precios y actualización del inventario.

Por esta razón, se pretende optimizar este proceso mediante un sistema que permita registrar ventas, calcular importes y actualizar automáticamente las existencias.

## 2. Datos que maneja el sistema

Cada producto contiene los siguientes datos:

- Código del producto.
- Nombre del producto.
- Precio unitario.
- Cantidad disponible en inventario.

Cada venta contiene:

- Código del producto.
- Cantidad vendida.
- Precio unitario.
- Importe total.

El código permite identificar cada producto de manera única.

## 3. Operaciones del inventario

| Operación | Descripción |
|---|---|
| Buscar por clave | Buscar un producto mediante su código. |
| Insertar | Registrar un nuevo producto en el inventario. |
| Borrar | Eliminar un producto del inventario. |
| Encontrar el menor | Encontrar el producto con el código menor. |
| Encontrar el siguiente | Encontrar el código que sigue a otro producto. |
| Buscar un rango | Consultar productos cuyos códigos estén entre dos valores. |
| Recorrer en orden | Mostrar todos los productos ordenados por código. |
| Registrar venta | Buscar un producto, calcular el importe y descontar las existencias. |

## 4. Frecuencia de las operaciones

Las operaciones que se realizan con mayor frecuencia son:

1. Buscar productos por su código, porque se necesita identificar el producto antes de registrar una venta.
2. Registrar ventas, porque diariamente se comercializan aproximadamente 30 productos.
3. Actualizar las existencias, descontando automáticamente las cantidades vendidas.
4. Calcular el importe total de cada venta.

Las operaciones de insertar y borrar productos se realizan con menor frecuencia, porque el catálogo normalmente se mantiene estable.

Las consultas por rango y los recorridos ordenados se utilizan principalmente para revisar el inventario y realizar controles.

## 5. Problema que se desea solucionar

El control manual puede ocasionar errores en los precios, cantidades y existencias. También requiere bastante tiempo para conocer los productos disponibles y las ventas realizadas.

Por esta razón, se busca utilizar una estructura de datos que permita encontrar rápidamente los productos y actualizar sus cantidades durante el registro de ventas.

## 6. Operaciones más importantes

La operación más importante es buscar un producto por su código, porque se utiliza constantemente durante las ventas.

También es importante actualizar las existencias y calcular el importe de cada producto vendido.

Por lo tanto, se priorizará una estructura que permita realizar búsquedas rápidas y actualizar la información de los productos.
