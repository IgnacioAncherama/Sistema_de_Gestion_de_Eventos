# Módulo de Funciones Comunes
## Sistema de Gestión de Eventos

Este módulo contiene funciones compartidas que son utilizadas por todos los módulos del sistema.

---

## Índice de Funciones

### 1. Funciones de Validación
- `Existe_Evento(id_evento)`
- `Existe_Participante(documento)`
- `Existe_Inscripcion(id_inscripcion)`
- `Validar_Evento_Activo(id_evento)`
- `Validar_Evento_Finalizado(id_evento)`

### 2. Funciones de Solicitud de Datos
- `Solicitar_ID_Evento()`
- `Solicitar_Documento_Participante()`
- `Solicitar_ID_Inscripcion()`

### 3. Funciones de Obtención de Información
- `Obtener_Info_Evento(id_evento)`
- `Obtener_Info_Participante(id_participante)`
- `Obtener_Info_Inscripcion(id_inscripcion)`
- `Obtener_Evento_De_Inscripcion(id_inscripcion)`

### 4. Funciones de Interacción con Usuario
- `Usuario_Confirma_Operacion(mensaje)`
- `Mostrar_Error(mensaje)`
- `Mostrar_Exito(mensaje)`
- `Mostrar_Mensaje(mensaje)`
- `Mostrar_Advertencia(mensaje)`

### 5. Funciones de Utilidad
- `Hay_Cupos_Disponibles(id_evento)`
- `Participante_Ya_Inscrito(id_evento, id_participante)`
- `Actualizar_Estado_Inscripcion(id_inscripcion, nuevo_estado)`

---

## Pseudocódigo de Funciones Comunes

```
// 1. FUNCIONES DE VALIDACIÓN


Funcion Existe_Evento(id_evento) : booleano
INICIO
    SI BUSCAR_EN_BD_EVENTOS(id_evento) <> NULO ENTONCES
        RETORNAR VERDADERO
    SINO
        RETORNAR FALSO
    FIN SI
FIN Funcion


Funcion Existe_Participante(documento) : booleano
INICIO
    SI BUSCAR_EN_BD_PARTICIPANTES(documento) <> NULO ENTONCES
        RETORNAR VERDADERO
    SINO
        RETORNAR FALSO
    FIN SI
FIN Funcion


Funcion Existe_Inscripcion(id_inscripcion) : booleano
INICIO
    SI BUSCAR_EN_BD_INSCRIPCIONES(id_inscripcion) <> NULO ENTONCES
        RETORNAR VERDADERO
    SINO
        RETORNAR FALSO
    FIN SI
FIN Funcion


Funcion Validar_Evento_Activo(id_evento) : booleano
// Valida que el evento existe, está activo y es futuro
// Se usa para: inscripciones, modificaciones
INICIO
    SI NOT Existe_Evento(id_evento) ENTONCES
        Mostrar_Error("Evento no encontrado.")
        RETORNAR FALSO
    FIN SI
    
    info_evento <- Obtener_Info_Evento(id_evento)
    
    SI info_evento.estado <> "activo" ENTONCES
        Mostrar_Error("El evento no está disponible para inscripciones.")
        RETORNAR FALSO
    FIN SI
    
    SI info_evento.fecha < FECHA_ACTUAL ENTONCES
        Mostrar_Error("Este evento ya se ha realizado.")
        RETORNAR FALSO
    FIN SI
    
    RETORNAR VERDADERO
FIN Funcion


Funcion Validar_Evento_Finalizado(id_evento) : booleano
// Valida que el evento existe y ya finalizó
// Se usa para: generación de informes
INICIO
    SI NOT Existe_Evento(id_evento) ENTONCES
        Mostrar_Error("Evento no encontrado.")
        RETORNAR FALSO
    FIN SI
    
    info_evento <- Obtener_Info_Evento(id_evento)
    
    SI info_evento.fecha > FECHA_ACTUAL ENTONCES
        Mostrar_Error("El informe solo puede generarse para eventos que ya han finalizado.")
        RETORNAR FALSO
    FIN SI
    
    RETORNAR VERDADERO
FIN Funcion


Funcion Validar_Inscripcion_Para_Cancelacion(id_inscripcion) : booleano
// Valida que la inscripción existe y el evento no ha pasado
INICIO
    SI NOT Existe_Inscripcion(id_inscripcion) ENTONCES
        Mostrar_Error("Inscripción no encontrada.")
        RETORNAR FALSO
    FIN SI
    
    id_evento <- Obtener_Evento_De_Inscripcion(id_inscripcion)
    info_evento <- Obtener_Info_Evento(id_evento)
    
    SI info_evento.fecha < FECHA_ACTUAL ENTONCES
        Mostrar_Error("No se puede cancelar. El evento ya se realizó.")
        RETORNAR FALSO
    FIN SI
    
    RETORNAR VERDADERO
FIN Funcion



// 2. FUNCIONES DE SOLICITUD DE DATOS


Funcion Solicitar_ID_Evento() : entero
INICIO
    ESCRIBIR "Ingrese el ID del evento:"
    LEER id
    RETORNAR id
FIN Funcion


Funcion Solicitar_Documento_Participante() : cadena
INICIO
    ESCRIBIR "Ingrese el documento del participante:"
    LEER documento
    RETORNAR documento
FIN Funcion


Funcion Solicitar_ID_Inscripcion() : entero
INICIO
    ESCRIBIR "Ingrese el ID de la inscripción:"
    LEER id
    RETORNAR id
FIN Funcion



// 3. FUNCIONES DE OBTENCIÓN DE INFORMACIÓN


Funcion Obtener_Info_Evento(id_evento) : registro
// Retorna un registro con toda la información del evento
// {id, nombre, descripcion, fecha, hora_inicio, hora_fin, ubicacion, capacidad_maxima, precio, estado}
INICIO
    info <- BUSCAR_EN_BD_EVENTOS(id_evento)
    RETORNAR info
FIN Funcion


Funcion Obtener_Info_Participante(id_participante) : registro
// Retorna un registro con toda la información del participante
// {id, nombre, apellido, documento, email, telefono}
INICIO
    info <- BUSCAR_EN_BD_PARTICIPANTES(id_participante)
    RETORNAR info
FIN Funcion


Funcion Obtener_Info_Inscripcion(id_inscripcion) : registro
// Retorna un registro con toda la información de la inscripción
// {id, id_evento, id_participante, fecha_inscripcion, estado, estado_pago}
INICIO
    info <- BUSCAR_EN_BD_INSCRIPCIONES(id_inscripcion)
    RETORNAR info
FIN Funcion


Funcion Obtener_Evento_De_Inscripcion(id_inscripcion) : entero
// Retorna el ID del evento asociado a una inscripción
INICIO
    info_inscripcion <- Obtener_Info_Inscripcion(id_inscripcion)
    RETORNAR info_inscripcion.id_evento
FIN Funcion


Funcion Obtener_ID_Participante(documento) : entero
// Retorna el ID del participante a partir de su documento
INICIO
    info <- BUSCAR_EN_BD_PARTICIPANTES_POR_DOCUMENTO(documento)
    SI info <> NULO ENTONCES
        RETORNAR info.id
    SINO
        RETORNAR 0
    FIN SI
FIN Funcion


// 4. FUNCIONES DE INTERACCIÓN CON USUARIO


Funcion Usuario_Confirma_Operacion(mensaje) : booleano
// Solicita confirmación del usuario para una operación
INICIO
    ESCRIBIR mensaje + " (S/N):"
    LEER respuesta
    RETORNAR (MAYUSCULA(respuesta) = "S")
FIN Funcion


Funcion Mostrar_Error(mensaje)
// Muestra un mensaje de error en pantalla
INICIO
    ESCRIBIR " ERROR: " + mensaje
FIN Funcion


Funcion Mostrar_Exito(mensaje)
// Muestra un mensaje de éxito en pantalla
INICIO
    ESCRIBIR " ÉXITO: " + mensaje
FIN Funcion


Funcion Mostrar_Mensaje(mensaje)
// Muestra un mensaje informativo en pantalla
INICIO
    ESCRIBIR mensaje
FIN Funcion


Funcion Mostrar_Advertencia(mensaje)
// Muestra un mensaje de advertencia en pantalla
INICIO
    ESCRIBIR " ADVERTENCIA: " + mensaje
FIN Funcion


// 5. FUNCIONES DE UTILIDAD


Funcion Hay_Cupos_Disponibles(id_evento) : booleano
// Verifica si el evento tiene cupos disponibles
INICIO
    info_evento <- Obtener_Info_Evento(id_evento)
    inscripciones_confirmadas <- CONTAR_INSCRIPCIONES_CONFIRMADAS(id_evento)
    
    SI inscripciones_confirmadas < info_evento.capacidad_maxima ENTONCES
        RETORNAR VERDADERO
    SINO
        RETORNAR FALSO
    FIN SI
FIN Funcion


Funcion Participante_Ya_Inscrito(id_evento, id_participante) : booleano
// Verifica si un participante ya está inscrito en un evento
INICIO
    inscripcion <- BUSCAR_INSCRIPCION_ACTIVA(id_evento, id_participante)
    SI inscripcion <> NULO ENTONCES
        RETORNAR VERDADERO
    SINO
        RETORNAR FALSO
    FIN SI
FIN Funcion


Funcion Actualizar_Estado_Inscripcion(id_inscripcion, nuevo_estado)
// Actualiza el estado de una inscripción en la base de datos
INICIO
    ACTUALIZAR_EN_BD_INSCRIPCIONES(id_inscripcion, "estado", nuevo_estado)
    Mostrar_Exito("Estado de inscripción actualizado a: " + nuevo_estado)
FIN Funcion


Funcion Obtener_Cupos_Disponibles(id_evento) : entero
// Retorna la cantidad de cupos disponibles en un evento
INICIO
    info_evento <- Obtener_Info_Evento(id_evento)
    inscripciones_confirmadas <- CONTAR_INSCRIPCIONES_CONFIRMADAS(id_evento)
    cupos_disponibles <- info_evento.capacidad_maxima - inscripciones_confirmadas
    RETORNAR cupos_disponibles
FIN Funcion


Funcion Hay_Participantes_En_Espera(id_evento) : booleano
// Verifica si hay participantes en la lista de espera de un evento
INICIO
    cantidad <- CONTAR_PARTICIPANTES_EN_LISTA_ESPERA(id_evento)
    SI cantidad > 0 ENTONCES
        RETORNAR VERDADERO
    SINO
        RETORNAR FALSO
    FIN SI
FIN Funcion



// 6. FUNCIONES DE OPERACIONES CON BD (ABSTRACTAS)

// Estas son las funciones de base de datos que cada implementación
// debe proporcionar. Se documentan aquí para referencia.

// BUSCAR_EN_BD_EVENTOS(id_evento) : registro
// BUSCAR_EN_BD_PARTICIPANTES(documento) : registro
// BUSCAR_EN_BD_INSCRIPCIONES(id_inscripcion) : registro
// BUSCAR_EN_BD_PARTICIPANTES_POR_DOCUMENTO(documento) : registro
// BUSCAR_INSCRIPCION_ACTIVA(id_evento, id_participante) : registro
// CONTAR_INSCRIPCIONES_CONFIRMADAS(id_evento) : entero
// CONTAR_PARTICIPANTES_EN_LISTA_ESPERA(id_evento) : entero
// ACTUALIZAR_EN_BD_INSCRIPCIONES(id_inscripcion, campo, valor)
// GUARDAR_EVENTO(...) : entero
// GUARDAR_PARTICIPANTE(...) : entero
// GUARDAR_INSCRIPCION(...) : entero

```

---

## Notas de Implementación

1. **Convención de Nombres**: Todas las funciones comunes usan PascalCase con guiones bajos.
2. **Manejo de Errores**: Las funciones de validación ya incluyen los mensajes de error, por lo que no es necesario repetirlos en los módulos que las llaman.
3. **Retornos Consistentes**: 
   - Funciones de validación retornan booleano
   - Funciones de obtención retornan el tipo de dato correspondiente o 0/NULO si no existe
4. **Abstracción de BD**: Las funciones que acceden a la base de datos están en MAYÚSCULAS para indicar que son operaciones de bajo nivel.

---


## Ventajas de Este Módulo

**Reutilización**: Código escrito una vez, usado en múltiples lugares  
**Mantenimiento**: Un solo lugar para actualizar la lógica  
**Consistencia**: Mismo comportamiento en todos los módulos  
**Legibilidad**: Nombres descriptivos y claros  
**Facilita Testing**: Funciones independientes más fáciles de probar

