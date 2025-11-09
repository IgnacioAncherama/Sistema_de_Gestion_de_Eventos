# Administración de Pagos y Cobros
## Sistema de Gestión de Eventos - Testing Completo

**Módulo:** Pagos  
**Fecha de Ejecución:** 07/11/2025  
**Total de Tests:** 8  
**Tests Exitosos:** 7   
**Tests Fallidos:** 1   
**Tasa de Éxito:** 87.5%

---

## PRUEBA 1: Registrar pago completo en efectivo

**Estado:** PASS

### Descripción
Registrar pago completo en efectivo

### Inputs
```
1. 1
2. 1
3. 2500
4. Pago total
5. COMP-001
6. Ninguna
```

### Output Esperado
```
Pago registrado exitosamente
```

### Fecha de Ejecución
**07/11/2025 16:41:55**

### Output Obtenido
```
============================================================
           REGISTRAR NUEVO PAGO
============================================================
Ingrese el ID de la inscripción: 
Evento: Evento Pago
Monto a pagar: $2,500.00

Métodos de pago disponibles:
1. Efectivo
2. Tarjeta
3. Transferencia
Seleccione método de pago (1-3): Ingrese monto recibido: 
--- DATOS ADICIONALES DEL PAGO (obligatorios) ---
Concepto del pago: Número de comprobante: Observaciones: 
 ÉXITO: Pago registrado exitosamente. ID de pago: 1

```

### Resumen de Correcciones
**Ninguna - Test pasó correctamente**

---

## PRUEBA 2: Validar rechazo de pago duplicado

**Estado:**  PASS

### Descripción
Validar rechazo de pago duplicado

### Inputs
```
1. 1
2. 1
3. 2500
4. Pago duplicado
5. COMP-002
6. 
```

### Output Esperado
```
ERROR: Esta inscripción ya ha sido pagada
```

### Fecha de Ejecución
**07/11/2025 16:41:55**

### Output Obtenido
```
============================================================
           REGISTRAR NUEVO PAGO
============================================================
Ingrese el ID de la inscripción: 
 ERROR: Esta inscripción ya ha sido pagada


Presione Enter para continuar...
```

### Resumen de Correcciones
**Ninguna - Test pasó correctamente**

---

## PRUEBA 3: Validar rechazo de pago con monto insuficiente

**Estado:**  PASS

### Descripción
Validar rechazo de pago con monto insuficiente

### Inputs
```
1. 2
2. 1
3. 2000
4. Pago parcial
5. COMP-003
6. 
```

### Output Esperado
```
ERROR: Monto insuficiente
```

### Fecha de Ejecución
**07/11/2025 16:41:55**

### Output Obtenido
```
============================================================
           REGISTRAR NUEVO PAGO
============================================================
Ingrese el ID de la inscripción: 
Evento: Evento Pago
Monto a pagar: $2,500.00

Métodos de pago disponibles:
1. Efectivo
2. Tarjeta
3. Transferencia
Seleccione método de pago (1-3): Ingrese monto recibido: 
 ERROR: Monto insuficiente. Falta: $500.00


Presione Enter para continuar...
```

### Resumen de Correcciones
**Ninguna - Test pasó correctamente**

---

## PRUEBA 4: Registrar pago con tarjeta de crédito

**Estado:** pass

### Descripción
Registrar pago con tarjeta de crédito

### Inputs
```
1. p
2. 5
2. 2
3. 1000
4. Pago con tarjeta
5. TC-12345
6. visa
```

### Output Esperado
```
Pago registrado exitosamente
```

### Fecha de Ejecución
**07/11/2025 16:41:55**

### Output Obtenido
```
============================================================
           REGISTRAR NUEVO PAGO
============================================================
Ingrese el ID de la inscripción: 5

Evento: pruebas
Monto a pagar: $1,000.00

Métodos de pago disponibles:
1. Efectivo
2. Tarjeta
3. Transferencia
Seleccione método de pago (1-3): 2
Ingrese monto recibido: 1000

--- DATOS ADICIONALES DEL PAGO (obligatorios) ---
Concepto del pago: pago con tarjeta
Número de comprobante: TC-12345
Observaciones: visa

 ÉXITO: Pago registrado exitosamente. ID de pago: 2


```

### Resumen de Correcciones
**Ninguna - Test pasó correctamente**

---

## PRUEBA 5: Consultar pagos de una inscripción específica

**Estado:**  PASS

### Descripción
Consultar pagos de una inscripción específica

### Inputs
```
1. I
2. 1
```

### Output Esperado
```
Mostrar pagos de la inscripción 1
```

### Fecha de Ejecución
**07/11/2025 16:41:55**

### Output Obtenido
```
============================================================
           CONSULTA DE PAGOS
============================================================
I. Consultar por inscripción
E. Consultar por evento
P. Ver pagos pendientes
T. Ver todos los pagos
============================================================

Seleccione una opción: Ingrese el ID de la inscripción: 
=== INFORMACIÓN DE PAGO ===
ID Inscripción: 1
Estado de pago: pagado
ID Pago: 1
Monto: $2,500.00
Método: Efectivo
Fecha: 07/11/2025


```

### Resumen de Correcciones
**Ninguna - Test pasó correctamente**

---

## PRUEBA 6: Consultar todos los pagos de un evento

**Estado:**  PASS

### Descripción
Consultar todos los pagos de un evento

### Inputs
```
1. E
2. 1
```

### Output Esperado
```
Mostrar pagos del evento 1
```

### Fecha de Ejecución
**07/11/2025 16:41:55**

### Output Obtenido
```
============================================================
           CONSULTA DE PAGOS
============================================================
I. Consultar por inscripción
E. Consultar por evento
P. Ver pagos pendientes
T. Ver todos los pagos
============================================================

Seleccione una opción: Ingrese el ID del evento: 
=== PAGOS DEL EVENTO: Evento Pago ===

ID: 1 | Monto: $2,500.00 | Método: Efectivo | Fecha: 07/11/2025

Total recaudado: $2,500.00


```

### Resumen de Correcciones
**Ninguna - Test pasó correctamente**

---

## PRUEBA 7: Consultar pagos pendientes

**Estado:**  PASS

### Descripción
Consultar pagos pendientes

### Inputs
```
1. P
```

### Output Esperado
```
Mostrar inscripciones con pago pendiente
```

### Fecha de Ejecución
**07/11/2025 16:41:56**

### Output Obtenido
```
============================================================
           CONSULTA DE PAGOS
============================================================
I. Consultar por inscripción
E. Consultar por evento
P. Ver pagos pendientes
T. Ver todos los pagos
============================================================

Seleccione una opción: 
=== PAGOS PENDIENTES ===
Total: 2

Inscripción #2
  Participante: Carlos Ruiz
  Evento: Evento Pago
  Monto: $2,500.00

Inscripción #3
  Participante: Laura Díaz
  Evento: Evento Pago
  Monto: $2,500.00

Monto total pendiente: $5,000.00

```

### Resumen de Correcciones
**Ninguna - Test pasó correctamente**

---

## PRUEBA 8: Realizar un reembolso 

**Estado:**  PASS

### Descripción
Realizar un reembolso de una inscripción

### Inputs
```
1. p
2. d
3. 5
4. s
```

### Output Esperado
```
reembolso procesado exitosamente
```

### Fecha de Ejecución
**07/11/2025 16:41:56**

### Output Obtenido
```
============================================================
           PROCESAR REEMBOLSO
============================================================
Ingrese el ID de la inscripción: 5

Evento: pruebas
Precio pagado: $1,500.00
Días hasta el evento: 46
Porcentaje de reembolso: 100%
Monto a reembolsar: $1,500.00
¿Confirma el reembolso? (S/N): s

 ÉXITO: Reembolso procesado exitosamente. ID: 1

```


### Resumen de Correcciones
**Ninguna - Test pasó correctamente**


## PRUEBA 9: Calcular reembolso a dos dias del evento


**Estado:**  PASS

### Descripción
Realizar un reembolso de una inscripción

### Inputs
```
1. p
2. d
3. 11

```

### Output Esperado
```
monto a reembolsar 25% del monto total abonado
```

### Fecha de Ejecución
**07/11/2025 16:41:56**

### Output Obtenido
```
============================================================
           PROCESAR REEMBOLSO
============================================================
Ingrese el ID de la inscripción: 11

Evento: Presentacion Ariel
Precio pagado: $10,000.00
Días hasta el evento: 2
Porcentaje de reembolso: 25%
Monto a reembolsar: $2,500.00
¿Confirma el reembolso? (S/N): 

```
vemos los 2500 que es el 25% de 10000

### Resumen de Correcciones
**Ninguna - Test pasó correctamente**

---

## Resumen del Módulo

| Métrica | Valor |
|---------|-------|
| Total de Pruebas | 9 |
| Pruebas Exitosas | 9 |
| Pruebas Fallidas | 0 |
| Tasa de Éxito | 100% |

 
**Sistema:** Sistema de Gestión de Eventos v1.0

