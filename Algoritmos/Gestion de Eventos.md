# Algoritmo de Sistemas de Gestion de Eventos

## Algoritmo

1. Mostrar menú principal de la gestion de eventos.
2. Solicitar al cliente que elija una opción.
3. Mostrar la interfaz correspondiente a la elección del cliente.
4. Leer la entrada o entradas del usuario.
5. Mostrar salida correspondiente a las entradas.

## Nivel de Refinamiento 1
````
1. Menu principal gestion de eventos.
  2. Crear un nuevo evento.
  3. Consultar eventos.
  4. Modificar un evento existente.
  5. Eliminar un evento.
````
----
## Nivel de Refinamiento 2

### Menu Principal 
````
  1.1. Hacer lo siguiente mientras la opción del usuario no sea "S" (Salir):
    1.2. Mostrar en pantalla: '--- MENÚ GESTIÓN DE EVENTOS ---'
    1.3. Mostrar en pantalla: 'Para crear un evento ingresar > C'
    1.4. Mostrar en pantalla: 'Para consultar eventos ingresar > M'
    1.5. Mostrar en pantalla: 'Para modificar un evento ingresar > X'
    1.6. Mostrar en pantalla: 'Para eliminar un evento ingresar > E'
    1.7. Mostrar en pantalla: 'Para salir del módulo ingresar > S'
    1.8. Leer y guardar en 'Input' la entrada del usuario (convertir a mayúscula).
    1.9. Según el valor de Input:
      1.9.1 Caso "C":
        1.9.1.1 Ejecutar el subproceso "Crear un Nuevo Evento".
      1.9.2 Caso "M":
        1.9.2.1 Ejecutar el subproceso "Consultar Eventos".
      1.9.3 Caso "X":
        1.9.3.1 Ejecutar el subproceso "Modificar un Evento Existente".
      1.9.4 Caso "E":
        1.9.4.1 Ejecutar el subproceso "Eliminar un Evento".
      1.9.5 Caso "S":
        1.9.5.1 Mostrar un mensaje de despedida: 'Saliendo del módulo de gestión de eventos...'
      1.9.6 De lo contrario:
        1.9.6.1 Mostrar mensaje de error: 'Opción no válida. Por favor, intente nuevamente.'
        1.9.6.2 Volver al paso (1.2)
  1.2. Fin del bucle.
````
### Crear un nuevo evento 
````
2.1. Mostrar en pantalla: 'Ingrese nombre del evento:'
2.2. Leer y guardar en 'nombre_evento'
2.3. Mostrar en pantalla: 'Ingrese descripción del evento:'
2.4. Leer y guardar en 'descripcion_evento'
2.5. Mostrar en pantalla: 'Ingrese fecha del evento (DD/MM/AAAA):'
2.6. Leer y guardar en 'fecha_evento'
2.7. Validar que fecha_evento > fecha_actual
2.8. Si fecha no es válida:
    2.8.1. Mostrar mensaje: 'Error: La fecha debe ser posterior a hoy'
    2.8.2. Volver al paso 2.5
2.9. Mostrar en pantalla: 'Ingrese hora de inicio (HH:MM):'
2.10. Leer y guardar en 'hora_inicio'
2.11. Mostrar en pantalla: 'Ingrese hora de fin (HH:MM):'
2.12. Leer y guardar en 'hora_fin'
2.13. Validar que hora_fin > hora_inicio
2.14. Si horarios no son válidos:
    2.14.1. Mostrar mensaje: 'Error: La hora de fin debe ser posterior a la de inicio'
    2.14.2. Volver al paso 2.9
2.15. Mostrar en pantalla: 'Ingrese ubicación del evento:'
2.16. Leer y guardar en 'ubicacion'
2.17. Mostrar en pantalla: 'Ingrese capacidad máxima:'
2.18. Leer y guardar en 'capacidad_maxima'
2.19. Validar que capacidad_maxima > 0
2.20. Si capacidad no es válida:
    2.20.1. Mostrar mensaje: 'Error: La capacidad debe ser mayor a 0'
    2.20.2. Volver al paso 2.17
2.21. Mostrar en pantalla: 'Ingrese precio del evento:'
2.22. Leer y guardar en 'precio'
2.23. Validar que precio >= 0
2.24. Si precio no es válido:
    2.24.1. Mostrar mensaje: 'Error: El precio no puede ser negativo'
    2.24.2. Volver al paso 2.21
2.25. Generar nuevo ID único para el evento
2.26. Establecer estado = 'activo'
2.27. Guardar evento en la base de datos
2.28. Mostrar mensaje: 'Evento creado exitosamente con ID: [ID_generado]'
````
### Consultar eventos 
````
3.1. Mostrar en pantalla: '--- CONSULTA DE EVENTOS ---'
3.2. Mostrar en pantalla: 'Para ver todos los eventos ingresar > T'
3.3. Mostrar en pantalla: 'Para buscar por ID ingresar > I'
3.4. Mostrar en pantalla: 'Para buscar por nombre ingresar > N'
3.5. Mostrar en pantalla: 'Para buscar por fecha ingresar > F'
3.6. Mostrar en pantalla: 'Para salir de este submodulo ingresar > S'
3.7. Leer y guardar en 'opcion_consulta'
3.8. Según el valor de opcion_consulta:
    3.8.1. Caso "T":
        3.8.1.1. Obtener todos los eventos de la base de datos
        3.8.1.2. Si no hay eventos:
            3.8.1.2.1. Mostrar mensaje: 'No hay eventos registrados'
        3.8.1.3. Si hay eventos:
            3.8.1.3.1. Para cada evento en la lista:
                3.8.1.3.1.1. Mostrar información completa del evento
    3.8.2. Caso "I":
        3.8.2.1. Mostrar en pantalla: 'Ingrese ID del evento:'
        3.8.2.2. Leer y guardar en 'id_busqueda'
        3.8.2.3. Buscar evento por ID en la base de datos
        3.8.2.4. Si evento encontrado:
            3.8.2.4.1. Mostrar información completa del evento
        3.8.2.5. Si no encontrado:
            3.8.2.5.1. Mostrar mensaje: 'Evento no encontrado'
    3.8.3. Caso "N":
        3.8.3.1. Mostrar en pantalla: 'Ingrese nombre del evento:'
        3.8.3.2. Leer y guardar en 'nombre_busqueda'
        3.8.3.3. Buscar eventos que contengan el nombre en la base de datos
        3.8.3.4. Si evento encontrado:
            3.8.3.4.1. Mostrar información completa del evento
        3.8.3.5. Si no encontrado:
            3.8.3.5.1. Mostrar mensaje: 'Evento no encontrado'
    3.8.4. Caso "F":
        3.8.4.1. Mostrar en pantalla: 'Ingrese fecha (DD/MM/AAAA):'
        3.8.4.2. Leer y guardar en 'fecha_busqueda'
        3.8.4.3. Buscar eventos por fecha en la base de datos
        3.8.4.4. Si evento encontrado:
            3.8.4.4.1. Mostrar información completa del evento
        3.8.4.5. Si no encontrado:
            3.8.4.5.1. Mostrar mensaje: 'Evento no encontrado'
    3.8.5. Caso "S":
        3.8.5.1. Mostrar mensaje: 'Volviendo al menu inicial de Gestion de eventos'
        3.8.5.2. Retornar al Menu Principal de Gestion de Eventos
    3.8.6. De lo contrario:
        3.8.6.1. Mostrar mensaje: 'Opción no válida'
````
### Modificar un evento existente 
````
4.1.  Mostrar en pantalla: '--- MODIFICAR EVENTO EXISTENTE ---'
4.2.  Verificar si existen eventos registrados. Si no hay, mostrar 'No hay eventos para modificar.' y volver al menú.
4.3.  Solicitar y leer el ID del evento a modificar. Guardar en 'id_buscado'.
4.4.  Buscar el evento con el 'id_buscado'.
4.5.  Si no se encuentra el evento, hacer:
      4.5.1. Mostrar mensaje de error: 'Evento no encontrado.'
      4.5.2. Finalizar subproceso y volver al menú principal.
4.6.  Si se encuentra el evento, hacer:
      4.6.1. Mostrar los datos actuales del evento encontrado.
      4.6.2. Solicitar al usuario el nuevo nombre del evento. Si no ingresa nada, mantener el original. Guardar en 'nuevo_nombre'.
      4.6.3. Solicitar la nueva fecha. Si no ingresa nada, mantener la original. Guardar en 'nueva_fecha'.
      4.6.4. Solicitar el nuevo lugar. Si no ingresa nada, mantener el original. Guardar en 'nuevo_lugar'.
      4.6.5. Validar los nuevos datos ingresados.
      4.6.6. Si los datos no son válidos, mostrar error y cancelar la modificación.
      4.6.7. Si los datos son válidos, preguntar: '¿Confirma los cambios? (S/N)'.
      4.6.8. Leer y guardar la confirmación.
      4.6.9. Si la confirmación es "S" (o "s"), hacer:
             4.6.9.1. Segun el 'id_buscado', actualizar los datos del evento en la base de datos.
             4.6.9.2. Mostrar mensaje de éxito: 'El evento ha sido modificado correctamente.'
      4.6.10. Si la confirmación no es "S", hacer:
             4.6.10.1. Mostrar mensaje: 'Modificación cancelada.'
4.7.  Finalizar subproceso y volver al menú principal.
````
### Eliminar un evento 
````
5.1. Mostrar en pantalla: 'Ingrese ID del evento a eliminar:'
5.2. Leer y guardar en 'id_evento'
5.3. Buscar evento por ID en la base de datos
5.4. Si evento no encontrado:
    5.4.1. Mostrar mensaje: 'Evento no encontrado'
    5.4.2. Terminar subproceso
5.5. Si evento encontrado:
    5.5.1. Mostrar información del evento
    5.5.2. Verificar si hay inscripciones asociadas
    5.5.3. Si hay inscripciones:
        5.5.3.1. Mostrar mensaje: 'No se puede eliminar. Hay inscripciones asociadas'
        5.5.3.2. Terminar subproceso
    5.5.4. Si no hay inscripciones:
        5.5.4.1. Mostrar en pantalla: '¿Está seguro? (S/N):'
        5.5.4.2. Leer confirmación
        5.5.4.3. Si confirmación = "S":
            5.5.4.3.1. Eliminar evento de la base de datos
            5.5.4.3.2. Mostrar mensaje: 'Evento eliminado exitosamente'
        5.5.4.4. Si confirmación = "N":
            5.5.4.4.1. Mostrar mensaje: 'Operación cancelada'
````
----
## Pseudocodigo

**NOTA**: Este módulo utiliza funciones del archivo `Funciones_Comunes.md`

````
VARIABLES:
    // Variables generales del menú
    Input: cadena
    id_buscado, id_evento: entero
    confirmacion: cadena
    
    // Variables para Crear y Modificar Evento
    nombre_evento, descripcion_evento, ubicacion: cadena
    fecha_evento: fecha
    hora_inicio, hora_fin: hora
    capacidad_maxima: entero
    precio: real
    estado: cadena
    evento_encontrado: registro // Estructura para almacenar los datos de un evento
    
    // Variables para Submenús
    opcion_consulta, opcion_modificar: cadena
    nuevo_valor_cadena: cadena
    nuevo_valor_entero: entero
    nuevo_valor_fecha: fecha

INICIO
    REPETIR
        ESCRIBIR '--- MENÚ GESTIÓN DE EVENTOS ---'
        ESCRIBIR 'Para crear un evento ingresar > C'
        ESCRIBIR 'Para consultar eventos ingresar > M'
        ESCRIBIR 'Para modificar un evento ingresar > X'
        ESCRIBIR 'Para eliminar un evento ingresar > E'
        ESCRIBIR 'Para salir del módulo ingresar > S'
        LEER Input
        Input <- MAYUSCULA(Input)
        
        SEGUN Input HACER
            CASO "C":
                // Crear nuevo evento
                ESCRIBIR 'Ingrese nombre del evento:'
                LEER nombre_evento
                ESCRIBIR 'Ingrese descripción del evento:'
                LEER descripcion_evento
                
                // Solicitar fecha con validación
                fecha_evento <- Solicitar_Fecha("Ingrese fecha del evento", FECHA_ACTUAL)
                
                // Solicitar horas con validación
                hora_inicio <- Solicitar_Hora("Ingrese hora de inicio")
                hora_fin <- Solicitar_Hora("Ingrese hora de fin")
                
                // Validar rango horario
                SI NO Validar_Rango_Horario(hora_inicio, hora_fin) ENTONCES
                    Mostrar_Error("La hora de fin debe ser posterior a la de inicio")
                    CONTINUAR
                FIN_SI
                
                ESCRIBIR 'Ingrese ubicación del evento:'
                LEER ubicacion
                
                // Solicitar capacidad con validación
                capacidad_maxima <- Solicitar_Cantidad_Positiva("Ingrese capacidad máxima")
                
                // Solicitar precio con validación
                precio <- Solicitar_Precio()
                id_evento <- GENERAR_ID_UNICO()
                estado <- 'activo'
                GUARDAR_EVENTO(id_evento, nombre_evento, descripcion_evento, fecha_evento, 
                               hora_inicio, hora_fin, ubicacion, capacidad_maxima, precio, estado)
                ESCRIBIR 'Evento creado exitosamente con ID: ', id_evento
                
            CASO "M":
                // Consultar eventos
                // Utiliza: Solicitar_ID_Evento, Mostrar_Error
                ESCRIBIR '--- CONSULTA DE EVENTOS ---'
                ESCRIBIR 'Para ver todos los eventos ingresar > T'
                ESCRIBIR 'Para buscar por ID ingresar > I'
                ESCRIBIR 'Para buscar por nombre ingresar > N'
                ESCRIBIR 'Para buscar por fecha ingresar > F'
                LEER opcion_consulta
                SEGUN opcion_consulta HACER
                    CASO "T":
                        MOSTRAR_TODOS_LOS_EVENTOS()
                    CASO "I":
                        id_evento <- Solicitar_ID_Evento()
                        BUSCAR_EVENTO_POR_ID(id_evento)
                    CASO "N":
                        ESCRIBIR 'Ingrese nombre del evento:'
                        LEER nombre_evento
                        BUSCAR_EVENTOS_POR_NOMBRE(nombre_evento)
                    CASO "F":
                        ESCRIBIR 'Ingrese fecha (DD/MM/AAAA):'
                        LEER fecha_evento
                        BUSCAR_EVENTOS_POR_FECHA(fecha_evento)
                    DE_LO_CONTRARIO:
                        Mostrar_Error('Opción no válida')
                FIN_SEGUN
                
            CASO "X":
                // Modificar evento
                // Utiliza: Solicitar_ID_Evento, Existe_Evento, Obtener_Info_Evento, Mostrar_Error
                ESCRIBIR '--- MODIFICAR EVENTO ---'
                id_buscado <- Solicitar_ID_Evento()
                
                SI NOT Existe_Evento(id_buscado) ENTONCES
                    Mostrar_Error('Evento no encontrado.')
                    CONTINUAR
                FIN SI
                
                evento_encontrado <- Obtener_Info_Evento(id_buscado)
                SI VERDADERO ENTONCES
                    ESCRIBIR 'Información actual del evento:'
                    // Mostrar aquí los datos de evento_encontrado
                    ESCRIBIR 'ID: ', evento_encontrado.id
                    ESCRIBIR 'Nombre: ', evento_encontrado.nombre
                    ESCRIBIR 'Fecha: ', evento_encontrado.fecha
                    ESCRIBIR 'Ubicación: ', evento_encontrado.ubicacion
                    
                    ESCRIBIR '¿Qué desea modificar?'
                    ESCRIBIR '(N) Nombre'
                    ESCRIBIR '(F) Fecha'
                    ESCRIBIR '(U) Ubicación'
                    ESCRIBIR '(C) Capacidad'
                    LEER opcion_modificar
                    opcion_modificar <- MAYUSCULA(opcion_modificar)
                    
                    SEGUN opcion_modificar HACER
                        CASO "N":
                            ESCRIBIR 'Ingrese el nuevo nombre:'
                            LEER nuevo_valor_cadena
                            SI nuevo_valor_cadena <> "" ENTONCES
                                ACTUALIZAR_CAMPO_EVENTO(id_buscado, "nombre", nuevo_valor_cadena)
                                Mostrar_Exito('Evento modificado exitosamente.')
                            SINO
                                Mostrar_Error('El nombre no puede estar vacío.')
                            FIN_SI
                        CASO "F":
                            nueva_fecha <- Solicitar_Fecha("Ingrese la nueva fecha", FECHA_ACTUAL)
                            ACTUALIZAR_CAMPO_EVENTO(id_buscado, "fecha", nueva_fecha)
                            Mostrar_Exito('Evento modificado exitosamente.')
                        CASO "U":
                             ESCRIBIR 'Ingrese la nueva ubicación:'
                             LEER nuevo_valor_cadena
                             ACTUALIZAR_CAMPO_EVENTO(id_buscado, "ubicacion", nuevo_valor_cadena)
                             Mostrar_Exito('Evento modificado exitosamente.')
                        CASO "C":
                            nueva_capacidad <- Solicitar_Cantidad_Positiva("Ingrese la nueva capacidad")
                            ACTUALIZAR_CAMPO_EVENTO(id_buscado, "capacidad", nueva_capacidad)
                            Mostrar_Exito('Evento modificado exitosamente.')
                        DE_LO_CONTRARIO:
                            Mostrar_Error('Opción de modificación no válida.')
                    FIN_SEGUN
                FIN_SI

            CASO "E":
                // Eliminar evento
                // Utiliza: Solicitar_ID_Evento, Existe_Evento, Usuario_Confirma_Operacion
                //          Mostrar_Error, Mostrar_Exito, Mostrar_Mensaje
                id_evento <- Solicitar_ID_Evento()
                SI Existe_Evento(id_evento) ENTONCES
                    SI TIENE_INSCRIPCIONES(id_evento) ENTONCES
                        Mostrar_Error('No se puede eliminar. Hay inscripciones asociadas.')
                    SINO
                        SI Usuario_Confirma_Operacion('¿Está seguro que desea eliminar este evento?') ENTONCES
                            ELIMINAR_EVENTO(id_evento)
                            Mostrar_Exito('Evento eliminado exitosamente.')
                        SINO
                            Mostrar_Mensaje('Operación cancelada.')
                        FIN_SI
                    FIN_SI
                SINO
                    Mostrar_Error('Evento no encontrado.')
                FIN_SI
                
            CASO "S":
                ESCRIBIR 'Saliendo del módulo de gestión de eventos...'
                
            DE_LO_CONTRARIO:
                ESCRIBIR 'Opción no válida. Por favor, intente nuevamente.'
        FIN_SEGUN
        
    HASTA_QUE Input = "S"
FIN
````


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
