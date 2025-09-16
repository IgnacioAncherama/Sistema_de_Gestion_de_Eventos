# Algoritmo de Sistemas de Gestion de Eventos

## Nivel de Refinamiento 1

1. Menu principal gestion de eventos.
2. Crear un nuevo evento.
3. Consultar eventos.
4. Modificar un evento existente.
5. Eliminar un evento.

----
## Nivel de Refinamiento 2
``
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
``
## Algoritmo

----
## Pseudocodigo
