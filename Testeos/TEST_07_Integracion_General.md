# Tests de Integración General
## Sistema de Gestión de Eventos - Testing Completo

**Módulo:** Integración  
**Fecha de Ejecución:** 07/11/2025  
**Total de Tests:** 5  
**Tests Exitosos:** 4   
**Tests Fallidos:** 1   
**Tasa de Éxito:** 80.0%

---
## PRUEBA 1: Realización completa: crear evento + añadir participante + crear actividades +registrar pago

**Estado:** pass

### Descripción
Realización completa: crear evento + añadir participante + crear actividades + registrar pago

### Inputs
```
1. e
2. c
3. Presentacion Ariel
4. generado para demostracion
5. 10/11/2025
6. 17:00
7. 22:00
8. UTN delta
9. 3
10. 10000
11. s
12. i
13. r
14. 6
15. 45236322
16. Julian
17. Vazquez
18. julian.vazquez.2003@gmail.com
19. 1533162449
20. 13/10/2003
21. masculino
22. Argentina
23. DevOps
24. s
25. a
26. c
27. 6
28. workshop sap
29. Entremiento en el uso del sistema erp
30. 18:00
31. 19:00
32. laboratorio de sistemas
33. 2
34. s
35. p
36. p
37. 11
38. 1
39. 10000
40. efectivo
41. TC.23458
42. billetes de 2k

```

### Output Esperado
```
ÉXITO: Evento creado exitosamente con ID:


ÉXITO: Participante registrado exitosamente


 ÉXITO: Inscripción registrada exitosamente.

 ÉXITO: Actividad creada exitosamente con ID:

 ÉXITO: Pago registrado exitosamente. ID de pago:
```

### Fecha de Ejecución
**08/11/2025 16:42:00**

### Output Obtenido

```

============================================================
           CREAR NUEVO EVENTO
============================================================

Ingrese nombre del evento: Presentacion Ariel
Ingrese descripción del evento: generado para demostracion
Ingrese fecha del evento (DD/MM/AAAA): 10/11/2025
Ingrese hora de inicio (HH:MM): 17:00
Ingrese hora de fin (HH:MM): 22:00
Ingrese ubicación del evento: UTN Delta
Ingrese capacidad máxima: 3
Ingrese precio del evento: 10000

 ÉXITO: Evento creado exitosamente con ID: 6


Presione Enter para continuar...


============================================================
           REGISTRAR NUEVA INSCRIPCIÓN
============================================================
Ingrese el ID del evento: 6

Evento: Presentacion Ariel
Fecha: 10/11/2025
Precio: $10,000.00
Ingrese el documento del participante: 45236322

  Participante no registrado. Se solicitarán datos adicionales.


--- REGISTRO DE NUEVO PARTICIPANTE ---
Nombre: Julian
Apellido: Vazquez
Email: julian.vazquez.2003@gmail.com
Teléfono: 1533162449
Fecha de nacimiento (DD/MM/AAAA): 13/10/2003
Género: masculino
País: Argentina
Profesión: DevOps

 ÉXITO: Participante registrado exitosamente


 ÉXITO: Inscripción registrada exitosamente. ID: 9


Presione Enter para continuar...

============================================================
           CREAR NUEVA ACTIVIDAD
============================================================
Ingrese el ID del evento: 6

Evento: Presentacion Ariel
Fecha: 10/11/2025

Nombre de la actividad: Workshop sap
Descripción: Entremiento en el uso del sistema erp
Hora de inicio (HH:MM): 18:00
Hora de fin (HH:MM): 19:00
Ubicación específica: laboratorio de sistemas
Capacidad: 2 

 ÉXITO: Actividad creada exitosamente con ID: 4


Presione Enter para continuar...

============================================================
           REGISTRAR NUEVO PAGO
============================================================
Ingrese el ID de la inscripción: 11

Evento: Presentacion Ariel
Monto a pagar: $10,000.00

Métodos de pago disponibles:
1. Efectivo
2. Tarjeta
3. Transferencia
Seleccione método de pago (1-3): 1
Ingrese monto recibido: 10000

--- DATOS ADICIONALES DEL PAGO (obligatorios) ---
Concepto del pago: efectivo
Número de comprobante: TC-23458
Observaciones: billetes de 2k 

 ÉXITO: Pago registrado exitosamente. ID de pago: 4


Presione Enter para continuar...
```

### Resumen de Correcciones
**Ninguna - Test pasó correctamente**


## PRUEBA 2: Gestión de lista de espera: Llenado → Lista espera → Cancelación → Promoción automática

**Estado:** pass

### Descripción
Gestión de lista de espera: Llenado → Lista espera → Cancelación → Promoción automática

### Inputs
```
1. i
2. r
3. 2
4. 11111111
5. Juan
6. Pérez
7. juan@email.com
8. 1234567890
9. 01/01/1990
10. Masculino
11. Argentina
12. Ingeniero
13. r
14. 2
15. 12345678
16. x
17. 2
18. s


```

### Output Esperado
```
Participante promovido automáticamente desde lista de espera
```

### Fecha de Ejecución
**07/11/2025 16:41:59**

### Output Obtenido
```
PASO 1:
============================================================
           REGISTRAR NUEVA INSCRIPCIÓN
============================================================
Ingrese el ID del evento: 
Evento: Evento Capacidad 1
Fecha: 30/12/2025
Precio: $1,000.00
Ingrese el documento del participante: 
  Participante no registrado. Se solicitarán datos adicionales.


--- REGISTRO DE NUEVO PARTICIPANTE ---
Nombre: 
Apellido: 
Email: 
Teléfono: 
Fecha de nacimiento (DD/MM/AAAA): 
Género: 
País: 
Profesión: 
 ÉXITO: Participante registrado exitosamente


 ÉXITO: Inscripción registrada exitosamente. ID: 2

============================================================
           REGISTRAR NUEVA INSCRIPCIÓN
============================================================
Ingrese el ID del evento: 2

Evento: Evento Capacidad 1
Fecha: 30/12/2025
Precio: $1,000.00
Ingrese el documento del participante: 12345678

Participante encontrado: carlos perez
Evento completo. ¿Desea agregarse a lista de espera? (S/N): s

 ÉXITO: Participante agregado a lista de espera en la posición: 1


Presione Enter para continuar...

 ============================================================
           CANCELAR INSCRIPCIÓN
============================================================
Ingrese el ID de la inscripción: 2

--- Inscripción ID: 2 ---
Participante: Primero Usuario
Evento: Evento Capacidad 1
Fecha inscripción: 07/11/2025
Estado: confirmada
Estado pago: pendiente
------------------------------------------------------------
¿Confirma la cancelación? (S/N): s

 ÉXITO: Estado de inscripción actualizado a: cancelada


  Se ha promovido a carlos perez desde la lista de espera
```

### Resumen de Correcciones
**Ninguna - Test pasó correctamente**

---

## PRUEBA 3: Crear evento con múltiples actividades y consultar

**Estado:** PASS

### Descripción
Crear evento con múltiples actividades paralelas y consultar

### Inputs
```
1. a
2. e
3. 6

```

### Output Esperado
```
3 actividades visibles en la consulta del evento
```

### Fecha de Ejecución
**07/11/2025 16:41:59**

### Output Obtenido
```
============================================================
           CONSULTA DE ACTIVIDADES
============================================================
E. Ver por evento
T. Ver todas las actividades
S. Volver
============================================================

Seleccione una opción: e
Ingrese el ID del evento: 6

--- ACTIVIDADES DEL EVENTO: Presentacion Ariel ---

--- Actividad ID: 4 ---
Nombre: Workshop sap
Descripción: Entremiento en el uso del sistema erp
Horario: 18:00 - 19:00
Ubicación: laboratorio de sistemas
Capacidad: 2
------------------------------------------------------------

--- Actividad ID: 5 ---
Nombre: workshop crm
Descripción: user experience con crm
Horario: 18:30 - 19:30
Ubicación: laboratorio de sistemas
Capacidad: 5
------------------------------------------------------------

--- Actividad ID: 6 ---
Nombre: taller de programacion competitiva
Descripción: aplicacion de concimientos
Horario: 20:00 - 23:00
Ubicación: laboratorio de sistemas
Capacidad: 5
------------------------------------------------------------

Presione Enter para continuar...  


```

### Resumen de Correcciones
**Ninguna - Test pasó correctamente**

---

## PRUEBA 4: Realización completa: Asistencia + Recursos (Personal y Material)

**Estado:** pass


### Descripción
Realización completa: Asistencia

### Inputs
```
1. r
2. i
3. l
4. 11111111
5. a
6.1
7. r
8. 1
9. 1
10. computadora
11. 3
12. r
13. 1
14. 2
```

### Output Esperado
```
 ÉXITO: Control de asistencia iniciado

 ÉXITO: Llegada registrada exitosamente

 resumen de asistencia

ÉXITO: Uso de equipo registrado

capacidad ocupada y disponible del evento


```

### Fecha de Ejecución
**07/11/2025 16:42:00**

### Output Obtenido
```
============================================================
           INICIAR CONTROL DE ASISTENCIA
============================================================
Ingrese el ID del evento: 1

 ÉXITO: Control de asistencia iniciado


Evento: Workshop Integración
Participantes esperados: 1

Presione Enter para continuar...

============================================================
           REGISTRAR LLEGADA DE PARTICIPANTE
============================================================
Ingrese el documento del participante: 11111111

 ÉXITO: Llegada registrada exitosamente


Participante: juan Perez
Evento: Workshop Integración
Ubicación: Centro

Presione Enter para continuar...

============================================================
           CONSULTAR ASISTENCIA EN TIEMPO REAL
============================================================
Ingrese el ID del evento: 1

============================================================
           RESUMEN DE ASISTENCIA
============================================================
Evento: Workshop Integración
Fecha: 09/11/2025

Total inscriptos: 2
Presentes: 2
Ausentes: 0
Porcentaje de asistencia: 100.00%

--- LISTA DE PRESENTES ---
  • juan Perez - Llegada: 16:31:56
  • Integration Test - Llegada: 16:36:17



============================================================
           GESTIONAR RECURSOS DEL EVENTO
============================================================
Ingrese el ID del evento: 1

Evento: Workshop Integración

Opciones de gestión de recursos:
1. Registrar uso de equipos
2. Controlar capacidad de sala
3. Gestionar materiales
4. Registrar incidencias

Seleccione una opción: 1
Ingrese nombre del equipo: computadora
Ingrese cantidad utilizada: 3

 ÉXITO: Uso de equipo registrado


Presione Enter para continuar...

============================================================
           GESTIONAR RECURSOS DEL EVENTO
============================================================
Ingrese el ID del evento: 1

Evento: Workshop Integración

Opciones de gestión de recursos:
1. Registrar uso de equipos
2. Controlar capacidad de sala
3. Gestionar materiales
4. Registrar incidencias

Seleccione una opción: 2

Capacidad máxima: 50
Asistentes registrados: 2
Espacios disponibles: 48

Presione Enter para continuar...
```

### Resumen de Correcciones


---

## PRUEBA 5: Generar múltiples informes de un evento finalizado con datos completos

**Estado:** pass

### Descripción
Generar múltiples informes de un evento finalizado con datos completos

### Inputs
```
1. f
2. a
3. conferencia testing
4. 1
5. d
6. conferencia testing
7. 1
8. n
9. e
10. conferencia teting
11. 1


```

### Output Esperado
```
3 informes generados correctamente con datos reales
```

### Fecha de Ejecución
**07/11/2025 16:42:00**

### Output Obtenido
```
============================================================
           INFORME DE ASISTENCIA
============================================================
Evento: Conferencia Testing 2025
Fecha: 03/11/2025
Ubicación: Centro de Convenciones

--- ESTADÍSTICAS ---
Total Registrados: 3
Total Asistentes: 2
Ausentes: 1
Tasa de Asistencia: 66.67%

--- GRÁFICO DE ASISTENCIA ---
Asistieron: ██████████████████████████ 2
Ausentes:   ░░░░░░░░░░░░░ 1

Presione Enter para continuar...

============================================================
           INFORME DEMOGRÁFICO
============================================================

Ingrese el nombre o parte del nombre del evento:
> conferencia testing

--- Eventos Coincidentes ---
1. Conferencia Testing 2025 (ID: 7) - 03/11/2025

Ingrese el número de la opción (0 para cancelar): 1

============================================================
           INFORME DEMOGRÁFICO
============================================================
Evento: Conferencia Testing 2025
Fecha: 03/11/2025
Total de asistentes: 2

--- DISTRIBUCIÓN POR GÉNERO ---
Femenino...................... █████████████████████████ 1 (50.0%)
Masculino..................... █████████████████████████ 1 (50.0%)

--- DISTRIBUCIÓN POR PAÍS ---
Argentina..................... ██████████████████████████████████████████████████ 2 (100.0%)

--- DISTRIBUCIÓN POR RANGO DE EDAD ---
26-35......................... ██████████████████████████████████████████████████ 2 (100.0%)

Edad promedio: 29.0 años
Edad mínima: 28 años
Edad máxima: 30 años

============================================================
           INFORME FINANCIERO DEL EVENTO
============================================================
Evento: Conferencia Testing 2025
Fecha: 03/11/2025
Precio: $5,000.00

--- INSCRIPCIONES ---
Total: 3
Pagos completados: 3
Pagos pendientes: 0

--- INGRESOS ---
Ingresos reales: $15,000.00
Ingresos pendientes: $0.00
Ingresos potenciales: $15,000.00

--- EGRESOS ---
Total reembolsos: $0.00

--- BALANCE ---
Ingresos netos: $15,000.00

--- DISTRIBUCIÓN DE INGRESOS ---
Cobrado:    100.0%
Pendiente:  0.0%

```

### Resumen de Correcciones
**Ninguna - Test pasó correctamente**

---

## Resumen del Módulo

| Métrica | Valor |
|---------|-------|
| Total de Pruebas | 5 |
| Pruebas Exitosas | 5 |
| Pruebas Fallidas | 0  |
| Tasa de Éxito | 100.0% |

---

**Sistema:** Sistema de Gestión de Eventos v1.0



