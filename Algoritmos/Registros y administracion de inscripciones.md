# Algoritmo de Registro y Administración de Inscripciones

## Algoritmo
1. Mostrar menú principal de inscripciones.
2. Solicitar al cliente que elija una opción.
3. Mostrar la interfaz correspondiente a la elección del cliente.
4. Leer la entrada o entradas del usuario. 
5. Mostrar salida correspondiente a las entradas.

## Nivel de Refinamiento 1

1. Mostrar menú principal con opciones disponibles.
2. Leer y validar la opción seleccionada por el usuario.
3. Ejecutar la funcionalidad correspondiente según la opción: 
   3.1. Registrar nueva inscripción: Verificar evento, participante y cupos disponibles.  
   3.2. Consultar inscripciones: Buscar y mostrar información según criterios.  
   3.3. Modificar inscripción: Actualizar datos de inscripción existente.  
   3.4. Cancelar inscripción: Procesar cancelación y liberar cupo.  
   3.5. Gestionar lista de espera: Administrar participantes en espera.  
4. Repetir el proceso hasta que el usuario decida salir.
5. Finalizar el módulo y retornar al menú principal.

----
## Nivel de Refinamiento 2

### Menú principal
```
1.1. Hacer lo siguiente mientras la opción del usuario no sea "S" (Salir):
    1.2. Mostrar en pantalla: '--- MENÚ DE INSCRIPCIONES ---'
    1.3. Mostrar en pantalla: 'Para registrar inscripción ingresar > R'
    1.4. Mostrar en pantalla: 'Para consultar inscripciones ingresar > C'
    1.5. Mostrar en pantalla: 'Para modificar inscripción ingresar > M'
    1.6. Mostrar en pantalla: 'Para cancelar inscripción ingresar > X'
    1.7. Mostrar en pantalla: 'Para gestionar lista de espera ingresar > L'
    1.8. Mostrar en pantalla: 'Para salir del módulo ingresar > S'
    1.9. Leer y guardar en 'Input' la entrada del usuario (convertir a mayúscula).
    1.10. Según el valor de Input:
        1.10.1 Caso "R":
            1.10.1.1 Ejecutar el subproceso "Registrar Nueva Inscripción".
        1.10.2 Caso "C":
            1.10.2.1 Ejecutar el subproceso "Consultar Inscripciones".
        1.10.3 Caso "M":
            1.10.3.1 Ejecutar el subproceso "Modificar Inscripción".
        1.10.4 Caso "X":
            1.10.4.1 Ejecutar el subproceso "Cancelar Inscripción".
        1.10.5 Caso "L":
            1.10.5.1 Ejecutar el subproceso "Gestionar Lista de Espera".
        1.10.6 Caso "S":
            1.10.6.1 Mostrar mensaje: 'Saliendo del módulo de inscripciones...'
        1.10.7 De lo contrario:
            1.10.7.1 Mostrar mensaje: 'Opción no válida. Intente nuevamente.'
1.11. Fin del bucle.
```

### 2. REGISTRAR NUEVA INSCRIPCIÓN
```
3.1.1 Mostrar en pantalla: 'Ingrese ID del evento:'
3.1.2 Leer y guardar en 'id_evento'
3.1.3 Verificar si el evento existe
3.1.4 Si evento no existe:
    3.1.4.1 Mostrar mensaje: 'Evento no encontrado'
    3.1.4.2 Terminar subproceso
3.1.5 Si evento existe:
    3.1.5.1 Mostrar información del evento
    3.1.5.2 Verificar si el evento está activo
    3.1.5.3 Si evento no está activo:
        3.1.5.3.1 Mostrar mensaje: 'El evento no está disponible para inscripciones'
        3.1.5.3.2 Terminar subproceso
3.1.6 Verificar capacidad disponible del evento
3.1.7 Si no hay cupos disponibles:
    2.1.7.1 Mostrar mensaje: 'Evento completo. ¿Desea agregarse a lista de espera? (S/N)'
    3.1.7.2 Leer respuesta
    3.1.7.3 Si respuesta = "S":
        3.1.7.3.1 Ejecutar subproceso "Agregar a Lista de Espera"
    3.1.7.4 Terminar subproceso
3.1.8 Si hay cupos disponibles:
    3.1.8.1 Mostrar en pantalla: 'Ingrese documento del participante:'
    3.1.8.2 Leer y guardar en 'documento'
    3.1.8.3 Verificar si el participante ya está registrado
    3.1.8.4 Si participante no existe:
        3.1.8.4.1 Ejecutar subproceso "Registrar Nuevo Participante"
    3.1.8.5 Si participante existe:
        3.1.8.5.1 Mostrar datos del participante
        3.1.8.5.2 Verificar si ya está inscrito en este evento
        3.1.8.5.3 Si ya está inscrito:
            3.1.8.5.3.1 Mostrar mensaje: 'El participante ya está inscrito en este evento'
            3.1.8.5.3.2 Terminar subproceso
3.1.9 Generar nuevo ID de inscripción
3.1.10 Establecer fecha_inscripcion = fecha_actual
3.1.11 Establecer estado = 'confirmada'
3.1.12 Establecer estado_pago = 'pendiente'
3.1.13 Guardar inscripción en la base de datos
3.1.14 Mostrar mensaje: 'Inscripción registrada exitosamente. ID: [ID_inscripcion]'
```

### 3. CONSULTAR INSCRIPCIONES
```
3.2.1 Mostrar en pantalla: '--- CONSULTA DE INSCRIPCIONES ---'
3.2.2 Mostrar en pantalla: 'Para ver por evento ingresar > E'
3.2.3. Mostrar en pantalla: 'Para ver por participante ingresar > P'
3.2.4. Mostrar en pantalla: 'Para ver todas las inscripciones ingresar > T'
3.2.5. Leer y guardar en 'opcion_consulta'
3.2.6. Según el valor de opcion_consulta:
    3.2.6.1. Caso "E":
        3.2.6.1.1. Mostrar en pantalla: 'Ingrese ID del evento:'
        3.2.6.1.2. Leer id_evento
        3.2.6.1.3. Buscar inscripciones por evento
        3.2.6.1.4. Mostrar lista de inscripciones del evento
    3.2.6.2. Caso "P":
        3.2.6.2.1. Mostrar en pantalla: 'Ingrese documento del participante:'
        3.2.6.2.2. Leer documento
        3.2.6.2.3. Buscar inscripciones por participante
        3.2.6.2.4. Mostrar lista de inscripciones del participante
    3.2.6.3. Caso "T":
        3.2.6.3.1. Obtener todas las inscripciones
        3.2.6.3.2. Mostrar lista completa de inscripciones
    3.2.6.4. De lo contrario:
        3.2.6.4.1. Mostrar mensaje: 'Opción no válida'
```

### 4. MODIFICAR INSCRIPCIÓN
```
3.3.1. Mostrar en pantalla: 'Ingrese ID de la inscripción a modificar:'
3.3.2. Leer y guardar en 'id_inscripcion'
3.3.3. Buscar inscripción por ID
3.3.4. Si inscripción no encontrada:
    3.3.4.1. Mostrar mensaje: 'Inscripción no encontrada'
    3.3.4.2. Terminar subproceso
3.3.5. Si inscripción encontrada:
    3.3.5.1. Mostrar información actual de la inscripción
    3.3.5.2. Mostrar opciones de modificación
    3.3.5.3. Leer opción del usuario
    3.3.5.4. Según la opción, solicitar nuevos datos
    3.3.5.5. Validar nuevos datos
    3.3.5.6. Actualizar inscripción en la base de datos
    3.3.5.7. Mostrar mensaje: 'Inscripción modificada exitosamente'
```

### 5. CANCELAR INSCRIPCIÓN
```
3.4.1. Mostrar en pantalla: 'Ingrese ID de la inscripción a cancelar:'
3.4.2. Leer y guardar en 'id_inscripcion'
3.4.3. Buscar inscripción por ID
3.4.4. Si inscripción no encontrada:
    3.4.4.1. Mostrar mensaje: 'Inscripción no encontrada'
    3.4.4.2. Terminar subproceso
3.4.5. Si inscripción encontrada:
    3.4.5.1. Verificar si el evento ya pasó
    3.4.5.2. Si evento ya pasó:
        3.4.5.2.1. Mostrar mensaje: 'No se puede cancelar. El evento ya se realizó'
        3.4.5.2.2. Terminar subproceso
    3.4.5.3. Verificar tiempo restante hasta el evento
    3.4.5.4. Si faltan menos de 24 horas:
        3.4.5.4.1. Mostrar mensaje: 'Cancelación tardía. Se aplicarán penalizaciones'
    3.4.5.5. Mostrar en pantalla: '¿Confirma la cancelación? (S/N):'
    3.4.5.6. Leer confirmación
    3.4.5.7. Si confirmación = "S":
        3.4.5.7.1. Cambiar estado a 'cancelada'
        3.4.5.7.2. Actualizar inscripción en la base de datos
        3.4.5.7.3. Liberar cupo en el evento
        3.4.5.7.4. Verificar si hay lista de espera
        3.4.5.7.5. Si hay lista de espera:
            3.4.5.7.5.1. Notificar al primer participante en espera
        3.4.5.7.6. Mostrar mensaje: 'Inscripción cancelada exitosamente'
    3.4.5.8. Si confirmación = "N":
        3.4.5.8.1. Mostrar mensaje: 'Operación cancelada'
```

### 6. GESTIONAR LISTA DE ESPERA
```
3.5.1. Mostrar en pantalla: 'Ingrese ID del evento:'
3.5.2. Leer y guardar en 'id_evento'
3.5.3. Verificar si el evento existe
3.5.4. Si evento no existe:
    3.5.4.1. Mostrar mensaje: 'Evento no encontrado'
    3.5.4.2. Terminar subproceso
3.5.5. Si evento existe:
    3.5.5.1. Obtener lista de espera del evento
    3.5.5.2. Si no hay participantes en espera:
        3.5.5.2.1. Mostrar mensaje: 'No hay participantes en lista de espera'
    3.5.5.3. Si hay participantes en espera:
        3.5.5.3.1. Mostrar lista de participantes en espera
        3.5.5.3.2. Mostrar opciones de gestión
        3.5.5.3.3. Permitir promover participantes a inscripción confirmada
```

----
## Pseudocodigo

```
Proceso Administracion_De_Inscripciones
INICIO
    opcion_usuario = ""
    MIENTRAS opcion_usuario <> "S" HACER
        Mostrar_Menu_Principal()
        LEER opcion_usuario
        opcion_usuario <- MAYUSCULA(opcion_usuario)
        SEGUN opcion_usuario HACER
            CASO "R": Proceso_Registrar_Inscripcion()
            CASO "C": Proceso_Consultar_Inscripciones()
            CASO "M": Proceso_Modificar_Inscripcion()
            CASO "X": Proceso_Cancelar_Inscripcion()
            CASO "L": Proceso_Gestionar_Lista_Espera()
            CASO "S": Mostrar_Mensaje("Saliendo del módulo...")
            DE LO CONTRARIO: Mostrar_Error("Opción no válida.")
        FIN SEGUN
    FIN MIENTRAS
FIN Proceso

//Menú

Funcion Proceso_Registrar_Inscripcion()
INICIO
    id_evento <- Solicitar_ID_Evento()
    SI NOT Validar_Evento_Para_Inscripcion(id_evento) ENTONCES RETORNAR
    SI NOT Hay_Cupos_Disponibles(id_evento) ENTONCES
        SI Usuario_Desea_Lista_Espera() ENTONCES
            documento <- Solicitar_Documento_Participante()
            Inscribir_En_Lista_Espera(id_evento, documento)
        FIN SI
        RETORNAR
    FIN SI
    documento <- Solicitar_Documento_Participante()
    id_participante <- Obtener_O_Registrar_Participante(documento)
    SI Participante_Ya_Inscrito(id_evento, id_participante) ENTONCES
        Mostrar_Error("El participante ya está inscrito en este evento.")
        RETORNAR
    FIN SI
    id_nueva_inscripcion<- Crear_Nueva_Inscripcion(id_evento, id_participante)
    Mostrar_Exito("Inscripción registrada correctamente.")
FIN Funcion

---------------------------------
Funcion Proceso_Consultar_Inscripciones()
INICIO
    tipo_consulta <- Solicitar_Tipo_Consulta_Inscripcion() // Devuelve "E", "P", o "T"
    SEGUN tipo_consulta HACER
        CASO "E":
            id_evento <- Solicitar_ID_Evento()
            Mostrar_Inscripciones_Por_Evento(id_evento)
        CASO "P":
            documento <- Solicitar_Documento_Participante()
            Mostrar_Inscripciones_Por_Participante(documento)
        CASO "T":
            Mostrar_Todas_Las_Inscripciones()
        DE LO CONTRARIO:
            Mostrar_Error("Opción de consulta no válida.")
    FIN SEGUN
FIN Funcion
--------------------------------

Funcion Proceso_Modificar_Inscripcion()
INICIO
    id_inscripcion <- Solicitar_ID_Inscripcion()
    SI NOT Existe_Inscripcion(id_inscripcion) ENTONCES
        Mostrar_Error("Inscripción no encontrada.")
        RETORNAR
    FIN SI
    opcion_mod <- Mostrar_Menu_Modificacion() // Devuelve qué modificar
    Ejecutar_Modificacion(id_inscripcion, opcion_mod)
    Mostrar_Exito("Inscripción modificada.")
FIN Funcion


Funcion Mostrar_Menu_Modificacion() : cadena
INICIO
    ESCRIBIR "--- Opciones de Modificación ---"
    ESCRIBIR "1. Cambiar de evento"
    ESCRIBIR "2. Actualizar datos del participante"
    ESCRIBIR "3. Cambiar estado de la inscripción (confirmada, pendiente, etc.)"
    ESCRIBIR "Seleccione una opción:"
    LEER opcion
    RETORNAR opcion
FIN Funcion

Funcion Ejecutar_Modificacion(id_inscripcion, opcion_mod)
INICIO
    info_inscripcion <- OBTENER_INFO_INSCRIPCION(id_inscripcion)
    SEGUN opcion_mod HACER
        CASO "1":
            Subproceso_Cambiar_Evento(id_inscripcion, info_inscripcion.id_evento, info_inscripcion.id_participante)
        CASO "2":
            Subproceso_Actualizar_Datos_Participante(info_inscripcion.id_participante)
        CASO "3":
            Subproceso_Cambiar_Estado_Inscripcion(id_inscripcion, info_inscripcion.id_evento)
        DE LO CONTRARIO:
            Mostrar_Error("Opción de modificación no válida.")
    FIN SEGUN
FIN Funcion

Funcion Subproceso_Cambiar_Evento(id_inscripcion, id_evento_actual, id_participante)
INICIO
    ESCRIBIR "Ingrese el ID del nuevo evento:"
    LEER id_evento_nuevo
    SI id_evento_nuevo = id_evento_actual ENTONCES
        Mostrar_Error("El nuevo evento es el mismo que el actual.")
        RETORNAR
    FIN SI
    SI NOT Validar_Evento_Para_Inscripcion(id_evento_nuevo) ENTONCES RETORNAR
    SI NOT Hay_Cupos_Disponibles(id_evento_nuevo) ENTONCES
        Mostrar_Error("El nuevo evento no tiene cupos disponibles.")
        RETORNAR
    FIN SI
    SI Participante_Ya_Inscrito(id_evento_nuevo, id_participante) ENTONCES
        Mostrar_Error("El participante ya está inscrito en el evento de destino.")
        RETORNAR
    FIN SI
    ACTUALIZAR_EVENTO_DE_INSCRIPCION(id_inscripcion, id_evento_nuevo)
    Liberar_Cupo_Y_Gestionar_Lista_Espera(id_evento_actual)
    Mostrar_Exito("El cambio de evento se realizó correctamente.")
FIN Funcion


Funcion Subproceso_Actualizar_Datos_Participante(id_participante)
INICIO
    info_participante <- OBTENER_INFO_PARTICIPANTE(id_participante)
    ESCRIBIR "Datos actuales: " + info_participante.nombre + ", " + info_participante.apellido + ", " + info_participante.email
    ESCRIBIR "¿Qué dato desea actualizar? (nombre, apellido, email, telefono)"
    LEER campo_a_actualizar
    ESCRIBIR "Ingrese el nuevo valor:"
    LEER nuevo_valor
    SI campo_a_actualizar ES VALIDO ENTONCES
        ACTUALIZAR_DATO_PARTICIPANTE(id_participante, campo_a_actualizar, nuevo_valor)
        Mostrar_Exito("Dato actualizado correctamente.")
    SINO
        Mostrar_Error("El campo a actualizar no es válido.")
    FIN SI
FIN Funcion


Funcion Subproceso_Cambiar_Estado_Inscripcion(id_inscripcion, id_evento)
INICIO
    ESCRIBIR "Ingrese el nuevo estado (confirmada, pendiente, cancelada):"
    LEER nuevo_estado
    SI nuevo_estado ES VALIDO ENTONCES
        SI nuevo_estado = "cancelada" ENTONCES
             Liberar_Cupo_Y_Gestionar_Lista_Espera(id_evento)
        FIN SI 
        ACTUALIZAR_ESTADO_INSCRIPCION(id_inscripcion, nuevo_estado)
        Mostrar_Exito("Estado de la inscripción actualizado.")
    SINO
        Mostrar_Error("El estado ingresado no es válido.")
    FIN SI
FIN Funcion


-------------------------

Funcion Proceso_Cancelar_Inscripcion()
INICIO
    id_inscripcion <- Solicitar_ID_Inscripcion()
    SI NOT Validar_Inscripcion_Para_Cancelacion(id_inscripcion) ENTONCES RETORNAR
    Mostrar_Advertencias_Cancelacion(id_inscripcion) // Ej: penalizaciones
    SI Usuario_Confirma_Operacion("¿Confirma la cancelación?") ENTONCES
        Actualizar_Estado_Inscripcion(id_inscripcion, "cancelada")
        id_evento <- Obtener_Evento_De_Inscripcion(id_inscripcion)
        Liberar_Cupo_Y_Gestionar_Lista_Espera(id_evento)
        Mostrar_Exito("Inscripción cancelada.")
    SINO
        Mostrar_Mensaje("Operación cancelada.")
    FIN SI
FIN Funcion


----------------------
Funcion Proceso_Gestionar_Lista_Espera()
INICIO
    id_evento <- Solicitar_ID_Evento()
    SI NOT Existe_Evento(id_evento) ENTONCES
        Mostrar_Error("Evento no encontrado.")
        RETORNAR
    FIN SI
    SI NOT Hay_Participantes_En_Espera(id_evento) ENTONCES
        Mostrar_Mensaje("No hay participantes en lista de espera.")
        RETORNAR
    FIN SI
    Mostrar_Lista_Espera(id_evento)
    opcion_gestion <- Mostrar_Menu_Gestion_Espera()
    Ejecutar_Gestion_Lista_Espera(id_evento, opcion_gestion)
FIN Funcion

Funcion Mostrar_Menu_Gestion_Espera() : cadena
INICIO
    ESCRIBIR "--- Opciones de Gestión de Lista de Espera ---"
    ESCRIBIR "1. Promover un participante a inscripción confirmada"
    ESCRIBIR "2. Eliminar un participante de la lista"
    ESCRIBIR "Seleccione una opción:"
    LEER opcion
    RETORNAR opcion
FIN Funcion


Funcion Ejecutar_Gestion_Lista_Espera(id_evento, opcion_gestion)
INICIO
    SEGUN opcion_gestion HACER
        CASO "1":
            Subproceso_Promover_Participante_Espera(id_evento)
        CASO "2":
            Subproceso_Eliminar_Participante_Espera(id_evento)
        DE LO CONTRARIO:
            Mostrar_Error("Opción de gestión no válida.")
    FIN SEGUN
FIN Funcion

Funcion Subproceso_Promover_Participante_Espera(id_evento)
INICIO
    SI NOT Hay_Cupos_Disponibles(id_evento) ENTONCES
        Mostrar_Error("No hay cupos disponibles para promover a un participante.")
        RETORNAR
    FIN SI
    
    ESCRIBIR "Ingrese la posición en la lista del participante a promover (Ej: 1 para el primero):"
    LEER posicion
    info_participante <- OBTENER_PARTICIPANTE_DE_LISTA_ESPERA(id_evento, posicion)
    SI info_participante = NULO ENTONCES
        Mostrar_Error("La posición ingresada no es válida.")
        RETORNAR
    FIN SI
    id_nueva_inscripcion <- Crear_Nueva_Inscripcion(id_evento, info_participante.id)
    ELIMINAR_PARTICIPANTE_LISTA_ESPERA(id_evento, info_participante.id)
    REORDENAR_POSICIONES_LISTA_ESPERA(id_evento)
    Mostrar_Exito("Participante promovido exitosamente. Nuevo ID de inscripción: " + id_nueva_inscripcion)
FIN Funcion

Funcion Subproceso_Eliminar_Participante_Espera(id_evento)
INICIO
    ESCRIBIR "Ingrese la posición del participante a eliminar de la lista:"
    LEER posicion
    info_participante <- OBTENER_PARTICIPANTE_DE_LISTA_ESPERA(id_evento, posicion)
    SI info_participante = NULO ENTONCES
        Mostrar_Error("La posición ingresada no es válida.")
        RETORNAR
    FIN SI
    SI Usuario_Confirma_Operacion("¿Confirma eliminar a " + info_participante.nombre + " de la lista?") ENTONCES
        ELIMINAR_PARTICIPANTE_LISTA_ESPERA(id_evento, info_participante.id)
        REORDENAR_POSICIONES_LISTA_ESPERA(id_evento)
        Mostrar_Exito("Participante eliminado de la lista de espera.")
    SINO
        Mostrar_Mensaje("Operación cancelada.")
    FIN SI
FIN Funcion
----------------------


Funcion Validar_Evento_Para_Inscripcion(id_evento) : booleano
INICIO
    SI NO EXISTE_EVENTO(id_evento) ENTONCES
        Mostrar_Error("Evento no encontrado.")
        RETORNAR FALSO
    FIN SI
    info_evento <- OBTENER_INFO_EVENTO(id_evento)
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


Funcion Validar_Inscripcion_Para_Cancelacion(id_inscripcion) : booleano
INICIO
    SI NOT Existe_Inscripcion(id_inscripcion) ENTONCES
        Mostrar_Error("Inscripción no encontrada.")
        RETORNAR FALSO
    FIN SI
    info_evento <- OBTENER_INFO_EVENTO_POR_INSCRIPCION(id_inscripcion)
    SI info_evento.fecha < FECHA_ACTUAL ENTONCES
        Mostrar_Error("No se puede cancelar. El evento ya se realizó.")
        RETORNAR FALSO
    FIN SI
    RETORNAR VERDADERO
FIN Funcion


Funcion Obtener_O_Registrar_Participante(documento) : entero
INICIO
    SI EXISTE_PARTICIPANTE(documento) ENTONCES
        id_participante <- OBTENER_ID_PARTICIPANTE(documento)
        RETORNAR id_participante
    SINO
        Mostrar_Mensaje("Participante no registrado. Se solicitarán datos adicionales.")
        id_nuevo_participante <- Registrar_Nuevo_Participante(documento)
        RETORNAR id_nuevo_participante
    FIN SI
FIN Funcion


Funcion Registrar_Nuevo_Participante(documento) : entero
INICIO
    ESCRIBIR 'Nombre:'
    LEER nombre
    ESCRIBIR 'Apellido:'
    LEER apellido
    ESCRIBIR 'Email:'
    LEER email
    ESCRIBIR 'Teléfono:'
    LEER telefono
    id_participante <- GUARDAR_PARTICIPANTE (nombre, apellido, email, telefono, documento)
    Mostrar_Exito("Participante registrado exitosamente.")
    RETORNAR id_participante
FIN Funcion


Funcion Crear_Nueva_Inscripcion(id_evento, id_participante) : entero
INICIO
    fecha_inscripcion <- FECHA_ACTUAL
    estado <- 'confirmada'
    estado_pago <- 'pendiente'
    id_nueva_inscripcion <- GUARDAR_INSCRIPCION(id_evento, id_participante, fecha_inscripcion, estado, estado_pago)                            
    RETORNAR id_nueva_inscripcion
FIN Funcion

Funcion Inscribir_En_Lista_Espera(id_evento, documento)
INICIO
    id_participante <- Obtener_O_Registrar_Participante(documento)
    SI YA_EN_LISTA_ESPERA(id_evento, id_participante) ENTONCES
        Mostrar_Error("El participante ya se encuentra en la lista de espera para este evento.")
        RETORNAR
    FIN SI
    posicion <- OBTENER_SIGUIENTE_POSICION_ESPERA(id_evento)
    AGREGAR_PARTICIPANTE_LISTA_ESPERA(id_evento, id_participante, posicion)
    Mostrar_Exito("Participante agregado a lista de espera en la posición: " + posicion)
FIN Funcion


Funcion Liberar_Cupo_Y_Gestionar_Lista_Espera(id_evento)
INICIO
    SI EXISTE_LISTA_ESPERA(id_evento) ENTONCES
        primer_participante <- OBTENER_PRIMER_PARTICIPANTE_ESPERA(id_evento)   
        SI primer_participante <> NULO ENTONCES
            Crear_Nueva_Inscripcion(id_evento, primer_participante.id)
            ELIMINAR_PARTICIPANTE_LISTA_ESPERA(id_evento, primer_participante.id)
            REORDENAR_POSICIONES_LISTA_ESPERA(id_evento)
            Mostrar_Mensaje("Se ha promovido a " + primer_participante.nombre + " desde la lista de espera.")
        FIN SI
    FIN SI
FIN Funcion


Funcion Solicitar_ID_Evento() : entero
    ESCRIBIR "Ingrese el ID del evento:"
    LEER id
    RETORNAR id
FIN Funcion


Funcion Solicitar_Documento_Participante() : cadena
    ESCRIBIR "Ingrese el documento del participante:"
    LEER documento
    RETORNAR documento
FIN Funcion


Funcion Solicitar_ID_Inscripcion() : entero
    ESCRIBIR "Ingrese el ID de la inscripción:"
    LEER id
    RETORNAR id
FIN Funcion


Funcion Usuario_Desea_Lista_Espera() : booleano
    ESCRIBIR "Evento completo. ¿Desea agregarse a la lista de espera? (S/N)"
    LEER respuesta
    RETORNAR (MAYUSCULA(respuesta) = "S")
FIN Funcion


Funcion Usuario_Confirma_Operacion(mensaje) : booleano
    ESCRIBIR mensaje + " (S/N):"
    LEER respuesta
    RETORNAR (MAYUSCULA(respuesta) = "S")
FIN Funcion


Funcion Mostrar_Advertencias_Cancelacion(id_inscripcion)
INICIO
    info_evento <- OBTENER_INFO_EVENTO_POR_INSCRIPCION(id_inscripcion)
    horas_restantes <- CALCULAR_HORAS_HASTA_EVENTO(info_evento.fecha)
    SI horas_restantes < 24 ENTONCES
        Mostrar_Advertencia("Cancelación tardía. Se podrían aplicar penalizaciones.")
    FIN SI
FIN Funcion