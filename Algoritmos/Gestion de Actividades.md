# Algoritmo de Sistema de Gestión de Eventos
## Módulo de Gestión de Actividades
---

## Descripción
Este módulo maneja la creación, consulta, modificación y eliminación de actividades dentro de eventos.
Las actividades son subcomponentes de los eventos con horarios específicos.

---

## Algoritmo General

1. Mostrar el menú principal de gestión de actividades.
2. Solicitar al usuario que elija una opción.
3. Leer y validar la entrada del usuario.
4. Procesar la funcionalidad correspondiente según la opción.
5. Volver al menú principal hasta que el usuario decida salir.

### Nivel de Refinamiento 1

```
1. Mostrar menú principal con las opciones disponibles.
2. Leer y validar la opción seleccionada por el usuario.
3. Ejecutar la funcionalidad correspondiente según la opción:
   3.1. Crear Actividad: Registrar una nueva actividad para un evento.
   3.2. Consultar Actividades: Ver actividades por evento o todas.
   3.3. Modificar Actividad: Actualizar datos de una actividad existente.
   3.4. Eliminar Actividad: Borrar una actividad del sistema.
4. Repetir el proceso hasta que el usuario decida salir.
5. Finalizar el módulo y retornar al menú principal.
```

### Nivel de Refinamiento 2

#### **MENÚ PRINCIPAL**
```
1.1. Hacer lo siguiente mientras la opción del usuario no sea "S" (Salir):
1.2. Mostrar en pantalla: '--- MENÚ GESTIÓN DE ACTIVIDADES ---'
1.3. Mostrar en pantalla: 'Para crear actividad ingresar > C'
1.4. Mostrar en pantalla: 'Para consultar actividades ingresar > M'
1.5. Mostrar en pantalla: 'Para modificar actividad ingresar > X'
1.6. Mostrar en pantalla: 'Para eliminar actividad ingresar > E'
1.7. Mostrar en pantalla: 'Para salir del módulo ingresar > S'
1.8. Leer y guardar en 'Input' la entrada del usuario (convertir a mayúscula).
1.9. Según el valor de Input:
    1.9.1. Caso "C": Ejecutar el subproceso "Crear Actividad"
    1.9.2. Caso "M": Ejecutar el subproceso "Consultar Actividades"
    1.9.3. Caso "X": Ejecutar el subproceso "Modificar Actividad"
    1.9.4. Caso "E": Ejecutar el subproceso "Eliminar Actividad"
    1.9.5. Caso "S": Mostrar mensaje: 'Saliendo del módulo de actividades...'
    1.9.6. De lo contrario: Mostrar mensaje: 'Opción no válida. Intente nuevamente.'
1.10. Fin del bucle.
```

#### **2. CREAR ACTIVIDAD**
```
2.1. Solicitar ID del evento usando Solicitar_ID_Evento()
2.2. Verificar que el evento existe usando Existe_Evento(id_evento)
2.3. Si el evento no existe:
    2.3.1. Mostrar error "Evento no encontrado"
    2.3.2. Terminar subproceso
2.4. Si el evento existe:
    2.4.1. Obtener información del evento usando Obtener_Info_Evento(id_evento)
    2.4.2. Mostrar horario del evento
    2.4.3. Solicitar nombre de la actividad
    2.4.4. Solicitar descripción de la actividad
    2.4.5. Solicitar hora de inicio usando Solicitar_Hora()
    2.4.6. Solicitar hora de fin usando Solicitar_Hora()
    2.4.7. Validar que hora_fin > hora_inicio usando Validar_Rango_Horario()
    2.4.8. Si el rango no es válido:
        2.4.8.1. Mostrar error "La hora de fin debe ser posterior a la de inicio"
        2.4.8.2. Terminar subproceso
    2.4.9. Validar que hora_inicio esté dentro del horario del evento usando Validar_Hora_En_Rango()
    2.4.10. Si hora_inicio está fuera del rango:
        2.4.10.1. Mostrar error indicando el rango válido
        2.4.10.2. Terminar subproceso
    2.4.11. Validar que hora_fin esté dentro del horario del evento
    2.4.12. Si hora_fin está fuera del rango:
        2.4.12.1. Mostrar error indicando el rango válido
        2.4.12.2. Terminar subproceso
    2.4.13. Solicitar ubicación específica
    2.4.14. Solicitar capacidad usando Solicitar_Cantidad_Positiva()
    2.4.15. Guardar actividad en la base de datos
    2.4.16. Mostrar mensaje de éxito con el ID de la actividad creada
```

#### **3. CONSULTAR ACTIVIDADES**
```
3.1. Mostrar submenu de consulta
3.2. Mostrar opciones:
    - E: Ver actividades por evento
    - T: Ver todas las actividades
    - S: Volver
3.3. Leer opción del usuario
3.4. Según la opción:
    3.4.1. Caso "E":
        3.4.1.1. Solicitar ID del evento
        3.4.1.2. Verificar que el evento existe
        3.4.1.3. Obtener actividades del evento
        3.4.1.4. Mostrar lista de actividades
    3.4.2. Caso "T":
        3.4.2.1. Obtener todas las actividades
        3.4.2.2. Mostrar lista completa con nombre del evento
    3.4.3. Caso "S":
        3.4.3.1. Volver al menú principal
```

#### **4. MODIFICAR ACTIVIDAD**
```
4.1. Solicitar ID de la actividad
4.2. Verificar que la actividad existe usando Existe_Actividad(id_actividad)
4.3. Si no existe:
    4.3.1. Mostrar error "Actividad no encontrada"
    4.3.2. Terminar subproceso
4.4. Si existe:
    4.4.1. Obtener información de la actividad
    4.4.2. Mostrar información actual
    4.4.3. Mostrar opciones de modificación:
        - N: Nombre
        - D: Descripción
        - H: Horario
        - U: Ubicación
        - C: Capacidad
    4.4.4. Leer opción del usuario
    4.4.5. Según la opción:
        4.4.5.1. Caso "N":
            - Solicitar nuevo nombre
            - Actualizar si no está vacío
        4.4.5.2. Caso "D":
            - Solicitar nueva descripción
            - Actualizar
        4.4.5.3. Caso "H":
            - Obtener horario del evento padre
            - Solicitar nueva hora de inicio con Solicitar_Hora()
            - Solicitar nueva hora de fin con Solicitar_Hora()
            - Validar rango horario
            - Validar que estén dentro del horario del evento
            - Actualizar si es válido
        4.4.5.4. Caso "U":
            - Solicitar nueva ubicación
            - Actualizar
        4.4.5.5. Caso "C":
            - Solicitar nueva capacidad con Solicitar_Cantidad_Positiva()
            - Actualizar
    4.4.6. Mostrar mensaje de éxito
```

#### **5. ELIMINAR ACTIVIDAD**
```
5.1. Solicitar ID de la actividad
5.2. Verificar que la actividad existe
5.3. Si no existe:
    5.3.1. Mostrar error "Actividad no encontrada"
    5.3.2. Terminar subproceso
5.4. Si existe:
    5.4.1. Obtener información de la actividad
    5.4.2. Mostrar nombre de la actividad
    5.4.3. Solicitar confirmación usando Usuario_Confirma_Operacion()
    5.4.4. Si confirma:
        5.4.4.1. Eliminar actividad de la base de datos
        5.4.4.2. Mostrar mensaje de éxito
    5.4.5. Si no confirma:
        5.4.5.1. Mostrar mensaje "Operación cancelada"
```

---

## Pseudocódigo

```pseudocode
Funcion Menu_Principal_Actividades()
INICIO
    REPETIR
        Limpiar_Pantalla()
        ESCRIBIR "==================================================="
        ESCRIBIR "         MENÚ GESTIÓN DE ACTIVIDADES"
        ESCRIBIR "==================================================="
        ESCRIBIR "C. Crear actividad"
        ESCRIBIR "M. Consultar actividades"
        ESCRIBIR "X. Modificar actividad"
        ESCRIBIR "E. Eliminar actividad"
        ESCRIBIR "S. Salir del módulo"
        ESCRIBIR "==================================================="
        
        ESCRIBIR "Seleccione una opción:"
        LEER opcion
        opcion <- MAYUSCULA(QUITAR_ESPACIOS(opcion))
        
        SEGUN opcion HACER
            CASO "C":
                Crear_Actividad()
            CASO "M":
                Consultar_Actividades()
            CASO "X":
                Modificar_Actividad()
            CASO "E":
                Eliminar_Actividad()
            CASO "S":
                Mostrar_Mensaje("Saliendo del módulo de actividades...")
            DE_LO_CONTRARIO:
                Mostrar_Error("Opción no válida. Intente nuevamente.")
                Pausar()
        FIN_SEGUN
    HASTA_QUE opcion = "S"
FIN Funcion


Funcion Crear_Actividad()
INICIO
    Limpiar_Pantalla()
    ESCRIBIR "==================================================="
    ESCRIBIR "         CREAR NUEVA ACTIVIDAD"
    ESCRIBIR "==================================================="
    
    id_evento <- Solicitar_ID_Evento()
    
    SI NO Existe_Evento(id_evento) ENTONCES
        Mostrar_Error("Evento no encontrado")
        Pausar()
        RETORNAR
    FIN SI
    
    info_evento <- Obtener_Info_Evento(id_evento)
    ESCRIBIR "Evento: ", info_evento.nombre
    ESCRIBIR "Fecha: ", Formatear_Fecha(info_evento.fecha)
    ESCRIBIR "Horario del evento: ", info_evento.hora_inicio, " - ", info_evento.hora_fin
    
    ESCRIBIR "Nombre de la actividad:"
    LEER nombre
    nombre <- QUITAR_ESPACIOS(nombre)
    
    ESCRIBIR "Descripción:"
    LEER descripcion
    descripcion <- QUITAR_ESPACIOS(descripcion)
    
    // Solicitar horas con validación
    hora_inicio <- Solicitar_Hora("Hora de inicio")
    hora_fin <- Solicitar_Hora("Hora de fin")
    
    // Validar rango horario
    SI NO Validar_Rango_Horario(hora_inicio, hora_fin) ENTONCES
        Mostrar_Error("La hora de fin debe ser posterior a la de inicio")
        Pausar()
        RETORNAR
    FIN SI
    
    // Validar que estén dentro del horario del evento
    SI NO Validar_Hora_En_Rango(hora_inicio, info_evento.hora_inicio, info_evento.hora_fin) ENTONCES
        Mostrar_Error("La hora de inicio debe estar entre " + info_evento.hora_inicio + " y " + info_evento.hora_fin)
        Pausar()
        RETORNAR
    FIN SI
    
    SI NO Validar_Hora_En_Rango(hora_fin, info_evento.hora_inicio, info_evento.hora_fin) ENTONCES
        Mostrar_Error("La hora de fin debe estar entre " + info_evento.hora_inicio + " y " + info_evento.hora_fin)
        Pausar()
        RETORNAR
    FIN SI
    
    ESCRIBIR "Ubicación específica:"
    LEER ubicacion_especifica
    ubicacion_especifica <- QUITAR_ESPACIOS(ubicacion_especifica)
    
    // Solicitar capacidad con validación
    capacidad <- Solicitar_Cantidad_Positiva("Capacidad")
    
    // Validar campos obligatorios
    SI descripcion = "" O hora_inicio = "" O hora_fin = "" O ubicacion_especifica = "" ENTONCES
        Mostrar_Error("Todos los campos son obligatorios")
        Pausar()
        RETORNAR
    FIN SI
    
    actividad <- CREAR_REGISTRO_ACTIVIDAD(id_evento, nombre, descripcion, hora_inicio, hora_fin, ubicacion_especifica, capacidad)
    
    id_actividad <- GUARDAR_ACTIVIDAD(actividad)
    Mostrar_Exito("Actividad creada exitosamente con ID: " + id_actividad)
    Pausar()
FIN Funcion


Funcion Consultar_Actividades()
INICIO
    Limpiar_Pantalla()
    ESCRIBIR "==================================================="
    ESCRIBIR "         CONSULTA DE ACTIVIDADES"
    ESCRIBIR "==================================================="
    ESCRIBIR "E. Ver por evento"
    ESCRIBIR "T. Ver todas las actividades"
    ESCRIBIR "S. Volver"
    ESCRIBIR "==================================================="
    
    ESCRIBIR "Seleccione una opción:"
    LEER opcion
    opcion <- MAYUSCULA(QUITAR_ESPACIOS(opcion))
    
    SEGUN opcion HACER
        CASO "E":
            Consultar_Por_Evento()
        CASO "T":
            Consultar_Todas()
        CASO "S":
            RETORNAR
        DE_LO_CONTRARIO:
            Mostrar_Error("Opción no válida")
    FIN_SEGUN
    
    Pausar()
FIN Funcion


Funcion Consultar_Por_Evento()
INICIO
    id_evento <- Solicitar_ID_Evento()
    
    SI NO Existe_Evento(id_evento) ENTONCES
        Mostrar_Error("Evento no encontrado")
        RETORNAR
    FIN SI
    
    info_evento <- Obtener_Info_Evento(id_evento)
    ESCRIBIR "--- ACTIVIDADES DEL EVENTO: ", info_evento.nombre, " ---"
    
    actividades <- OBTENER_ACTIVIDADES_EVENTO(id_evento)
    
    SI LONGITUD(actividades) = 0 ENTONCES
        Mostrar_Mensaje("No hay actividades registradas para este evento")
        RETORNAR
    FIN SI
    
    PARA CADA actividad EN actividades HACER
        Mostrar_Actividad_Detallada(actividad)
    FIN_PARA
FIN Funcion


Funcion Consultar_Todas()
INICIO
    actividades <- OBTENER_TODAS_ACTIVIDADES_CON_EVENTO()
    
    SI LONGITUD(actividades) = 0 ENTONCES
        Mostrar_Mensaje("No hay actividades registradas")
        RETORNAR
    FIN SI
    
    ESCRIBIR "--- TODAS LAS ACTIVIDADES ---"
    PARA CADA actividad EN actividades HACER
        ESCRIBIR "--- Actividad ID: ", actividad.id, " ---"
        ESCRIBIR "Evento: ", actividad.evento_nombre
        ESCRIBIR "Nombre: ", actividad.nombre
        SI actividad.descripcion <> "" ENTONCES
            ESCRIBIR "Descripción: ", actividad.descripcion
        FIN SI
        SI actividad.hora_inicio <> "" ENTONCES
            ESCRIBIR "Horario: ", actividad.hora_inicio, " - ", actividad.hora_fin
        FIN SI
        SI actividad.ubicacion_especifica <> "" ENTONCES
            ESCRIBIR "Ubicación: ", actividad.ubicacion_especifica
        FIN SI
        SI actividad.capacidad <> 0 ENTONCES
            ESCRIBIR "Capacidad: ", actividad.capacidad
        FIN SI
        ESCRIBIR "----------------------------------------------------"
    FIN_PARA
FIN Funcion


Funcion Mostrar_Actividad_Detallada(actividad : registro)
INICIO
    ESCRIBIR "--- Actividad ID: ", actividad.id, " ---"
    ESCRIBIR "Nombre: ", actividad.nombre
    SI actividad.descripcion <> "" ENTONCES
        ESCRIBIR "Descripción: ", actividad.descripcion
    FIN SI
    SI actividad.hora_inicio <> "" ENTONCES
        ESCRIBIR "Horario: ", actividad.hora_inicio, " - ", actividad.hora_fin
    FIN SI
    SI actividad.ubicacion_especifica <> "" ENTONCES
        ESCRIBIR "Ubicación: ", actividad.ubicacion_especifica
    FIN SI
    SI actividad.capacidad <> 0 ENTONCES
        ESCRIBIR "Capacidad: ", actividad.capacidad
    FIN SI
    ESCRIBIR "----------------------------------------------------"
FIN Funcion


Funcion Modificar_Actividad()
INICIO
    Limpiar_Pantalla()
    ESCRIBIR "==================================================="
    ESCRIBIR "         MODIFICAR ACTIVIDAD"
    ESCRIBIR "==================================================="
    
    ESCRIBIR "Ingrese el ID de la actividad:"
    LEER id_actividad
    id_actividad <- CONVERTIR_A_ENTERO(id_actividad)
    
    SI NO Existe_Actividad(id_actividad) ENTONCES
        Mostrar_Error("Actividad no encontrada")
        Pausar()
        RETORNAR
    FIN SI
    
    actividad <- OBTENER_INFO_ACTIVIDAD(id_actividad)
    ESCRIBIR "Información actual de la actividad:"
    Mostrar_Actividad_Detallada(actividad)
    
    ESCRIBIR "¿Qué desea modificar?"
    ESCRIBIR "N. Nombre"
    ESCRIBIR "D. Descripción"
    ESCRIBIR "H. Horario"
    ESCRIBIR "U. Ubicación"
    ESCRIBIR "C. Capacidad"
    
    ESCRIBIR "Seleccione una opción:"
    LEER opcion
    opcion <- MAYUSCULA(QUITAR_ESPACIOS(opcion))
    
    SEGUN opcion HACER
        CASO "N":
            ESCRIBIR "Ingrese el nuevo nombre:"
            LEER nuevo_nombre
            nuevo_nombre <- QUITAR_ESPACIOS(nuevo_nombre)
            SI nuevo_nombre <> "" ENTONCES
                ACTUALIZAR_CAMPO_ACTIVIDAD(id_actividad, "nombre", nuevo_nombre)
                Mostrar_Exito("Actividad modificada exitosamente")
            SINO
                Mostrar_Error("El nombre no puede estar vacío")
            FIN SI
        
        CASO "D":
            ESCRIBIR "Ingrese la nueva descripción:"
            LEER nueva_descripcion
            nueva_descripcion <- QUITAR_ESPACIOS(nueva_descripcion)
            ACTUALIZAR_CAMPO_ACTIVIDAD(id_actividad, "descripcion", nueva_descripcion)
            Mostrar_Exito("Actividad modificada exitosamente")
        
        CASO "H":
            // Obtener info del evento para validar horarios
            id_evento <- actividad.id_evento
            info_evento <- Obtener_Info_Evento(id_evento)
            
            ESCRIBIR "Horario del evento: ", info_evento.hora_inicio, " - ", info_evento.hora_fin
            
            // Solicitar nuevas horas con validación
            nueva_hora_inicio <- Solicitar_Hora("Ingrese la nueva hora de inicio")
            nueva_hora_fin <- Solicitar_Hora("Ingrese la nueva hora de fin")
            
            // Validar rango horario
            SI NO Validar_Rango_Horario(nueva_hora_inicio, nueva_hora_fin) ENTONCES
                Mostrar_Error("La hora de fin debe ser posterior a la de inicio")
            SINO SI NO Validar_Hora_En_Rango(nueva_hora_inicio, info_evento.hora_inicio, info_evento.hora_fin) ENTONCES
                Mostrar_Error("La hora de inicio debe estar entre " + info_evento.hora_inicio + " y " + info_evento.hora_fin)
            SINO SI NO Validar_Hora_En_Rango(nueva_hora_fin, info_evento.hora_inicio, info_evento.hora_fin) ENTONCES
                Mostrar_Error("La hora de fin debe estar entre " + info_evento.hora_inicio + " y " + info_evento.hora_fin)
            SINO
                ACTUALIZAR_HORARIO_ACTIVIDAD(id_actividad, nueva_hora_inicio, nueva_hora_fin)
                Mostrar_Exito("Actividad modificada exitosamente")
            FIN SI
        
        CASO "U":
            ESCRIBIR "Ingrese la nueva ubicación:"
            LEER nueva_ubicacion
            nueva_ubicacion <- QUITAR_ESPACIOS(nueva_ubicacion)
            ACTUALIZAR_CAMPO_ACTIVIDAD(id_actividad, "ubicacion_especifica", nueva_ubicacion)
            Mostrar_Exito("Actividad modificada exitosamente")
        
        CASO "C":
            nueva_capacidad <- Solicitar_Cantidad_Positiva("Ingrese la nueva capacidad")
            ACTUALIZAR_CAMPO_ACTIVIDAD(id_actividad, "capacidad", nueva_capacidad)
            Mostrar_Exito("Actividad modificada exitosamente")
        
        DE_LO_CONTRARIO:
            Mostrar_Error("Opción de modificación no válida")
    FIN_SEGUN
    
    Pausar()
FIN Funcion


Funcion Eliminar_Actividad()
INICIO
    Limpiar_Pantalla()
    ESCRIBIR "==================================================="
    ESCRIBIR "         ELIMINAR ACTIVIDAD"
    ESCRIBIR "==================================================="
    
    ESCRIBIR "Ingrese el ID de la actividad:"
    LEER id_actividad
    id_actividad <- CONVERTIR_A_ENTERO(id_actividad)
    
    SI NO Existe_Actividad(id_actividad) ENTONCES
        Mostrar_Error("Actividad no encontrada")
        Pausar()
        RETORNAR
    FIN SI
    
    actividad <- OBTENER_INFO_ACTIVIDAD(id_actividad)
    ESCRIBIR "Actividad a eliminar: ", actividad.nombre
    
    SI Usuario_Confirma_Operacion("¿Está seguro que desea eliminar esta actividad?") ENTONCES
        ELIMINAR_ACTIVIDAD_BD(id_actividad)
        Mostrar_Exito("Actividad eliminada exitosamente")
    SINO
        Mostrar_Mensaje("Operación cancelada")
    FIN SI
    
    Pausar()
FIN Funcion

```

---
## Notas

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