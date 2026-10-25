# Solicitud QA con evidencia

## FUENTE
- **Documento de especificación de requisitos:** `Requisitos para la aplicación móvil Urban.Lunch` (TripleTen, Páginas 1 a 9).
  - Pág. 1: Introducción y flujo general (3 pasos).
  - Pág. 2: Sección 1. Selección del punto de recogida.
  - Pág. 3: Sección 2. Elección de platillos (Lista de platillos).
  - Pág. 4: Sección 2. Elección de platillos (Detalles del platillo).
  - Pág. 5: Sección 3. Confirmación del pedido.
  - Pág. 6: Sección 4. Pantalla de seguimiento de pedidos / Recogida de pedidos.
  - Pág. 7: Sección 5. El pedido ha sido enviado / Notificaciones de error.
  - Pág. 8: Cálculo de tiempo y costo (Tiempos de preparación y entrega).
  - Pág. 9: Costo de los platillos (Tabla de precios por restaurante) y costo del pedido.
- **Resultados de ejecución:** `Lista de comprobación y resultados de la prueba para la aplicación móvil Urban.Lunch` (46 ítems ejecutados, 2 defectos reportados: TQPS6-2 y TQPS6-3).

## OBJETIVO
Validar la cobertura, trazabilidad y consistencia de la lista de comprobación de pruebas (46 ítems) frente a la especificación de requisitos de Urban.Lunch, identificando discrepancias, brechas de cobertura, diseño de pruebas de valores límite y estado de los defectos reportados, con estricto respaldo de evidencia.

## CONTEXTO
- **Producto o funcionalidad:** Aplicación móvil Urban.Lunch (flujo completo de selección de punto de recogida, selección de platillos, confirmación, seguimiento y finalización del pedido).
- **Usuario o rol:** Cliente/Usuario final de la aplicación móvil.
- **Alcance incluido:**
  - Pantalla 1: Selección de punto de recogida (mapa, lista desplegable, pie de página, progreso paso 1).
  - Pantalla 2: Elección y detalle de platillos (contadores, botones `+`/`-`, ingredientes, fotos, restaurante, progreso paso 2).
  - Pantalla 3: Confirmación de pedido (lista, cantidades, importes, progreso paso 3, botón "Pedir").
  - Pantalla 4: Seguimiento de pedido (rutas, tiempos de cocción y entrega, temporizador de 15s de prueba).
  - Pantalla 5: Pedido enviado (notificación, dirección, botón "Recibí el pedido", feedback).
  - Notificaciones de error (geolocalización denegada, pedido vacío).
  - Reglas de cálculo de costos y tiempos.
- **Fuera de alcance:** Pasarela de pago bancario real, arquitectura de backend / base de datos interna.
- **Restricciones conocidas:** En la versión de prueba, el temporizador de recogida está configurado de forma fija a 15 segundos.
- **Qué sé que NO está definido:**
  - Qué sucede si el usuario revoca los permisos de geolocalización mientras la app ya está abierta.
  - Comportamiento al perder conexión de red durante el temporizador de 15 segundos.
  - Límite máximo de platillos que se pueden agregar a través del contador `+`.

## SALIDA
Tabla estructurada con el formato:
`| Fuente (Página / Sección / Ítem) | Afirmación / Criterio Verificado | Estado / Evidencia | Clasificación | Observación / Duda QA |`

## LÍMITES Y GATE
- No presentar como hecho nada que no aparezca en la FUENTE.
- Si algo no tiene respaldo en la FUENTE, escribir estrictamente `SIN FUENTE`.
- Si se realiza una deducción lógica no explícita, etiquetarla como `INFERENCIA`.
- Para cada resultado, citar con exactitud la página del PDF o el número de ítem de la lista.
- Para criterios con límites numéricos, diseñar casos de valor límite (BVA); no limitarse a repetir el criterio.
- No tomar decisiones de alcance unilaterales; proponerlas para validación del usuario.
