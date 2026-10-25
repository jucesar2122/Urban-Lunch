# Lista de comprobación y resultados de la prueba para la aplicación móvil Urban.Lunch

| # | Descripción | Estado | Enlace al informe de errores |
| :-: | :--- | :---: | :--- |
| 1 | El mapa muestra los puntos de recogida. | APROBADO | |
| 2 | Verificar que la pantalla de selección de punto de recogida se abre al iniciar la aplicación sin pedidos activos. | APROBADO | |
| 3 | El mapa muestra el punto de ubicación del usuario. | APROBADO | |
| 4 | Verificar que al tocar un punto de recogida este cambie a color negro. | APROBADO | |
| 5 | Verificar que al tocar el mismo punto este se deselecciona. | APROBADO | |
| 6 | Verificar que al seleccionar otro punto cambia la selección al nuevo punto. | APROBADO | |
| 7 | Verificar que el nombre del punto selecionado aparece en el pie de página. | APROBADO | |
| 8 | Verificar que el botón Siguiente permanece deshabitado sin selección. | APROBADO | |
| 9 | Verificar que el botón Siguiente se habilita tras seleccionar un punto. | APROBADO | |
| 10 | Verificar que el botón Siguiente abre la pantalla de selección de platillos. | APROBADO | |
| 11 | Verificar que seleccionar un punto desde la lista desplegable también lo selecciona en el mapa. | APROBADO | |
| 12 | Verificar que la lista desplegable refleja correctamente el punto seleccionado desde el mapa. | APROBADO | |
| 13 | Verificar que el indicador de progreso muestra el paso 1 como activó. | APROBADO | |
| 14 | Verificar que inicialmente ningún punto aparece seleccionado. | APROBADO | |
| 15 | Verificar que en cada elemento de la lista muestra el nombre del platillo. | APROBADO | |
| 16 | Verificar que en cada elemento de la lista se encuentran los botones "+" y "−". | APROBADO | |
| 17 | Verificar que cada elemento de la lista tiene un contador para realizar pedido. | APROBADO | |
| 18 | Verificar que el botón Siguiente está inactivo si no hay platillos seleccionados en el pedido. | APROBADO | |
| 19 | Verificar que el nombre del restaurante se muestra debajo de los ingredientes, asi como el costo y tiempo de elaboraciòn. | APROBADO | |
| 20 | Verificar que la pantalla muestra en la foto, descripción e ingredientes del platillo. | APROBADO | |
| 21 | Verificar que con la flecha se vuelve a la lista de platillos. | APROBADO | |
| 22 | Verificar que en el importe total se incluye el precio de todos los platillos. | APROBADO | |
| 23 | Verificar que la lista muestra los nombres de los platillos y las cantidades del pedido. | APROBADO | |
| 24 | Verificar que en el importe total se incluye el costo de entrega. | APROBADO | |
| 25 | Verificar que en el mapa se muestran los restaurantes donde se preparan los platillos. | APROBADO | |
| 26 | Verificar que al tocar el botòn "Pedir" se abre la pantalla de seguimiento. | APROBADO | |
| 27 | Verificar que en el mapa se muestra el punto de recogida. | APROBADO | |
| 28 | Verificar que se muestran los costos de los platillos pedidos por restaurante. | APROBADO | |
| 29 | Verificar que en el mapa se muestran las rutas desde los restaurantes al punto de recogida. | APROBADO | |
| 30 | Verificar que se muestra el tiempo de cocción restante de cada restaurante. | APROBADO | *Es de hacer notar que al ser una App de prueba el contador de tiempo esta configurado para 15 segundos.* |
| 31 | Verificar que al tocar el botón "Recibí el pedido" se muestra la barra de feedback. | APROBADO | |
| 32 | Verificar que se muestra el tiempo de entrega de cada restaurante. | APROBADO | |
| 33 | Verificar la notificación que indica si el pedido puede recogerse. | APROBADO | |
| 34 | Verificar que el temporizador muestra el tiempo restante hasta la recogida. | APROBADO | |
| 35 | Verificar que en el mapa se muestre el punto de recogida deseado. | APROBADO | |
| 36 | Verificar que la transición a "Pedido enviado" ocurre automáticamente al expirar el temporizador. | APROBADO | |
| 37 | Verificar que al tocar en cualquier área del elemento se abre la pantalla de detalles (excepto "+" y "−"). | APROBADO | |
| 38 | Verificar que al tocar "−" se elimina un platillo de la lista del pedido. | APROBADO | |
| 39 | Verificar que el progreso del pedido se muestra en el pie de página. | APROBADO | |
| 40 | Verificar que al tocar el botón "Pedir" lleve al usuario a la pantalla de seguimiento de pedidos. | APROBADO | |
| 41 | Verificar si en la pantalla aparece la notificación "El pedido ha sido enviado". | APROBADO | |
| 42 | Verificar si el usuario intenta hacer un pedido sin agregar ningún platillo, aparezca un mensaje de error. | APROBADO | |
| 43 | Verificar si el usuario no permite que la aplicación acceda a la geolocalización, aparezca un mensaje de error. | **NO APROBADO** | https://juliodelamar101010.atlassian.net/browse/TQPS6-3 |
| 44 | Verificar si el usuario intenta hacer un pedido sin agregar ningún platillo, aparezca un mensaje de error. | APROBADO | |
| 45 | Verificar que en el seguimiento de pedido este la dirección correcta del restaurante. | APROBADO | |
| 46 | Verificar que los precios de los platillos sean correctos para pedidos de uno o multiples restaurantes. | **NO APROBADO** | https://juliodelamar101010.atlassian.net/browse/TQPS6-2 |

---

## Conclusiones y Recomendaciones de la Prueba

* La funcionalidad de selección del punto de recogida presenta un estado de prueba mayoritariamente satisfactorio. La mayor parte de los requisitos funcionales se cumplen correctamente y el flujo principal permite al usuario seleccionar un punto de recogida y continuar con el proceso de pedido.
* Una vez aplicada la corrección, se recomienda realizar una prueba de regresión sobre esta funcionalidad para confirmar que el defecto ha sido resuelto y que el resto del comportamiento continúa funcionando correctamente.
* No obstante, se identificó que hay un problema con la geolocalizacion y precios de algunos platillos. Aunque este problema no impide continuar con el flujo de la aplicación, afecta al cumplimiento de los requisitos y a la experiencia del usuario, por lo que se recomienda corregirlo antes de la siguiente versión.
