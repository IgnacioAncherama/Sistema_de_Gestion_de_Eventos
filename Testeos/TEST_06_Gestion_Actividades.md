# Gestión de Actividades
## Sistema de Gestión de Eventos - Testing Completo

**Módulo:** Gestión de Actividades  
**Fecha de Ejecución:** 07/11/2025  
**Total de Tests:** 8  
**Tests Exitosos:** 8   
**Tests Fallidos:** 0   
**Tasa de Éxito:** 100.0%

---

## PRUEBA 1: Crear actividad válida para un evento

**Estado:**  PASS

### Descripción
Crear actividad válida para un evento

### Inputs
```
1. 1
2. Charla Inaugural
3. Presentación del evento
4. 09:30
5. 10:30
6. Auditorio Principal
7. 100
```

### Output Esperado
```
Actividad creada exitosamente con ID: 1
```

### Fecha de Ejecución
**07/11/2025 16:41:58**

### Output Obtenido
```
============================================================
           CREAR NUEVA ACTIVIDAD
============================================================
Ingrese el ID del evento: 
Evento: Conferencia con Actividades
Fecha: 20/12/2025

Nombre de la actividad: 
Descripción: 
Hora de inicio (HH:MM): 
Hora de fin (HH:MM): 
Ubicación específica: 
Capacidad: 
 ÉXITO: Actividad creada exitosamente con ID: 1


```

### Resumen de Correcciones
**Ninguna - Test pasó correctamente**

---

## PRUEBA 2: Validar rechazo de actividad con horario inválido

**Estado:**  PASS

### Descripción
Validar rechazo de actividad con horario inválido

### Inputs
```
1. 6
2. juegos
3. juegos
4. 13:00
5. 20:00
```

### Output Esperado
```
ERROR: La hora de inicio debe estar entre 17:0 y 22:00
```

### Fecha de Ejecución
**07/11/2025 16:41:58**

### Output Obtenido
```
=============================================================
           CREAR NUEVA ACTIVIDAD
============================================================
Ingrese el ID del evento: 6

Evento: Presentacion Ariel
Fecha: 10/11/2025
Horario del evento: 17:00 - 22:00

Nombre de la actividad: juegos
Descripción: juegos
Hora de inicio (HH:MM): 13:00
Hora de fin (HH:MM): 20:00

 ERROR: La hora de inicio debe estar entre 17:00 y 22:00


Presione Enter para continuar...
```

### Resumen de Correcciones
**Ninguna - Test pasó correctamente**

---

## PRUEBA 3: Validar rechazo de actividad con capacidad negativa

**Estado:**  PASS

### Descripción
Validar rechazo de actividad con capacidad negativa

### Inputs
```
1. 6
2. juegis
3. juegos
4. 18:00
5. 20:00
6. lab
7. -5
```

### Output Esperado
```
ERROR: La capacidad debe ser mayor a 0
```

### Fecha de Ejecución
**07/11/2025 16:41:58**

### Output Obtenido
```
============================================================
           CREAR NUEVA ACTIVIDAD
============================================================
Ingrese el ID del evento: 6

Evento: Presentacion Ariel
Fecha: 10/11/2025
Horario del evento: 17:00 - 22:00

Nombre de la actividad: juegis
Descripción: juegos
Hora de inicio (HH:MM): 18:00
Hora de fin (HH:MM): 20:00
Ubicación específica: lab
Capacidad: -5

 ERROR: La capacidad debe ser mayor a 0


Presione Enter para continuar...

```

### Resumen de Correcciones
**Ninguna - Test pasó correctamente**

---

## PRUEBA 4: Crear segunda actividad para el mismo evento

**Estado:**  PASS

### Descripción
Crear segunda actividad para el mismo evento

### Inputs
```
1. 1
2. Taller Práctico
3. Ejercicios prácticos
4. 11:00
5. 13:00
6. Sala B
7. 30
```

### Output Esperado
```
Actividad creada exitosamente
```

### Fecha de Ejecución
**07/11/2025 16:41:58**

### Output Obtenido
```
============================================================
           CREAR NUEVA ACTIVIDAD
============================================================
Ingrese el ID del evento: 
Evento: Conferencia con Actividades
Fecha: 20/12/2025

Nombre de la actividad: 
Descripción: 
Hora de inicio (HH:MM): 
Hora de fin (HH:MM): 
Ubicación específica: 
Capacidad: 
 ÉXITO: Actividad creada exitosamente con ID: 2

```

### Resumen de Correcciones
**Ninguna - Test pasó correctamente**

---

## PRUEBA 5: Consultar todas las actividades de un evento

**Estado:**  PASS

### Descripción
Consultar todas las actividades de un evento

### Inputs
```
1. E
2. 1
```

### Output Esperado
```
Mostrar lista de actividades del evento 1
```

### Fecha de Ejecución
**07/11/2025 16:41:58**

### Output Obtenido
```
============================================================
           CONSULTA DE ACTIVIDADES
============================================================
E. Ver por evento
T. Ver todas las actividades
S. Volver
============================================================

Seleccione una opción: Ingrese el ID del evento: 
--- ACTIVIDADES DEL EVENTO: Conferencia con Actividades ---

--- Actividad ID: 1 ---
Nombre: Charla Inaugural
Descripción: Presentación del evento
Horario: 09:30 - 10:30
Ubicación: Auditorio Principal
Capacidad: 100
------------------------------------------------------------

--- Actividad ID: 2 ---
Nombre: Taller Práctico
Descripción: Ejercicios prácticos
Horario: 11:00 - 13:00
Ubicación: Sala B
Capacidad: 30
------------------------------------------------------------


```

### Resumen de Correcciones
**Ninguna - Test pasó correctamente**

---

## PRUEBA 6: Consultar todas las actividades del sistema

**Estado:**  PASS

### Descripción
Consultar todas las actividades del sistema

### Inputs
```
1. T
```

### Output Esperado
```
Mostrar todas las actividades registradas
```

### Fecha de Ejecución
**07/11/2025 16:41:58**

### Output Obtenido
```
============================================================
           CONSULTA DE ACTIVIDADES
============================================================
E. Ver por evento
T. Ver todas las actividades
S. Volver
============================================================

Seleccione una opción: 
--- TODAS LAS ACTIVIDADES ---

--- Actividad ID: 1 ---
Evento: Conferencia con Actividades
Nombre: Charla Inaugural
Descripción: Presentación del evento
Horario: 09:30 - 10:30
Ubicación: Auditorio Principal
Capacidad: 100
------------------------------------------------------------

--- Actividad ID: 2 ---
Evento: Conferencia con Actividades
Nombre: Taller Práctico
Descripción: Ejercicios prácticos
Horario: 11:00 - 13:00
Ubicación: Sala B
Capacidad: 30
------------------------------------------------------------

```

### Resumen de Correcciones
**Ninguna - Test pasó correctamente**

---

## PRUEBA 7: Modificar nombre de una actividad

**Estado:**  PASS

### Descripción
Modificar nombre de una actividad

### Inputs
```
1. 1
2. N
3. Charla Inaugural Actualizada
```

### Output Esperado
```
Actividad modificada exitosamente
```

### Fecha de Ejecución
**07/11/2025 16:41:58**

### Output Obtenido
```
============================================================
           MODIFICAR ACTIVIDAD
============================================================
Ingrese el ID de la actividad: 
Información actual de la actividad:

--- Actividad ID: 1 ---
Nombre: Charla Inaugural
Descripción: Presentación del evento
Horario: 09:30 - 10:30
Ubicación: Auditorio Principal
Capacidad: 100
------------------------------------------------------------

¿Qué desea modificar?
N. Nombre
D. Descripción
H. Horario
U. Ubicación
C. Capacidad

Seleccione una opción: Ingrese el nuevo nombre: 
 ÉXITO: Actividad modificada exitosamente



```

### Resumen de Correcciones
**Ninguna - Test pasó correctamente**

---

## PRUEBA 8: Eliminar actividad existente

**Estado:** PASS

### Descripción
Eliminar actividad existente

### Inputs
```
1. 2
2. S
```

### Output Esperado
```
Actividad eliminada exitosamente
```

### Fecha de Ejecución
**07/11/2025 16:41:58**

### Output Obtenido
```
============================================================
           ELIMINAR ACTIVIDAD
============================================================
Ingrese el ID de la actividad: 
Actividad a eliminar: Taller Práctico
¿Está seguro que desea eliminar esta actividad? (S/N): 
 ÉXITO: Actividad eliminada exitosamente


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

