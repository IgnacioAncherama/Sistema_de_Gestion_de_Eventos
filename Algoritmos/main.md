# Algoritmo del main

## Algoritmo
1. Iniciar el bucle principal de la aplicación.
2. Mostrar el menú principal con las opciones de módulos.
3. Leer la opción seleccionada por el usuario.
4. Ejecutar el módulo correspondiente.
5. Repetir hasta que el usuario elija salir.

## Nivel de Refinamiento 1

1. Mientras la opción del usuario no sea 'S' (Salir):
2. Mostrar el Menú Principal con los 5 módulos definidos.
3. Leer y validar la opción seleccionada.
4. Si la opción es válida, ejecutar el subproceso del módulo:
    * 4.1. Caso 'E': Ejecutar el módulo de Gestión de Eventos.
    * 4.2. Caso 'I': Ejecutar el módulo de Registro e Inscripciones.
    * 4.3. Caso 'P': Ejecutar el módulo de Administración de Pagos.
    * 4.4. Caso 'R': Ejecutar el módulo de Realización del Evento.
    * 4.5. Caso 'F': Ejecutar el módulo de Generación de Informes.
5. Si la opción no es válida, mostrar un mensaje de error.
6. Fin del bucle.

## Nivel de Refinamiento 2

1.  Hacer lo siguiente mientras la opción del usuario no sea "S" (Salir):
2.  Mostrar en pantalla: '--- SISTEMA DE GESTIÓN DE EVENTOS ---'
3.  Mostrar en pantalla: 'Módulo Gestión de Eventos > E'
4.  Mostrar en pantalla: 'Módulo Registro e Inscripciones > I'
5.  Mostrar en pantalla: 'Módulo Administración de Pagos > P'
6.  Mostrar en pantalla: 'Módulo Realización del Evento > R'
7.  Mostrar en pantalla: 'Módulo Generación de Informes > F'
8.  Mostrar en pantalla: 'Para salir del sistema ingresar > S'
9.  Leer y guardar en Input la entrada del usuario (convertir a mayúscula).
10. Según el valor de Input:
    * Caso "E": Ejecutar el subproceso "Gestionar_Eventos"
    * Caso "I": Ejecutar el subproceso "Gestionar_Inscripciones"
    * Caso "P": Ejecutar el subproceso "Administrar_Pagos"
    * Caso "R": Ejecutar el subproceso "Controlar_Realizacion"
    * Caso "F": Ejecutar el subproceso "Generar_Informes_y_Estadisticas"
    * Caso "S": Mostrar mensaje: 'Saliendo del Sistema...'
    * De lo contrario: Mostrar mensaje: 'Opción no válida. Intente nuevamente.'
11. Fin del bucle.

## Pseudocodigo


```python
Programa Principal_SGE
INICIO
    opcion_usuario = ""
    MIENTRAS opcion_usuario <> "S" HACER
        ESCRIBIR '--- SISTEMA DE GESTIÓN DE EVENTOS ---'
        ESCRIBIR 'Módulo Gestión de Eventos > E'
        ESCRIBIR 'Módulo Registro e Inscripciones > I'
        ESCRIBIR 'Módulo Administración de Pagos > P'
        ESCRIBIR 'Módulo Realización del Evento > R'
        ESCRIBIR 'Módulo Generación de Informes > F'
        ESCRIBIR 'Para salir del sistema ingresar > S'
        
        LEER opcion_usuario
        opcion_usuario <- MAYUSCULA(opcion_usuario)
        SEGUN opcion_usuario HACER
            CASO "E": Gestionar_Eventos()
            CASO "I": Gestionar_Inscripciones()
            CASO "P": Administrar_Pagos()
            CASO "R": Controlar_Realizacion()
            CASO "F": Generar_Informes_y_Estadisticas()
            CASO "S": Mostrar_Mensaje("Saliendo del Sistema...")
            DE LO CONTRARIO: Mostrar_Error("Opción no válida. Intente nuevamente.")
        FIN SEGUN
        
    FIN MIENTRAS
FIN Programa


Funcion Gestionar_Eventos()
INICIO
  Mostrar_Mensaje("Accediendo a Gestión de Eventos..")
  Menu_Principal_Eventos()
FIN Funcion

Funcion Gestionar_Inscripciones()
INICIO
    Mostrar_Mensaje("Accediendo a Registro e Inscripciones..")
    Menu_Principal_Inscripciones()
FIN Funcion

Funcion Administrar_Pagos()
INICIO
    Mostrar_Mensaje("Accediendo a Administración de Pagos...")
    Menu_Principal_Pagos()
FIN Funcion

Funcion Controlar_Realizacion()
INICIO
    Mostrar_Mensaje("Accediendo a Realización del Evento..")
    Menu_Principal_Realizacion()
FIN Funcion

Funcion Generar_Informes_y_Estadisticas()
INICIO
    Mostrar_Mensaje("Accediendo a Generación de Informes..") 
    Menu_Principal_Informes() 
FIN Funcion

