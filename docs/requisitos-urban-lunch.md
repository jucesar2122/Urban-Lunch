# Requisitos para la aplicación móvil Urban.Lunch

Urban.Lunch es una aplicación para personalizar comidas de negocios de diferentes restaurantes de la ciudad.

A la gente le gustan diferentes tipos de comida, pero los restaurantes suelen ofrecer un solo tipo de gastronomía; por lo tanto, las comidas de negocios que se piden en estos restaurantes pueden resultar monótonas. Nuestra aplicación podrá proporcionar una variedad de alimentos en una comida de negocios, así que puedes combinar gazpacho, sushi y mousse de mango con chía en un solo pedido. Todo esto se puede hacer con solo unos pocos clics, y el pedido completo estará disponible en una cómoda ubicación.

El proceso es lo más sencillo posible:
1. El usuario selecciona el punto de recogida.
2. Selecciona platillos de la lista.
3. Confirma el pedido.

Posteriormente, las partes individuales del pedido se envían a los restaurantes para que las cocinen, y nuestros repartidores preparan estos pedidos para el punto de recogida y los empaquetan cuidadosamente. Cuando el pedido está listo para ser recogido, el cliente llega al punto de recogida, paga y recibe el pedido.

*Diseños de aplicaciones en Figma.*

---

## 1. Selección del punto de recogida

Esta pantalla se muestra por defecto si el usuario no tiene un pedido realizado.

La pantalla consta de un mapa con restaurantes marcados, una lista desplegable y un pie de página.

* **Mapa:** El mapa muestra los puntos de recogida de pedidos. Ninguno de los puntos de recogida está seleccionado de forma predeterminada. Cuando tocas el punto de recogida, está en negro y se considera seleccionado. Un toque repetido en el punto de recogida cancela la selección. Tocar el punto de recogida cuando se selecciona otro punto de recogida cambia la selección al nuevo punto de recogida. Después de seleccionar un punto de recogida, se muestra su nombre en el pie de página.
* **Lista desplegable:** La lista desplegable contiene una lista de puntos de recogida; cuando seleccionas un elemento de la lista, este se selecciona en el mapa y se considera seleccionado.
* **Pie de página:** El pie de página muestra el progreso del pedido. Ahora el progreso está en el nivel 1. El botón **Siguiente** (círculo gris oscuro con una flecha blanca a la derecha) está inactivo si no se selecciona ningún punto de recogida. Después de seleccionar el elemento, el botón se activa. Tocar el botón Siguiente te llevará a la pantalla de selección de platillos.

---

## 2. Elección de platillos

### Lista de platillos
La pantalla consta de una lista de platillos y un pie de página.

* **Lista de platillos:** Es una lista donde cada elemento contiene el nombre del platillo, los botones `+` y `−`, un contador y una flecha. Tocar en cualquier área de la lista, excepto `+` o `−`, te lleva a la pantalla de detalles del platillo. Al hacer clic en `+`, el platillo se agrega a la lista de pedidos desde el restaurante más cercano hasta el punto de recogida. Cuando hagas clic en el botón `−`, se eliminará un elemento de la lista del pedido.
* **Pie de página:** El progreso del pedido se muestra en el pie de página; el primer paso se marca como completado (en color) y el segundo paso se marca como en curso. En el pie de página también se encuentra el botón **Siguiente**. El botón **Siguiente** está inactivo si no hay platillos en la lista de pedidos.

### Detalles del platillo
Se puede acceder a esta pantalla desde la pantalla de lista de alimentos.

La pantalla consta de una descripción del platillo, el nombre del restaurante y un pie de página.

* **Descripción del platillo:** Consta de una foto, una descripción general, la composición del platillo y el restaurante donde está disponible. A la izquierda del nombre de un platillo hay una flecha para regresar a la lista de platillos.
* **Acciones:** Al tocar el `+`, el platillo se agrega a la lista de pedidos.
* **Pie de página:** El progreso del pedido se muestra en el pie de página; el primer paso se marca como completado (en color) y el segundo paso se marca como en curso. El botón **Siguiente** se encuentra inactivo si no hay platillos en la lista de pedidos.

---

## 3. Confirmación del pedido

La pantalla consta del nombre del punto de recogida y el botón "Atrás", la lista de platillos, el importe total, el tiempo estimado de entrega en el punto de recogida y el pie de página.

* **Parte superior:** Puedes ver el nombre del punto de recogida.
* **Lista de platillos:** Es solo una lista de sus nombres y el número de cada uno (si es más de 1); no contiene ninguna otra información sobre el platillo. Si la lista es demasiado larga, puedes desplazarte por ella.
* **Importe total:** Contiene el precio de todos los platillos preparados y la entrega.
* **Pie de página:** El progreso del pedido se muestra en el pie de página; el primer y segundo paso se marcan como completados (en color) y el tercer paso se marca como en curso. También hay un botón **Pedir** en el pie de página. Un toque en el botón **Pedir** lleva al usuario a la pantalla de seguimiento de pedidos.

---

## 4. Pantalla de seguimiento de pedidos. Recogida de pedidos

Para acceder a la pantalla de recogida de pedidos hay que pulsar el botón **Pedir** al confirmar el pedido.

La pantalla consta de un mapa, lista de platillos, importe total, dirección y temporizador. En la versión de prueba de la aplicación, el temporizador siempre está configurado en 15 segundos.

* **Mapa:** Muestra el punto de recogida desde el que puedes recoger tu pedido, los restaurantes donde se preparan los platillos y las rutas desde los restaurantes hasta el punto de recogida, mostrando el costo de todos los platillos pedidos en el restaurante, el tiempo de preparación restante y el tiempo de entrega desde el restaurante hasta el punto de recogida. Cuando los platillos se entregan desde el restaurante hasta el punto de recogida, el punto de ese restaurante y la ruta desde este hasta el punto de recogida desaparecen del mapa.
* **Lista:** Muestra los platillos con los restaurantes desde donde se envían. La lista es informativa y al hacer clic en ella no sucede nada. Cuando el platillo se entrega en el punto de recogida, aparece una marca de verificación de color verde a la izquierda del mismo, lo que indica que el platillo está listo. Si hay muchos elementos en la lista y no caben en la pantalla, puedes desplazarte por la lista.
* **Importe total:** Es el costo final de todos los platillos.
* **Temporizador:** Muestra el tiempo que queda hasta que se recoja el pedido. Una vez entregados todos los platillos, el temporizador debe estar en cero; en ese momento se produce la transición a la pantalla "El pedido ha sido enviado".

---

## 5. El pedido ha sido enviado

El cambio a la pantalla "El pedido ha sido enviado" se hace de manera automática cuando el temporizador expira.

La pantalla consta de un mapa, una notificación y el botón **Recibí el pedido**.

* **Mapa:** Muestra el punto en el mapa donde se encuentra el punto de recogida deseado.
* **Notificación:** Muestra un texto grande que indica que se puede recoger el pedido, la dirección del punto de recogida y una advertencia de que se debe recoger el pedido antes de que se enfríe.
* **Botón "Recibí el pedido":** Se encuentra debajo de la notificación. Después de hacer clic en este botón, el pedido se considera completado, se lleva al usuario a la página de feedback y luego a seleccionar un punto de recogida para crear un nuevo pedido.

### Notificaciones de error
* Si no permites que la aplicación acceda a la geolocalización, aparece un mensaje de error.
* Si intentas hacer un pedido sin agregar ningún platillo, aparece un mensaje de error.

---

## Cálculo de tiempo y costo

### Tiempo de preparación

| # | Nombre | En qué restaurante | Tiempo de preparación, minutos |
| :-: | :--- | :--- | :-: |
| 1 | Sopa de tomate con crutones | The Aroma Lane | 20 |
| 2 | Rollo de sushi California con salmón | The Nomad | 15 |
| 3 | Budín de chía con mango | Enigma | 5 |
| 4 | Pasta alfredo con pollo | Splash | 25 |
| 5 | Sopa Tom Yum | The Nomad | 40 |
| 6 | Wrap de pollo a la parrilla | After Dark | 15 |
| 7 | Ñoquis con espinacas y parmesano | The Depot | 25 |
| 8 | Batatas fritas | Glasshouse | 10 |
| 9 | Ensalada de atún | Splash | 20 |
| 10 | Pastel de ciruela | Mirrors | 5 |
| 11 | Bocaditos de coliflor | Splash | 15 |
| 12 | Hamburguesa vegana de remolacha | Enigma | 25 |
| 13 | Brownie de chocolate | The Aroma Lane | 5 |
| 14 | Palitos de pan de ajo | After Dark | 5 |
| 15 | Jugo de naranja | The Depot | 5 |
| 16 | Lasaña de carne | Glasshouse | 45 |
| 17 | Batido de arándanos, frambuesas y semillas de chía | The Nomad | 10 |

### Tiempos de preparación y entrega de todos los platillos de un restaurante en particular

$$\text{Tiempo de entrega} = \text{tiempo máximo de preparación desde el pedido} + \text{tiempo de entrega desde el restaurante hasta el punto de recogida}$$

*Ejemplo:* Si en el restaurante se pidieron dos platillos con un tiempo de preparación de 10 y 40 minutos como parte del pedido actual, y el tiempo de entrega desde el restaurante hasta el punto de recogida es de 20 minutos, entonces el tiempo total de preparación y entrega será de 60 minutos ($40 + 20 = 60$). El tiempo de entrega se calcula automáticamente.

### Tiempo de preparación del pedido

Se define como el **tiempo máximo de preparación y entrega de todos los restaurantes**.

*Ejemplo:* Si los platillos se pidieron en 3 restaurantes con un tiempo de preparación y entrega de 10, 20 y 45 minutos para todos los platillos, entonces el tiempo de preparación del pedido será de 45 minutos.

---

### Costo de los platillos

| # | Nombre | Precio, $ | En qué restaurante |
| :-: | :--- | :-: | :--- |
| 1 | Sopa de tomate con crutones | 12 | The Aroma Lane |
| 2 | Rollo de sushi California con salmón | 30 | The Nomad |
| 3 | Budín de chía con mango | 15 | Enigma |
| 4 | Pasta alfredo con pollo | 24 | Splash |
| 5 | Sopa Tom Yum | 19 | The Nomad |
| 6 | Wrap de pollo a la parrilla | 10 | After Dark |
| 7 | Ñoquis con espinacas y parmesano | 17 | The Depot |
| 8 | Batatas fritas | 12 | Glasshouse |
| 9 | Ensalada de atún | 16 | Splash |
| 10 | Pastel de ciruela | 11 | Mirrors |
| 11 | Bocaditos de coliflor | 14 | Splash |
| 12 | Hamburguesa vegana de remolacha | 25 | Enigma |
| 13 | Brownie de chocolate | 15 | The Aroma Lane |
| 14 | Palitos de pan de ajo | 7 | After Dark |
| 15 | Jugo de naranja | 5 | The Depot |
| 16 | Lasaña de carne | 30 | Glasshouse |
| 17 | Batido de arándanos, frambuesas y semillas de chía | 8 | The Nomad |

### Costo del pedido

Calculado como la suma del costo de todos los platillos pedidos.
