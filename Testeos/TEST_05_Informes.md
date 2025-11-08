# Generación de Informes y Estadísticas
## Sistema de Gestión de Eventos - Testing Completo

**Módulo:** Informes  
**Fecha de Ejecución:** 07/11/2025  
**Total de Tests:** 7  
**Tests Exitosos:** 6  
**Tests Fallidos:** 1  
**Tasa de Éxito:** 87.5%

---

## PRUEBA 1: Generar informe de asistencia de evento finalizado

**Estado:** PASS

### Descripción
Generar informe de asistencia de evento finalizado

### Inputs
```
1. f
2. a
3. conferencia testing
```

### Output Esperado
```
Informe con estadísticas de asistencia
```

### Fecha de Ejecución
**07/11/2025 16:41:57**

### Output Obtenido
```
============================================================
           INFORME DE ASISTENCIA
============================================================

Ingrese el nombre o parte del nombre del evento:
> conferencia testing

--- Eventos Coincidentes ---
1. Conferencia Testing 2025 (ID: 7) - 03/11/2025

Ingrese el número de la opción (0 para cancelar): 1

 Error inesperado: no such column: id_evento
Por favor, contacte al soporte técnico.
```

### Resumen de Correcciones
**Requiere corrección**

**Nota:** Este test falló por falta de un import 

 **Corrección:** corecciones en la linea 76, 133 y 175 y en realizacion_eventos linea 275 acerca de las consultas sql 
```
SELECT COUNT(*) as total FROM asistencia a
        JOIN inscripciones i ON a.id_inscripcion = i.id
        WHERE i.id_evento = ?


SELECT p.* FROM participantes p
        JOIN inscripciones i ON p.id = i.id_participante
        JOIN asistencia a ON i.id = a.id_inscripcion
        WHERE i.id_evento = ?        


SELECT e.*, 
               (SELECT COUNT(*) FROM inscripciones WHERE id_evento = e.id) as inscripciones,
               (SELECT COUNT(*) FROM asistencia a 
                JOIN inscripciones i ON a.id_inscripcion = i.id 
                WHERE i.id_evento = e.id) as asistentes
        FROM eventos e
        ORDER BY inscripciones DESC

 SELECT COUNT(*) as total FROM asistencia a
            JOIN inscripciones i ON a.id_inscripcion = i.id
            WHERE i.id_evento = ?
```

### Inputs
```
1. f
2. a
3. conferencia testing
4. 1
```

### Output Esperado
```
informe con estadísticas de asistencia
```

### Fecha de Ejecución
**07/11/2025 16:41:55**

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

```
ahora si se obtuvo el resulado esperado



---

## PRUEBA 2: Generar informe demográfico (género, país, edad)

**Estado:**  fail

### Descripción
Generar informe demográfico (género, país, edad)

### Inputs
```
1. d
2. conferencia testing
3. 1
```

### Output Esperado
```
Informe con distribución demográfica
```

### Fecha de Ejecución
**07/11/2025 16:41:57**

### Output Obtenido
```
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
```

### Resumen de Correcciones
**Ninguna - Test pasó correctamente**

---

## PRUEBA 3: Generar informe de nivel de interés (inscritos vs capacidad)

**Estado:** PASS

### Descripción
Generar informe de nivel de interés (inscritos vs capacidad)

### Inputs
```
1. i
```

### Output Esperado
```
Informe con tasa de ocupación
```

### Fecha de Ejecución
**07/11/2025 16:41:57**

### Output Obtenido
```
============================================================
           RANKING DE EVENTOS POR INTERÉS
============================================================

1. Workshop Integración
   Inscripciones: 3
   Asistentes: 0
   Ocupación: 6.0%
   ██

2. pruebas
   Inscripciones: 3
   Asistentes: 0
   Ocupación: 300.0%
   ████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████

3. Presentacion Ariel
   Inscripciones: 3
   Asistentes: 0
   Ocupación: 100.0%
   ████████████████████████████████████████

4. Conferencia Testing 2025
   Inscripciones: 3
   Asistentes: 2
   Ocupación: 6.0%
   ██

5. Evento Capacidad 1
   Inscripciones: 1
   Asistentes: 0
   Ocupación: 100.0%
   ████████████████████████████████████████

6. Evento Realización Full
   Inscripciones: 1
   Asistentes: 0
   Ocupación: 3.3%
   █

7. Conferencia Multi-Track
   Inscripciones: 0
   Asistentes: 0
   Ocupación: 0.0%
```

### Resumen de Correcciones
**Ninguna - Test pasó correctamente**

---

## PRUEBA 4: Generar informe de fidelización (participantes recurrentes)

**Estado:**  PASS

### Descripción
Generar informe de fidelización (participantes recurrentes)

### Inputs
```
1. f
```

### Output Esperado
```
Informe con participantes en múltiples eventos
```

### Fecha de Ejecución
**07/11/2025 16:41:57**

### Output Obtenido
```
============================================================
           ANÁLISIS DE FIDELIZACIÓN
============================================================
Total participantes únicos: 11
Participantes recurrentes: 2
Tasa de retorno: 18.18%

--- TOP 10 PARTICIPANTES MÁS ACTIVOS ---
1. juan Perez: 3 inscripciones
2. carlos perez: 2 inscripciones
3. Laura Rodriguez: 1 inscripciones
4. Pedro Martinez: 1 inscripciones
5. Ana Garcia: 1 inscripciones
6. Tomas Pertile: 1 inscripciones
7. Julian Vazquez: 1 inscripciones
8. ignacio anquerama: 1 inscripciones
9. Asistente Test: 1 inscripciones
10. Primero Usuario: 1 inscripciones

--- DISTRIBUCIÓN DE PARTICIPACIÓN ---
1 evento:     9 participantes
2 eventos:    1 participantes
3+ eventos:   1 participantes
```

### Resumen de Correcciones
**Ninguna - Test pasó correctamente**

---

## PRUEBA 5: Generar informe financiero de un evento específico

**Estado:**  PASS

### Descripción
Generar informe financiero de un evento específico

### Inputs
```
1. n
2. e
3. conferencia teting
4. 1
```

### Output Esperado
```
Informe con ingresos y pagos del evento
```

### Fecha de Ejecución
**07/11/2025 16:41:57**

### Output Obtenido
```
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

## PRUEBA 6: Generar informe financiero general (todos los eventos)

**Estado:**  PASS

### Descripción
Generar informe financiero general (todos los eventos)

### Inputs
```
1. n
2. g
```

### Output Esperado
```
Informe con resumen financiero global
```

### Fecha de Ejecución
**07/11/2025 16:41:57**

### Output Obtenido
```
============================================================
           REPORTE FINANCIERO GENERAL
============================================================
Total eventos registrados: 7
Total inscripciones: 14

--- PAGOS ---
Completados: 7
Pendientes: 7
Tasa de pago: 50.00%

--- INGRESOS ---
Ingresos totales: $30,300.00
Ingresos pendientes: $29,000.00
Total reembolsos: $0.00
Ingresos netos: $30,300.00

--- TOP 5 EVENTOS MÁS RENTABLES ---
1. Conferencia Testing 2025: $15,000.00
2. Presentacion Ariel: $10,000.00
3. Workshop Integración: $2,500.00
4. Evento Realización Full: $1,800.00
5. pruebas: $1,000.00
```

### Resumen de Correcciones
**Ninguna - Test pasó correctamente**

---

## PRUEBA 7: Validar rechazo de informe para evento no finalizado

**Estado:**  PASS

### Descripción
Validar rechazo de informe para evento no finalizado

### Inputs
```
1. a
2. presentacion ariel
```

### Output Esperado
```
ERROR: No se encontraron eventos finalizados con ese criterio
```

### Fecha de Ejecución
**07/11/2025 16:41:58**

### Output Obtenido
```
============================================================
           INFORME DE ASISTENCIA
============================================================

Ingrese el nombre o parte del nombre del evento:
> Presentacion Ariel

 ERROR: No se encontraron eventos finalizados con ese criterio
```

### Resumen de Correcciones
**Ninguna - Test pasó correctamente**

---

**Documento generado automáticamente el 07/11/2025**  
**Sistema:** Sistema de Gestión de Eventos v1.0

