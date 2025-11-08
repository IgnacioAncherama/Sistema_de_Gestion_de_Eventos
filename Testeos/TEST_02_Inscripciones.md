# Inscripciones y Administración de Participantes
## Sistema de Gestión de Eventos - Testing Completo

**Módulo:** Inscripciones  
**Fecha de Ejecución:** 07/11/2025  
**Total de Tests:** 8  
**Tests Exitosos:** 7   
**Tests Fallidos:** 1   
**Tasa de Éxito:** 87,5%

---

## PRUEBA 1: Inscribir nuevo participante a evento

**Estado:** PASS

### Descripción
Inscribir nuevo participante a evento

### Inputs
```
1. 1
2. 12345678
3. Juan
4. Pérez
5. juan@email.com
6. 1234567890
7. 01/01/1990
8. Masculino
9. Argentina
10. Ingeniero
```

### Output Esperado
```
Inscripción registrada exitosamente
```

### Fecha de Ejecución
**07/11/2025 16:41:54**

### Output Obtenido
```
============================================================
           REGISTRAR NUEVA INSCRIPCIÓN
============================================================
Ingrese el ID del evento: 
Evento: Evento Test
Fecha: 15/12/2025
Precio: $1,000.00
Ingrese el documento del participante: 
  Participante no registrado. Se solicitarán datos adicionales.


--- REGISTRO DE NUEVO PARTICIPANTE ---
Nombre: Apellido: Email: Teléfono: Fecha de nacimiento (DD/MM/AAAA): Género: País: Profesión: 
 ÉXITO: Participante registrado exitosamente


 ÉXITO: Inscripción registrada exitosamente. ID: 1

```

### Resumen de Correcciones
**Ninguna - Test pasó correctamente**

---

## PRUEBA 2: Validar rechazo de inscripción duplicada

**Estado:**  PASS

### Descripción
Validar rechazo de inscripción duplicada

### Inputs
```
1. 1
2. 12345678
```

### Output Esperado
```
ERROR: El participante ya está inscrito en este evento
```

### Fecha de Ejecución
**07/11/2025 16:41:54**

### Output Obtenido
```
============================================================
           REGISTRAR NUEVA INSCRIPCIÓN
============================================================
Ingrese el ID del evento: 
Evento: Evento Test
Fecha: 15/12/2025
Precio: $1,000.00
Ingrese el documento del participante: 
Participante encontrado: Juan Pérez

 ERROR: El participante ya está inscrito en este evento


```

### Resumen de Correcciones
**Ninguna - Test pasó correctamente**

---

## PRUEBA 3: Agregar participante a lista de espera cuando evento lleno

**Estado:** pass

### Descripción
Agregar participante a lista de espera cuando evento lleno

### Inputs
```
1. 5
2. 12345678
3. carlos
4. perez
5. perez@gmail.com
6. 1567899876
7. 21/10/2000
8. masculino
9. argentina
10. ingeniero
11. s

```

### Output Esperado
```
Participante agregado a lista de espera
```

### Fecha de Ejecución
**07/11/2025 16:41:54**

### Output Obtenido
```
============================================================
           REGISTRAR NUEVA INSCRIPCIÓN
============================================================
Ingrese el ID del evento: 5

Evento: pruebas
Fecha: 24/12/2025
Precio: $1,000.00
Ingrese el documento del participante: 12345678

  Participante no registrado. Se solicitarán datos adicionales.


--- REGISTRO DE NUEVO PARTICIPANTE ---
Nombre: carlos
Apellido: perez
Email: perez@gmail.com
Teléfono: 1567899876
Fecha de nacimiento (DD/MM/AAAA): 21/10/2000
Género: masculino
País: argentina
Profesión: ingeniero

 ÉXITO: Participante registrado exitosamente

Evento completo. ¿Desea agregarse a lista de espera? (S/N): s

 ÉXITO: Participante agregado a lista de espera en la posición: 1
```

### Resumen de Correcciones
**Ninguna - Test pasó correctamente**.

---

## PRUEBA 4: Consultar inscripciones de un evento específico

**Estado:** PASS

### Descripción
Consultar inscripciones de un evento específico

### Inputs
```
1. i
2. c
3. e
4. 1
```

### Output Esperado
```
Mostrar lista de inscripciones del evento 1
```

### Fecha de Ejecución
**07/11/2025 16:41:54**

### Output Obtenido
```
============================================================
           CONSULTA DE INSCRIPCIONES
============================================================
E. Ver por evento
P. Ver por participante
T. Ver todas las inscripciones
============================================================

Seleccione una opción: e
Ingrese el ID del evento: 1

--- INSCRIPCIONES DEL EVENTO: Workshop Integración ---

--- Inscripción ID: 1 ---
Participante: Integration Test
Evento: Workshop Integración
Fecha inscripción: 07/11/2025
Estado: confirmada
Estado pago: pagado
------------------------------------------------------------

--- Inscripción ID: 4 ---
Participante: juan Perez
Evento: Workshop Integración
Fecha inscripción: 07/11/2025
Estado: confirmada
Estado pago: pendiente
------------------------------------------------------------
```

### Resumen de Correcciones
**Ninguna - Test pasó correctamente**

---

## PRUEBA 5: Consultar inscripciones de un participante específico

**Estado:**  PASS

### Descripción
Consultar inscripciones de un participante específico

### Inputs
```
1. c
2. p
2. 11111111
```

### Output Esperado
```
Mostrar inscripciones del participante 12345678
```

### Fecha de Ejecución
**07/11/2025 16:41:54**

### Output Obtenido
```
============================================================
           CONSULTA DE INSCRIPCIONES
============================================================
E. Ver por evento
P. Ver por participante
T. Ver todas las inscripciones
============================================================

Seleccione una opción: p
Ingrese el documento del participante: 11111111

--- INSCRIPCIONES DE: juan Perez ---

--- Inscripción ID: 4 ---
Participante: juan Perez
Evento: Workshop Integración
Fecha inscripción: 07/11/2025
Estado: confirmada
Estado pago: pendiente
------------------------------------------------------------

--- Inscripción ID: 5 ---
Participante: juan Perez
Evento: pruebas
Fecha inscripción: 07/11/2025
Estado: confirmada
Estado pago: pendiente
------------------------------------------------------------

```

### Resumen de Correcciones
**Ninguna - Test pasó correctamente**

---

## PRUEBA 6: Cancelar inscripción confirmada

**Estado:**  FAIL

### Descripción
Cancelar inscripción confirmada

### Inputs
```
1. x
2. 5
```

### Output Esperado
```
Inscripción cancelada exitosamente
```

### Fecha de Ejecución
**07/11/2025 16:41:55**

### Output Obtenido
```
============================================================
           CANCELAR INSCRIPCIÓN
============================================================
Ingrese el ID de la inscripción: 5

--- Inscripción ID: 5 ---
Participante: juan Perez
Evento: pruebas
Fecha inscripción: 07/11/2025
Estado: confirmada
Estado pago: pendiente
------------------------------------------------------------

 Error inesperado: name 'datetime' is not defined
Por favor, contacte al soporte técnico.

```

### Resumen de Correcciones
**Requiere corrección**

**Nota:** Este test falló por falta de un import 

 **Corrección:** se agrega el import "datetime" en la linea 8 del modulo
```
from datetime import date, datetime
```

### Inputs
```
1. x
2. 6
3. s
```

### Output Esperado
```
ÉXITO: Estado de inscripción actualizado a: cancelada

y si hay gente en la lista de espera

Se ha promovido a xxxx desde la lista de espera
```

### Fecha de Ejecución
**07/11/2025 16:41:55**

### Output Obtenido
```
============================================================
           CANCELAR INSCRIPCIÓN
============================================================
Ingrese el ID de la inscripción: 6

--- Inscripción ID: 6 ---
Participante: carlos perez
Evento: pruebas
Fecha inscripción: 08/11/2025
Estado: confirmada
Estado pago: pendiente
------------------------------------------------------------
¿Confirma la cancelación? (S/N): s

 ÉXITO: Estado de inscripción actualizado a: cancelada


  Se ha promovido a juan Perez desde la lista de espera

```
ahora si se obtuvo el resulado esperado

---

## PRUEBA 7: Verificar promoción desde lista de espera

**Estado:** pass

### Descripción
Verificar promoción automática desde lista de espera

### Inputs
```
1. i
2. l
3. 5
4. 1
5. 1
```

### Output Esperado
```
Participante promovido exitosamente. ID inscripcion n
```

### Fecha de Ejecución
**07/11/2025 16:41:55**

### Output Obtenido
```
============================================================
           GESTIONAR LISTA DE ESPERA
============================================================
Ingrese el ID del evento: 5

--- LISTA DE ESPERA: pruebas ---
1. carlos perez - 12345678

1. Promover un participante
2. Eliminar un participante

Seleccione una opción: 1
Ingrese la posición del participante a promover: 1

 ÉXITO: Participante promovido exitosamente. ID inscripción: 6
```

### Resumen de Correcciones
**Ninguna - Test pasó correctamente**

---

## PRUEBA 8: Visualizar lista de espera de un evento

**Estado:** PASS

### Descripción
Visualizar lista de espera de un evento

### Inputs
```
1. i
2. l
3. 5

```

### Output Esperado
```
Mostrar lista de espera del evento
```

### Fecha de Ejecución
**07/11/2025 16:41:55**

### Output Obtenido
```
============================================================
           GESTIONAR LISTA DE ESPERA
============================================================
Ingrese el ID del evento: 5

--- LISTA DE ESPERA: pruebas ---
1. juan Perez - 11111111

1. Promover un participante
2. Eliminar un participante
```

### Resumen de Correcciones
**Ninguna - Test pasó correctamente**

---

## Resumen del Módulo

| Métrica | Valor |
|---------|-------|
| Total de Pruebas | 8 |
| Pruebas Exitosas | 7  |
| Pruebas Fallidas | 1  |
| Tasa de Éxito | 87,5% |



**Documento generado automáticamente el 07/11/2025**  
**Sistema:** Sistema de Gestión de Eventos v1.0
