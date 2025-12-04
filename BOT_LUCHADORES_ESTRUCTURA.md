# 🤖 BOT LUCHADORES - ESTRUCTURA MENÚ

## 📱 CONTEXTO
Bot de WhatsApp centralizado para gestionar la interacción con clientes de los 6 locales AGAVE.

**Objetivo:** Un solo número de WhatsApp (oficina CENOTE) donde los clientes pueden reservar, pedir, ver beneficios, reclamar, etc.

---

## 🎯 MENÚ PRINCIPAL DEL BOT

Cuando un cliente escribe al número:

```
¡Hola Luchador! 👋🌮

Bienvenido a AGAVE - CENOTE
¿En qué podemos ayudarte hoy?

1️⃣ Reservas
2️⃣ Ver Menú
3️⃣ Take Away
4️⃣ Delivery
5️⃣ Luchadores (Mis Beneficios)
6️⃣ Merchandise
7️⃣ Trabajá con nosotros
8️⃣ Reclamos / Sugerencias

Escribí el número de la opción
```

---

## 📋 DETALLE DE CADA OPCIÓN

### 1️⃣ RESERVAS
**Qué hace el bot:**
- Pregunta: Local, fecha, hora, cantidad de personas, nombre, teléfono
- ¿Es una ocasión especial? (Cumpleaños/Aniversario/Celebración/No)
- ¿Alguien tiene alergias o restricciones? (Celíaco/Vegetariano/Vegano/Mariscos/Frutos secos/Otra/No)
- Confirma la reserva

**Importante:** Después de tomar datos, el AI puede responder preguntas libres sobre la reserva.

---

### 2️⃣ VER MENÚ
**Qué hace el bot:**
- Pregunta: ¿Qué menú querés ver?
  - Mediodía (PDF)
  - Happy Hour (PDF)
  - Noche (PDF)
- Envía el PDF correspondiente

---

### 3️⃣ TAKE AWAY
**Qué hace el bot:**
- Muestra mensaje: "Pedí online y retirá en tu local!"
- Envía link para armar pedido online

---

### 4️⃣ DELIVERY
**Qué hace el bot:**
- Muestra mensaje: "Hacemos delivery por PedidosYa!"
- Envía link a PedidosYa

---

### 5️⃣ LUCHADORES (MIS BENEFICIOS)
**Qué hace el bot:**
- Muestra beneficios activos del cliente:

```
💪 TUS BENEFICIOS LUCHADORES

Hola [Nombre]! 🌮

Tenés disponible:
💰 $850 (vence 05/12)
🎟️ 2 gift cards ($5,000 y $2,000)
🏷️ 20% OFF próxima visita
🍹 1 Margarita gratis

¿En qué puedo ayudarte?
```

**Tipos de beneficios:**
- **Saldo disponible:** 10% cashback de consumos (válido 10 días)
- **Gift cards:** Códigos/crédito asignados
- **Descuentos:** Promos activas (2x1, 20% OFF, etc.)
- **Regalos:** Margaritas gratis, postres, etc.

**Importante:** Después de mostrar beneficios, el AI responde preguntas conversacionales:
- "¿Cómo uso mi saldo?"
- "¿Hasta cuándo es válido?"
- "¿Cómo gano más puntos?"

---

### 6️⃣ MERCHANDISE
**Qué hace el bot:**
- Muestra catálogo de productos (Remeras, Gorras, Accesorios, Combos)
- AI entiende pedidos: "quiero una remera talle L", "cuánto sale la gorra negra", etc.
- Pregunta cómo lo recibe: Envío a domicilio o Retiro en local

---

### 7️⃣ TRABAJÁ CON NOSOTROS
**Qué hace el bot:**
- Muestra posiciones abiertas por local y por rol
- AI entiende: "quiero enviar CV", "qué requisitos hay para cocina", etc.
- Recibe CV (PDF) y datos del postulante

---

### 8️⃣ RECLAMOS / SUGERENCIAS
**Qué hace el bot:**
- Pregunta tipo: Reclamo / Sugerencia / Felicitación
- Pregunta: ¿De qué local?
- Cliente explica libremente
- Puede adjuntar foto
- Bot genera número de caso para seguimiento

**Importante:** AI categoriza automáticamente la gravedad y deriva si es urgente.

---

## 🧠 ARQUITECTURA: MENÚ + AI CONVERSACIONAL

**Flujo:**
1. Cliente escribe → Ve menú principal (8 opciones)
2. Elige opción (1-8) → Bot ejecuta acción específica
3. Después de eso → **AI conversacional** entiende preguntas libres

**Ejemplo:**
```
Usuario: 5
Bot: [Muestra beneficios Luchadores]
Usuario: "cómo uso el saldo de 850?"
Bot: [AI responde naturalmente]
Usuario: "y la margarita gratis cuándo vence?"
Bot: [AI responde naturalmente]
```

---

## 💡 FEATURES IMPORTANTES

### SISTEMA LUCHADORES
- **10% cashback:** Cliente consume $10,000 → recibe $1,000 de crédito (válido 10 días)
- **Gift cards:** Se asignan manualmente desde admin y aparecen en la cuenta
- **Promos automáticas:** Cuando se crea una promo, aparece en cuenta del cliente
- **Regalos:** Margaritas, postres, etc. se asignan y aparecen disponibles

### INTEGRACIONES NECESARIAS
- Base de datos clientes (CRM)
- Sistema de beneficios (asignar/consumir)
- PDFs de menú (3 versiones)
- Links: Take Away + PedidosYa
- Sistema de reservas (o manual)

---

## 🚀 PRIORIDAD FASE 1

**MVP - Lo esencial:**
1. Menú principal funcionando
2. Reservas (con ocasión especial + alergias)
3. Ver Menú (PDFs)
4. Take Away + Delivery (solo links)
5. Luchadores (mostrar beneficios + AI conversacional básico)
6. Reclamos (registro básico)

**Fase 2 - Futuro:**
- Merchandise con compra integrada
- Pagos online integrados
- Panel admin para gestionar beneficios
- Analytics y reportes

---

## 📞 NÚMERO CENTRALIZADO

- **1 solo número WhatsApp** para todos los locales
- Ubicado en oficina CENOTE
- Bot responde 24/7
- Opción de derivar a humano si es necesario

---

## ❓ PREGUNTAS PARA DEFINIR

1. ¿Tienen base de datos de clientes actual? ¿Cómo identificamos al usuario?
2. ¿Cómo se asignan beneficios? ¿Panel admin? ¿Manual?
3. ¿Integración con sistema POS para el cashback?
4. ¿Qué plataforma de AI usar? (GPT-4, Claude, otra)
5. ¿Reservas se integran con algo o son manuales?

---

**Documento creado para reunión con NotChatBot**
**Fecha:** 02/12/2025
