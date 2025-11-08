# Gestión de Eventos
## Sistema de Gestión de Eventos - Testing Completo

**Módulo:** Gestión de Eventos  
**Fecha de Ejecución:** 07/11/2025  
**Total de Tests:** 8  
**Tests Exitosos:** 8   
**Tests Fallidos:** 0   
**Tasa de Éxito:** 100.0%

---

## PRUEBA 1: Crear evento válido con todos los campos correctos

**Estado:**  PASS

### Descripción
Crear evento válido con todos los campos correctos

### Inputs
```
1. Conferencia Python 2025
2. Conferencia anual
3. 15/12/2025
4. 09:00
5. 17:00
6. Centro Convenciones
7. 200
8. 5000
```

### Output Esperado
```
Evento creado exitosamente con ID: 1
```

### Fecha de Ejecución
**07/11/2025 16:41:53**

### Output Obtenido
```
============================================================
           CREAR NUEVO EVENTO
============================================================

Ingrese nombre del evento: 
Ingrese descripción del evento: 
Ingrese fecha del evento (DD/MM/AAAA):
 Ingrese hora de inicio (HH:MM): 
 Ingrese hora de fin (HH:MM): 
 Ingrese ubicación del evento: 
 Ingrese capacidad máxima: 
 Ingrese precio del evento: 
 ÉXITO: Evento creado exitosamente con ID: 1

```

### Resumen de Correcciones
**Ninguna - Test pasó correctamente**

---

## PRUEBA 2: Validar rechazo de evento con fecha pasada

**Estado:** PASS

### Descripción
Validar rechazo de evento con fecha pasada

### Inputs
```
1. Evento Pasado
2. Descripción
3. 01/01/2024
4. 09:00
5. 10:00
6. Ubicación
7. 50
8. 100
```

### Output Esperado
```
ERROR: La fecha debe ser posterior a hoy
```

### Fecha de Ejecución
**07/11/2025 16:41:53**

### Output Obtenido
```
============================================================
           CREAR NUEVO EVENTO
============================================================

Ingrese nombre del evento:
 Ingrese descripción del evento: 
 Ingrese fecha del evento (DD/MM/AAAA): 
 ERROR: La fecha debe ser posterior a hoy

Ingrese fecha del evento (DD/MM/AAAA): 

```

### Resumen de Correcciones
**Ninguna - Test pasó correctamente**

---

## PRUEBA 3: Validar rechazo de capacidad negativa

**Estado:** PASS

### Descripción
Validar rechazo de capacidad negativa

### Inputs
```
1. Evento Cap Negativa
2. Desc
3. 01/01/2026
4. 09:00
5. 10:00
6. Ubic
7. -10
8. 100
```

### Output Esperado
```
ERROR: La capacidad debe ser mayor a 0
```

### Fecha de Ejecución
**07/11/2025 16:41:53**

### Output Obtenido
```
============================================================
           CREAR NUEVO EVENTO
============================================================

Ingrese nombre del evento: 
Ingrese descripción del evento:
Ingrese fecha del evento (DD/MM/AAAA):
Ingrese hora de inicio (HH:MM): 
Ingrese hora de fin (HH:MM): Ingrese ubicación del evento: 
Ingrese capacidad máxima: 
ERROR: La capacidad debe ser mayor a 0

```

### Resumen de Correcciones
**Ninguna - Test pasó correctamente**

---

## PRUEBA 4: Validar rechazo de precio negativo

**Estado:**  PASS

### Descripción
Validar rechazo de precio negativo

### Inputs
```
1. Evento Precio Neg
2. Desc
3. 01/01/2026
4. 09:00
5. 10:00
6. Ubic
7. 100
8. -50
```

### Output Esperado
```
ERROR: El precio no puede ser negativo
```

### Fecha de Ejecución
**07/11/2025 16:41:53**

### Output Obtenido
```
============================================================
           CREAR NUEVO EVENTO
============================================================

Ingrese nombre del evento: 
Ingrese descripción del evento:
Ingrese fecha del evento (DD/MM/AAAA):
Ingrese hora de inicio (HH:MM): 
Ingrese hora de fin (HH:MM): Ingrese ubicación del evento: 
Ingrese capacidad máxima: 
Ingrese precio del evento: 
 ERROR: El precio no puede ser negativo

```

### Resumen de Correcciones
**Ninguna - Test pasó correctamente**

---

## PRUEBA 5: Consultar evento existente por ID

**Estado:**  PASS

### Descripción
Consultar evento existente por ID

### Inputs
```
1. I
2. 1
```

### Output Esperado
```
Evento ID: 1, nombre visible
```

### Fecha de Ejecución
**07/11/2025 16:41:53**

### Output Obtenido
```
============================================================
           CONSULTA DE EVENTOS
============================================================
T. Ver todos los eventos
I. Buscar por ID
N. Buscar por nombre
F. Buscar por fecha
S. Volver
============================================================

Seleccione una opción: Ingrese el ID del evento: 
--- Evento ID: 1 ---
Nombre: Conferencia Python 2025
Descripción: Conferencia anual
Fecha: 15/12/2025
Horario: 09:00 - 17:00
Ubicación: Centro Convenciones
Capacidad: 200 personas
Precio: $5,000.00
Estado: activo
Cupos disponibles: 200
------------------------------------------------------------

```

### Resumen de Correcciones
**Ninguna - Test pasó correctamente**

---

## PRUEBA 6: Consultar evento inexistente

**Estado:**  PASS

### Descripción
Consultar evento inexistente

### Inputs
```
1. I
2. 999
```

### Output Esperado
```
ERROR: Evento no encontrado
```

### Fecha de Ejecución
**07/11/2025 16:41:54**

### Output Obtenido
```
============================================================
           CONSULTA DE EVENTOS
============================================================
T. Ver todos los eventos
I. Buscar por ID
N. Buscar por nombre
F. Buscar por fecha
S. Volver
============================================================

Seleccione una opción: Ingrese el ID del evento: 
 ERROR: Evento no encontrado


```

### Resumen de Correcciones
**Ninguna - Test pasó correctamente**

---

## PRUEBA 7: Buscar eventos por nombre parcial

**Estado:**  PASS

### Descripción
Buscar eventos por nombre parcial

### Inputs
```
1. N
2. Conferencia
```

### Output Esperado
```
Mostrar eventos que contengan 'Conferencia'
```

### Fecha de Ejecución
**07/11/2025 16:41:54**

### Output Obtenido
```
============================================================
           CONSULTA DE EVENTOS
============================================================
T. Ver todos los eventos
I. Buscar por ID
N. Buscar por nombre
F. Buscar por fecha
S. Volver
============================================================

Seleccione una opción: 
Ingrese nombre del evento a buscar: 
Se encontraron 2 evento(s):

--- Evento ID: 3 ---
Nombre: Conferencia IA
Descripción: Desc
Fecha: 25/12/2025
Horario: 09:00 - 18:00
Ubicación: Centro
Capacidad: 100 personas
Precio: $3,000.00
Estado: activo
Cupos disponibles: 100
------------------------------------------------------------

--- Evento ID: 1 ---
Nombre: Conferencia Python 2025
Descripción: Conferencia anual
Fecha: 15/12/2025
Horario: 09:00 - 17:00
```

### Resumen de Correcciones
**Ninguna - Test pasó correctamente**

---

## PRUEBA 8: Modificar nombre de evento existente

**Estado:**  PASS

### Descripción
Modificar nombre de evento existente

### Inputs
```
1. ID: 1
2. N
3. Conferencia Python 2025 - Actualizado
```

### Output Esperado
```
ÉXITO: Evento modificado exitosamente
```

### Fecha de Ejecución
**07/11/2025 16:41:54**

### Output Obtenido
```
============================================================
           MODIFICAR EVENTO
============================================================
Ingrese el ID del evento: 
Información actual del evento:

--- Evento ID: 1 ---
Nombre: Conferencia Python 2025
Descripción: Conferencia anual
Fecha: 15/12/2025
Horario: 09:00 - 17:00
Ubicación: Centro Convenciones
Capacidad: 200 personas
Precio: $5,000.00
Estado: activo
Cupos disponibles: 200
------------------------------------------------------------

¿Qué desea modificar?
N. Nombre
F. Fecha
U. Ubicación
C. Capacidad
P. Precio

Seleccione una opción: 
Ingrese el nuevo nombre: 
ÉXITO: Evento modificado exitosamente


```

### Resumen de Correcciones
**Ninguna - Test pasó correctamente**

---

## Resumen del Módulo

| Métrica | Valor |
|---------|-------|
| Total de Pruebas | 8 |
| Pruebas Exitosas | 8  |
| Pruebas Fallidas | 0  |
| Tasa de Éxito | 100.0% |


**Documento generado automáticamente el 07/11/2025**  
**Sistema:** Sistema de Gestión de Eventos v1.0
