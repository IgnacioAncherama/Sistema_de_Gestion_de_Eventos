# Realización del Evento
## Sistema de Gestión de Eventos - Testing Completo

**Módulo:** Realización de Evento  
**Fecha de Ejecución:** 09/11/2025  
**Total de Tests:** 8  
**Tests Exitosos:** 7 
**Tests Fallidos:** 1  
**Tasa de Éxito:** 87.5%

---

## PRUEBA 1: Iniciar control de asistencia para un evento

**Estado:** PASS

### Descripción
Iniciar control de asistencia para un evento

### Inputs
```
1. r
2. i


```

### Output Esperado
```
Control de asistencia iniciado
```

### Fecha de Ejecución
**09/11/2025 16:41:56**

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


```

### Resumen de Correcciones
**Ninguna - Test pasó correctamente**

---

## PRUEBA 2: Registrar llegada de participante inscrito

**Estado:** fail

### Descripción
Registrar llegada de participante inscrito

### Inputs
```
1. l
2. 11111111
```

### Output Esperado
```
Llegada registrada exitosamente
```

### Fecha de Ejecución
**09/11/2025 16:41:56**

### Output Obtenido
```
============================================================
           REGISTRAR LLEGADA DE PARTICIPANTE
============================================================
Ingrese el documento del participante: 11111111

 Error inesperado: no such column: id_evento
Por favor, contacte al soporte técnico.
```


### Resumen de Correcciones
**Requiere corrección**

**Nota:** Este test falló por falta de un import 

 **Corrección:** en la linea 136-139 problema en la consulta
```
     SELECT * FROM asistencia 
        WHERE id_inscripcion = ?
    ''', (inscripcion['id'],)
```

### Inputs
```
1. l
2. 11111111
```

### Output Esperado
```
ÉXITO: Llegada registrada exitosamente
```

### Fecha de Ejecución
**09/11/2025 16:41:55**

### Output Obtenido
```
============================================================
           REGISTRAR LLEGADA DE PARTICIPANTE
============================================================
Ingrese el documento del participante: 11111111

 ÉXITO: Llegada registrada exitosamente


Participante: juan Perez
Evento: Workshop Integración
Ubicación: Centro

Presione Enter para continuar...

```
ahora si se obtuvo el resulado esperado

---

---

## PRUEBA 3: Validar rechazo de llegada duplicada

**Estado:** pass

### Descripción
Validar rechazo de llegada duplicada

### Inputs
```
1. l
2. 11111111
```

### Output Esperado
```
ADVERTENCIA: Participante ya registró su llegada
```

### Fecha de Ejecución
**09/11/2025 16:41:56**

### Output Obtenido
```
============================================================
           REGISTRAR LLEGADA DE PARTICIPANTE
============================================================
Ingrese el documento del participante: 11111111

  ADVERTENCIA: Participante ya registró su llegada


Presione Enter para continuar...
```

### Resumen de Correcciones
**Ninguna - Test pasó correctamente**

---

## PRUEBA 4: Validar rechazo de participante no inscrito

**Estado:**  FAIL

### Descripción
Validar rechazo de participante no inscrito

### Inputs
```
1. l
2. 22222222
```

### Output Esperado
```
ERROR: Participante no registrado
```

### Fecha de Ejecución
**09/11/2025 16:41:56**

### Output Obtenido
```
============================================================
           REGISTRAR LLEGADA DE PARTICIPANTE
============================================================
Ingrese el documento del participante: 22222222

 ERROR: Participante no registrado


Presione Enter para continuar...
```

### Resumen de Correcciones
**Ninguna - Test pasó correctamente**
---

## PRUEBA 5: Consultar lista de asistencia de un evento

**Estado:**  PASS

### Descripción
Consultar lista de asistencia de un evento

### Inputs
```
1. a
2. 1

```

### Output Esperado
```
Mostrar asistentes del evento
```

### Fecha de Ejecución
**09/11/2025 16:41:56**

### Output Obtenido
```
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
```

### Resumen de Correcciones
**Ninguna - Test pasó correctamente**

---

## PRUEBA 6: Registrar recurso material para evento

**Estado:** pass

### Descripción
Registrar recurso de material para evento

### Inputs
```
1. r
2. 1
3. 1
4. computadora
5. 3

```

### Output Esperado
```
uso de equipo registrado
```

### Fecha de Ejecución
**09/11/2025 16:41:56**

### Output Obtenido
```
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
```

### Resumen de Correcciones
**Ninguna - Test pasó correctamente**
---

## PRUEBA 7: Consultar la capacidad de la sala usada

**Estado:** pass

### Descripción
Ver la capacidad usada y espacios disponibles

### Inputs
```
1. r
2. 1
3. 2
```

### Output Esperado
```
Resultado de los espacios disponibles
```

### Fecha de Ejecución
**09/11/2025 16:41:56**

### Output Obtenido
```
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
**Ninguna - Test pasó correctamente**

---

## PRUEBA 8: Finalización de el evento 

**Estado:** PASS

### Descripción
Consultar recursos asignados a un evento

### Inputs
```
1. f
2. 1
3. s
```

### Output Esperado
```
Mostrar lista de recursos del evento
```

### Fecha de Ejecución
**09/11/2025 16:41:56**

### Output Obtenido
```
============================================================
           FINALIZAR EVENTO
============================================================
Ingrese el ID del evento: 1

============================================================
           RESUMEN FINAL DEL EVENTO
============================================================
Evento: Workshop Integración
Fecha: 09/11/2025

--- Asistencia ---
Total inscriptos: 2
Presentes: 2
Ausentes: 0
Porcentaje de asistencia: 100.00%

--- Recursos Utilizados ---
Total de recursos registrados: 2
  • Equipos: 1
  • Incidencias reportadas: 1

============================================================
¿Confirma finalización del evento? (S/N): s

 ÉXITO: Evento finalizado exitosamente


  El reporte final ha sido generado


Presione Enter para continuar...
```

### Resumen de Correcciones
**Ninguna - Test pasó correctamente**


---

**Sistema:** Sistema de Gestión de Eventos v1.0

