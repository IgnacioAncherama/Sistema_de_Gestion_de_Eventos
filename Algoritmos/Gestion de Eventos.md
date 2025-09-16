# Algoritmo de Sistemas de Gestion de Eventos

## Nivel de Refinamiento 1

1. Menu principal gestion de eventos.
2. Crear un nuevo evento.
3. Consultar eventos.
4. Modificar un evento existente.
5. Eliminar un evento.

----
## Nivel de Refinamiento 2
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
````
2.1.  Mostrar en pantalla: '--- CREACIÓN DE NUEVO EVENTO ---'
2.2.  Solicitar y leer el nombre del evento. Guardar en 'nombre_evento'.
2.3.  Solicitar y leer la fecha del evento (formato DD/MM/AAAA). Guardar en 'fecha_evento'.
2.4.  Solicitar y leer el lugar del evento. Guardar en 'lugar_evento'.
2.5.  Solicitar y leer la descripción del evento. Guardar en 'descripcion_evento'.
2.6.  Solicitar y leer la capacidad máxima de asistentes. Guardar en 'capacidad_evento'.
2.7.  Validar los datos ingresados:
      2.7.1. Si 'nombre_evento' está vacío O la 'fecha_evento' no tiene un formato válido O 'capacidad_evento' no es un número positivo, hacer:
             2.7.1.1. Mostrar mensaje de error: 'Datos inválidos. Por favor, revise la información ingresada.'
             2.7.1.2. Finalizar subproceso y volver al menú principal.
2.8.  Generar un ID único para el evento. Guardar en 'id_evento'.
2.9.  Guardar los datos ('id_evento', 'nombre_evento', 'fecha_evento', etc.) en la base de datos o estructura de datos del sistema.
2.10. Mostrar mensaje de éxito: 'Evento "' + nombre_evento + '" creado exitosamente con el ID: ' + id_evento.
2.11. Finalizar subproceso y volver al menú principal.
````
````
3.1.  Mostrar en pantalla: '--- CONSULTA DE EVENTOS ---'
3.2.  Verificar si existen eventos registrados en el sistema.
3.3.  Si no hay eventos, hacer:
      3.3.1. Mostrar mensaje: 'No hay eventos registrados en el sistema.'
      3.3.2. Finalizar subproceso y volver al menú principal.
3.4.  Si hay eventos, mostrar la lista completa:
      3.4.1. Para cada evento en la lista de eventos, hacer:
             3.4.1.1. Mostrar en pantalla: 'ID: ' + evento.id + ' | Nombre: ' + evento.nombre + ' | Fecha: ' + evento.fecha
3.5.  Preguntar al usuario: '¿Desea ver el detalle de un evento específico? (S/N)'.
3.6.  Leer y guardar la respuesta en 'ver_detalle'.
3.7.  Si 'ver_detalle' es "S" (o "s"), hacer:
      3.7.1. Solicitar y leer el ID del evento a detallar. Guardar en 'id_buscado'.
      3.7.2. Buscar el evento con el 'id_buscado' en la lista de eventos.
      3.7.3. Si se encuentra el evento, hacer:
             3.7.3.1. Mostrar todos sus detalles: ID, Nombre, Fecha, Lugar, Descripción, Capacidad.
      3.7.4. Si no se encuentra el evento, hacer:
             3.7.4.1. Mostrar mensaje de error: 'No se encontró ningún evento con el ID proporcionado.'
3.8.  Finalizar subproceso y volver al menú principal.
````
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
      4.6.5. Validar los nuevos datos ingresados (similar al paso 2.7).
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
````
5.1.  Mostrar en pantalla: '--- ELIMINAR EVENTO ---'
5.2.  Verificar si existen eventos registrados. Si no hay, mostrar 'No hay eventos para eliminar.' y volver al menú.
5.3.  Solicitar y leer el ID del evento a eliminar. Guardar en 'id_a_eliminar'.
5.4.  Buscar el evento con el 'id_a_eliminar'.
5.5.  Si no se encuentra el evento, hacer:
      5.5.1. Mostrar mensaje de error: 'Evento no encontrado.'
      5.5.2. Finalizar subproceso y volver al menú principal.
5.6.  Si se encuentra el evento, hacer:
      5.6.1. Mostrar en pantalla los datos del evento que se va a eliminar.
      5.6.2. Preguntar al usuario: '¿Está SEGURO de que desea eliminar este evento de forma permanente? (S/N)'.
      5.6.3. Leer y guardar la confirmación en 'confirmar_eliminar'.
      5.6.4. Si 'confirmar_eliminar' es "S" (o "s"), hacer:
             5.6.4.1. Eliminar el evento de la base de datos.
             5.6.4.2. Mostrar mensaje de éxito: 'El evento ha sido eliminado correctamente.'
      5.6.5. Si la confirmación no es "S", hacer:
             5.6.5.1. Mostrar mensaje: 'Operación cancelada. El evento no ha sido eliminado.'
5.7.  Finalizar subproceso y volver al menú principal.
````
## Algoritmo

----
## Pseudocodigo
