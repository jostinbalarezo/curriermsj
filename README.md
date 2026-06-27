# PLAN MAESTRO — Sistema de Automatización para Courier

## Visión General

Sistema de automatización para atención al cliente y gestión de envíos mediante **Telegram** (fase inicial) → **WhatsApp Business** (producción), **panel web administrativo**, **chatbot con IA**, integración con el sistema del courier para consulta de estados, despliegue mediante **Docker** y hospedaje en **Google Cloud**.

### Prioridad

Automatizar lo que la operadora hace manualmente: responder mensajes todo el día, crear pedidos y consultar estados de paquetes.

### Decisiones Técnicas

| Decisión | Detalle |
|---|---|
| **Mensajería** | Empezar con **Telegram** (gratis), migrar a **WhatsApp Business** al consolidar clientes |
| **IA** | Empezar con **Kimi** / **Gemini Flash**, migrar a **Claude** si se necesita |
| **UX** | Menús con botones interactivos, conversaciones cortas y eficientes |
| **Cloud** | Google Cloud (crédito estudiante $300) |
| **Despliegue** | Docker en VPS → Cloud Run |

---

# FASE 1 — Automatización de Atención al Cliente

## 1A. Infraestructura

* Base de datos PostgreSQL (Supabase o Cloud SQL)
* API Backend para la gestión de clientes y consultas
* Variables de entorno para credenciales y servicios

```
TELEGRAM_BOT_TOKEN=
WHATSAPP_API_KEY=
DATABASE_URL=
AI_API_KEY=
```

## 1B. Automatización de Telegram / WhatsApp

### Operaciones sin IA (flujo directo con botones)

El bot resuelve directamente estas consultas sin necesidad de IA:

* Consultar estado de paquetes (ingresa guía → respuesta inmediata)
* Consultar tarifas
* Consultar horarios
* Registrar nuevo envío
* Ver sucursales

### Operaciones con IA (preguntas complejas)

Cuando el cliente hace preguntas que no encajan en los botones, la IA entra en acción:

* ¿Cuánto demora un envío a X ciudad?
* ¿Qué documentos necesito para enviar Y?
* Preguntas abiertas o ambiguas

### Derivación a operador

* Cuando la IA no pueda responder
* Cuando el cliente lo solicite explícitamente

### Notificación a bot de operadores

Cuando se cierra un negocio (envío registrado, cotización aceptada, etc.), el sistema envía automáticamente una notificación a un **bot interno de operadores** con los detalles:

```
🔔 Nueva orden registrada

Cliente: Juan Pérez
Guía: CU123456789
Destino: Guayaquil
Tipo: Paquete 5kg
Total: $12.50
Estado: Pagado ✓
```

## 1C. Flujo Conversacional

```
Bienvenido

1️⃣ Consultar paquete    → Respuesta directa (sin IA)
2️⃣ Registrar envío      → Formulario por botones (sin IA)
3️⃣ Tarifas              → Respuesta directa (sin IA)
4️⃣ Horarios             → Respuesta directa (sin IA)
5️⃣ Pregunta libre       → IA responde
6️⃣ Hablar con asesor    → Deriva a operador
```

Todo mediante botones interactivos para minimizar escritura. Las opciones 1-4 se resuelven sin IA, ahorrando tokens y siendo más rápidas.

## 1D. Consulta automática de envíos

El usuario podrá ingresar número de guía o código del envío. El sistema consultará automáticamente el estado dentro del sistema interno del courier.

```
📦 Estado del paquete

Guía: CU123456789
Estado: En tránsito
Última actualización: Centro Logístico Cuenca
Entrega estimada: 27/06/2026
```

## 1E. Notificaciones Automáticas

Cuando cambie el estado del paquete el cliente recibirá mensajes automáticos.

```
📦 Tu paquete fue recibido.
📦 Tu paquete salió a distribución.
🚚 Tu paquete está en ruta.
✅ Tu paquete fue entregado.
```

## 1F. Integración con el Sistema del Courier

El chatbot se conectará al sistema interno para obtener:

* Estado del envío
* Información del destinatario
* Historial de movimientos
* Fecha estimada de entrega

## 1G. Arquitectura

```
Telegram / WhatsApp Business
        ↓
    API Backend
        ↓
    Base de datos
        ↓
  Sistema del Courier
```

---

# FASE 2 — Chatbot con Inteligencia Artificial

## 2A. Modelo IA

Inicialmente: **Kimi** / **Gemini Flash**
Migración futura a **Claude** si fuese necesario.

## 2B. Funciones de IA

Responder automáticamente preguntas como:

* ¿Dónde está mi paquete?
* ¿Cuánto cuesta un envío?
* ¿Cuánto demora un envío?
* ¿Qué documentos necesito?
* ¿Cuál es el horario de atención?
* ¿Dónde están las sucursales?

## 2C. Escalamiento

Cuando la IA no pueda responder:

```
Cliente → IA → Operador Humano
```

Toda la conversación será transferida.

---

# FASE 3 — Panel Administrativo

## Funcionalidades

Dashboard web para operadores. Permitirá:

* Buscar paquetes
* Consultar clientes
* Actualizar estados
* Responder conversaciones
* Ver historial
* Administrar usuarios
* Configurar respuestas automáticas

## Seguimiento

Visualización en tiempo real del estado del paquete.

```
Recibido → Clasificación → En tránsito → En reparto → Entregado
```

## Reportes

* Número de consultas
* Tiempo promedio de respuesta
* Cantidad de envíos
* Clientes atendidos
* Estadísticas del chatbot

---

# FASE 4 — Producción

## Docker

Todo el sistema será desplegado mediante Docker.

Servicios: Backend, Base de datos, Panel Web, Chatbot, WhatsApp/Telegram API

## Cloud

Infraestructura: **Google Cloud**

Servicios: VPS o Cloud Run, PostgreSQL, Almacenamiento, Secret Manager

## Arquitectura Final

```
            Telegram / WhatsApp Business
                        │
               Chatbot con IA
                        │
        ┌───────────────┴───────────────┐
        │                               │
Panel Administrativo            Sistema Courier
        │                               │
        └───────────────┬───────────────┘
                        │
                  Base de Datos
```

---

# Modelo de Negocio

| Concepto | Detalle |
|---|---|
| **Implementación** | ~$400-500 USD (una vez) |
| **Mensualidad** | Cubre servidor + APIs + soporte |
| **Estrategia** | Prototipo con primer cliente → generalizar producto → vender a más empresas |

---

# Resumen de Fases

| Fase | Objetivo |
|---|---|
| **1** | Automatización de Telegram/WhatsApp y consultas de envíos |
| **2** | Integración de IA para atención automática |
| **3** | Desarrollo del panel administrativo y gestión de paquetes |
| **4** | Despliegue en Docker y migración a Google Cloud |
