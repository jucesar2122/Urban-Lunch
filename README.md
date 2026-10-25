# Urban.Lunch — QA Testing & Documentación de la Aplicación Móvil

Bienvenido al repositorio del proyecto de aseguramiento de calidad (QA) para la aplicación móvil **Urban.Lunch**. Este repositorio contiene la especificación de requisitos, la lista de comprobación de pruebas ejecutadas, los reportes de defectos y la plantilla de solicitud QA con evidencia.

---

## 📱 Acerca de Urban.Lunch

**Urban.Lunch** es una aplicación móvil diseñada para personalizar comidas de negocios combinando platillos de diferentes restaurantes de la ciudad en un único pedido con entrega coordinada en un punto de recogida seleccionado.

### Flujo principal de la aplicación (3 pasos):
1. **Selección del punto de recogida:** El usuario selecciona en el mapa o mediante una lista desplegable el punto donde retirará su comida.
2. **Elección de platillos:** Selección de platillos desde diversos restaurantes con información de ingredientes, tiempos y costos.
3. **Confirmación del pedido:** Resumen detallado con cantidades, desglose y confirmación.
4. **Seguimiento y recogida:** Pantalla con temporizador en cuenta regresiva, mapas de ruta por restaurante y aviso de pedido listo para retirar.

---

## 📁 Estructura del Repositorio

Toda la documentación técnica y de pruebas se encuentra organizada dentro de la carpeta [`docs/`](./docs):

```text
├── docs/
│   ├── prompt-template.md            # Plantilla estandarizada de "Solicitud QA con evidencia"
│   ├── requisitos-urban-lunch.md     # Especificación completa de requisitos funcionales y de negocio
│   └── casos-de-prueba-urban-lunch.md # Lista de comprobación y resultados de los 46 casos de prueba
└── README.md                         # Portada y descripción general del proyecto
```

### Enlaces directos a la documentación:
* 📄 [**Requisitos de Urban.Lunch**](docs/requisitos-urban-lunch.md): Detalla los flujos de pantallas (1 a 5), notificaciones de error y las fórmulas para el cálculo de tiempos y costos.
* 🧪 [**Casos de Prueba y Resultados**](docs/casos-de-prueba-urban-lunch.md): Matriz de 46 pruebas ejecutadas que incluye estados de aprobación y notas de prueba.
* 📋 [**Solicitud QA con Evidencia**](docs/prompt-template.md): Estructura con FUENTE, OBJETIVO, CONTEXTO, SALIDA y LÍMITES Y GATE para auditoría de calidad con IA.

---

## 📊 Resumen de Resultados de Pruebas QA

Durante el ciclo de pruebas funcionales sobre la versión de prueba móvil de Urban.Lunch, se obtuvieron las siguientes métricas:

| Métrica | Cantidad | Porcentaje |
| :--- | :---: | :---: |
| **Total de casos ejecutados** | **46** | 100% |
| **Casos Aprobados** | **44** | 95.65% |
| **Casos No Aprobados (Defectos)** | **2** | 4.35% |

### 🐛 Defectos Identificados y Reportados

1. **[TQPS6-2](https://juliodelamar101010.atlassian.net/browse/TQPS6-2) — Error en el cálculo de precios para pedidos combinados:**
   * **Descripción:** Los precios finales de los platillos no se calculan de manera correcta al realizar pedidos que incluyen uno o múltiples restaurantes.
   * **Impacto:** Integridad financiera y discrepancia en el cobro al usuario.

2. **[TQPS6-3](https://juliodelamar101010.atlassian.net/browse/TQPS6-3) — Falta de mensaje de error al denegar geolocalización:**
   * **Descripción:** Al revocar o denegar los permisos de geolocalización a la aplicación, no se muestra el mensaje de error correspondiente especificado en los requisitos.
   * **Impacto:** Manejo de excepciones y experiencia de usuario.

---

## ⏱️ Reglas de Negocio Clave

* **Temporizador de prueba:** En el entorno de pruebas, el temporizador de seguimiento está fijado a 15 segundos para validar la transición automática hacia la pantalla de entrega.
* **Tiempo de entrega por restaurante:**
  $$\text{Tiempo de entrega} = \max(\text{tiempo de preparación de los platillos}) + \text{tiempo de entrega al punto de recogida}$$
* **Tiempo total del pedido:** Es el tiempo máximo de preparación y entrega entre todos los restaurantes involucrados.
* **Costo del pedido:** Suma total de los costos de los platillos solicitados.
