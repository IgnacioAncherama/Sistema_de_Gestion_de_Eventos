# PRIMERA ENTREGA - SISTEMA DE GESTIÓN DE EVENTOS
**Equipo N°5**

## INTEGRANTES
- **Gestión de Eventos**: Ignacio Ancherama
- **Registro y administración de inscripciones**: Sebastian Stefanelli  
- **Administración de pagos y cobros**: Joaquin Landra
- **Realización del Evento**: Julian Vazquez
- **Generación de Informes**: Milagros Trotta

---

## 1. RELEVAMIENTO

### 1.1 Problemática
Una empresa organizadora de eventos necesita un sistema integral para gestionar todo el ciclo de vida de sus eventos, desde la planificación inicial hasta la generación de informes post-evento. Actualmente, la gestión se realiza de forma manual y desorganizada, lo que genera:

- **Pérdida de información** sobre inscripciones y pagos
- **Dificultades en el control** de asistencia y capacidad
- **Problemas de comunicación** con los participantes
- **Falta de seguimiento** financiero en tiempo real
- **Imposibilidad de generar reportes** precisos y oportunos

### 1.2 Objetivos del Sistema

#### Objetivo General
Desarrollar un sistema informático que permita gestionar de manera integral todos los aspectos relacionados con la organización y realización de eventos.

#### Objetivos Específicos
1. **Gestionar eventos**: Crear, modificar, consultar y eliminar eventos
2. **Administrar inscripciones**: Registrar participantes y controlar cupos
3. **Controlar pagos**: Gestionar cobros, pagos y estado financiero
4. **Facilitar la realización**: Controlar asistencia y recursos durante el evento
5. **Generar informes**: Producir reportes estadísticos y de gestión

### 1.3 Alcance del Sistema

#### Funcionalidades Incluidas:
- Gestión completa del catálogo de eventos
- Registro y administración de participantes con validaciones
- Control de pagos y estados financieros
- Gestión de asistencia en tiempo real
- Generación de informes y estadísticas

#### Funcionalidades NO Incluidas:
- Integración con sistemas de pago externos
- Notificaciones automáticas por email/SMS
- Gestión de recursos físicos (salas, equipos)
- Sistema de calificaciones o feedback

---

## 2. ANÁLISIS

### 2.1 Análisis de Requerimientos

#### Requerimientos Funcionales

**RF01 - Gestión de Eventos**
- El sistema debe permitir crear nuevos eventos con toda su información
- Debe permitir consultar eventos existentes
- Debe permitir modificar datos de eventos
- Debe permitir eliminar eventos (con validaciones)

**RF02 - Gestión de Inscripciones**
- El sistema debe registrar participantes en eventos
- Debe validar disponibilidad de cupos
- Debe mantener listas de espera cuando sea necesario
- Debe permitir cancelar inscripciones

**RF03 - Gestión de Pagos**
- El sistema debe registrar pagos realizados
- Debe controlar estados de pago de cada participante
- Debe generar recordatorios de pagos pendientes
- Debe permitir diferentes métodos de pago

**RF04 - Realización del Evento**
- El sistema debe controlar asistencia en tiempo real
- Debe permitir registro de llegada de participantes
- Debe generar listas de asistencia
- Debe controlar recursos utilizados

**RF05 - Generación de Informes**
- El sistema debe generar reportes de inscripciones
- Debe generar reportes financieros
- Debe generar estadísticas de asistencia
- Debe permitir exportar información

#### Requerimientos No Funcionales

**RNF01 - Usabilidad**
- La interfaz debe ser intuitiva y fácil de usar
- Los tiempos de respuesta deben ser menores a 3 segundos

**RNF02 - Confiabilidad**
- El sistema debe mantener la integridad de los datos
- Debe tener mecanismos de validación de información

**RNF03 - Mantenibilidad**
- El código debe estar bien documentado
- Debe tener una estructura modular clara

### 2.2 Análisis de Actores

#### Actor Principal: Administrador del Sistema
- **Responsabilidades**: Gestión completa del sistema
- **Permisos**: Acceso total a todas las funcionalidades

#### Actor Secundario: Operador de Eventos
- **Responsabilidades**: Gestión operativa de eventos específicos
- **Permisos**: Acceso limitado según evento asignado

#### Actor Externo: Participante
- **Responsabilidades**: Proporcionar información para inscripción
- **Permisos**: Solo consulta de su información personal

### 2.3 Análisis de Casos de Uso Principales

1. **Crear Evento**: El administrador define un nuevo evento con todos sus parámetros
2. **Inscribir Participante**: Se registra un participante en un evento específico
3. **Procesar Pago**: Se registra un pago y se actualiza el estado del participante
4. **Controlar Asistencia**: Durante el evento se registra la asistencia
5. **Generar Reporte**: Se produce un informe según criterios específicos

---

## 3. DISEÑO

### 3.1 Arquitectura del Sistema

El sistema seguirá una arquitectura modular con 5 módulos principales:

```
┌─────────────────────────────────────────────┐
│           SISTEMA PRINCIPAL                 │
├─────────────────────────────────────────────┤
│  ┌─────────────┐  ┌─────────────────────┐   │
│  │   GESTIÓN   │  │     REGISTRO E      │   │
│  │     DE      │  │   ADMINISTRACIÓN    │   │
│  │   EVENTOS   │  │  DE INSCRIPCIONES   │   │
│  └─────────────┘  └─────────────────────┘   │
│                                             │
│  ┌─────────────┐  ┌─────────────────────┐   │
│  │ADMINISTRACIÓN│  │    REALIZACIÓN     │   │
│  │  DE PAGOS   │  │    DEL EVENTO      │   │
│  │  Y COBROS   │  │                    │   │
│  └─────────────┘  └─────────────────────┘   │
│                                             │
│  ┌─────────────────────────────────────────┐ │
│  │        GENERACIÓN DE INFORMES          │ │
│  │         Y ESTADÍSTICAS                 │ │
│  └─────────────────────────────────────────┘ │
└─────────────────────────────────────────────┘
```

### 3.2 Diseño de Datos

#### Estructura de Datos Principal

**Evento**
```
Evento {
    - id: entero
    - nombre: cadena
    - descripcion: cadena
    - fecha: fecha
    - hora_inicio: hora
    - hora_fin: hora
    - ubicacion: cadena
    - capacidad_maxima: entero
    - precio: real
    - estado: cadena (activo/inactivo/finalizado)
}
```

**Participante**
```
Participante {
    - id: entero
    - nombre: cadena
    - apellido: cadena
    - email: cadena
    - telefono: cadena
    - documento: cadena
    - fecha_nacimiento: fecha
}
```

**Inscripción**
```
Inscripcion {
    - id: entero
    - id_evento: entero
    - id_participante: entero
    - fecha_inscripcion: fecha
    - estado: cadena (confirmada/pendiente/cancelada)
    - estado_pago: cadena (pagado/pendiente/vencido)
}
```

**Pago**
```
Pago {
    - id: entero
    - id_inscripcion: entero
    - monto: real
    - fecha_pago: fecha
    - metodo_pago: cadena
    - estado: cadena (confirmado/pendiente/rechazado)
}
```

**Asistencia**
```
Asistencia {
    - id: entero
    - id_inscripcion: entero
    - fecha_hora_llegada: fecha_hora
    - presente: booleano
}
```

### 3.3 Diseño de Interfaces

#### Interfaz Principal
- **Menú Principal**: Acceso a los 5 módulos principales
- **Panel de Control**: Resumen de estado general del sistema
- **Navegación**: Estructura jerárquica clara entre módulos

#### Interfaces por Módulo
1. **Gestión de Eventos**: CRUD completo de eventos
2. **Inscripciones**: Formularios de registro y gestión
3. **Pagos**: Panel de control financiero
4. **Realización**: Interface de control en tiempo real
5. **Informes**: Generador de reportes con filtros

### 3.4 Diseño de Flujo de Trabajo

```
1. CREACIÓN DE EVENTO
   ↓
2. APERTURA DE INSCRIPCIONES
   ↓
3. REGISTRO DE PARTICIPANTES
   ↓
4. PROCESAMIENTO DE PAGOS
   ↓
5. REALIZACIÓN DEL EVENTO
   ↓
6. GENERACIÓN DE INFORMES
```

### 3.5 Validaciones y Reglas de Negocio

#### Reglas Principales:
1. **Capacidad**: No se pueden inscribir más participantes que la capacidad máxima
2. **Fechas**: No se pueden crear eventos en fechas pasadas
3. **Pagos**: El pago debe realizarse antes del evento
4. **Cancelaciones**: Las cancelaciones deben realizarse con 24hs de anticipación
5. **Asistencia**: Solo se puede registrar asistencia el día del evento

---

## 4. CONSIDERACIONES TÉCNICAS

### 4.1 Manejo de Errores
- Validación de datos de entrada
- Manejo de excepciones
- Mensajes de error claros para el usuario
- Log de errores para debugging

---

## 5. CONCLUSIONES

El Sistema de Gestión de Eventos propuesto permitirá:

1. **Centralizar** toda la información relacionada con eventos
2. **Automatizar** procesos manuales propensos a errores
3. **Mejorar** el control y seguimiento de inscripciones y pagos
4. **Facilitar** la toma de decisiones mediante informes precisos
5. **Optimizar** los recursos durante la realización de eventos

La arquitectura modular propuesta permite un desarrollo incremental y facilita el mantenimiento futuro del sistema.

