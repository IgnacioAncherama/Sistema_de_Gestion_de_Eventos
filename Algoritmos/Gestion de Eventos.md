# Algoritmo de Sistemas de Gestion de Eventos

## Algoritmo

## Nivel de Refinamiento 1

1. Menu principal gestion de eventos.
2. Crear un nuevo evento.
3. Consultar eventos.
4. Modificar un evento existente.
5. Eliminar un evento.

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
3.6. Leer y guardar en 'opcion_consulta'
3.7. Según el valor de opcion_consulta:
    3.7.1. Caso "T":
        3.7.1.1. Obtener todos los eventos de la base de datos
        3.7.1.2. Si no hay eventos:
            3.7.1.2.1. Mostrar mensaje: 'No hay eventos registrados'
        3.7.1.3. Si hay eventos:
            3.7.1.3.1. Para cada evento en la lista:
                3.7.1.3.1.1. Mostrar información completa del evento
    3.7.2. Caso "I":
        3.7.2.1. Mostrar en pantalla: 'Ingrese ID del evento:'
        3.7.2.2. Leer y guardar en 'id_busqueda'
        3.7.2.3. Buscar evento por ID en la base de datos
        3.7.2.4. Si evento encontrado:
            3.7.2.4.1. Mostrar información completa del evento
        3.7.2.5. Si no encontrado:
            3.7.2.5.1. Mostrar mensaje: 'Evento no encontrado'
    3.7.3. Caso "N":
        3.7.3.1. Mostrar en pantalla: 'Ingrese nombre del evento:'
        3.7.3.2. Leer y guardar en 'nombre_busqueda'
        3.7.3.3. Buscar eventos que contengan el nombre en la base de datos
        3.7.3.4. Mostrar resultados encontrados
    3.7.4. Caso "F":
        3.7.4.1. Mostrar en pantalla: 'Ingrese fecha (DD/MM/AAAA):'
        3.7.4.2. Leer y guardar en 'fecha_busqueda'
        3.7.4.3. Buscar eventos por fecha en la base de datos
        3.7.4.4. Mostrar resultados encontrados
    3.7.5. De lo contrario:
        3.7.5.1. Mostrar mensaje: 'Opción no válida'
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
             4.6.9.1. Actualizar los datos del evento en la base de datos.
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
