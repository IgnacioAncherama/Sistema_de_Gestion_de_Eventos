# Algoritmo de Realización del Evento

## Nivel de Refinamiento 1

1. Menú principal realización del evento.
2. Iniciar control de asistencia.
3. Registrar llegada de participantes.
4. Consultar asistencia en tiempo real.
5. Gestionar recursos del evento.
6. Finalizar evento.

----
## Nivel de Refinamiento 2

### 1. Menu Realizacion del Evento
```
1.1. Hacer lo siguiente mientras la opción del usuario no sea "S" (Salir):
    1.2. Mostrar en pantalla: '--- MENÚ REALIZACIÓN DEL EVENTO ---'
    1.3. Mostrar en pantalla: 'Para iniciar control de asistencia ingresar > I'
    1.4. Mostrar en pantalla: 'Para registrar llegada ingresar > L'
    1.5. Mostrar en pantalla: 'Para consultar asistencia ingresar > A'
    1.6. Mostrar en pantalla: 'Para gestionar recursos ingresar > R'
    1.7. Mostrar en pantalla: 'Para finalizar evento ingresar > F'
    1.8. Mostrar en pantalla: 'Para salir del módulo ingresar > S'
    1.9. Leer y guardar en 'Input' la entrada del usuario (convertir a mayúscula).
    1.10. Según el valor de Input:
        1.10.1 Caso "I":
            1.10.1.1 Ejecutar el subproceso "Iniciar Control de Asistencia".
        1.10.2 Caso "L":
            1.10.2.1 Ejecutar el subproceso "Registrar Llegada".
        1.10.3 Caso "A":
            1.10.3.1 Ejecutar el subproceso "Consultar Asistencia".
        1.10.4 Caso "R":
            1.10.4.1 Ejecutar el subproceso "Gestionar Recursos".
        1.10.5 Caso "F":
            1.10.5.1 Ejecutar el subproceso "Finalizar Evento".
        1.10.6 Caso "S":
            1.10.6.1 Mostrar mensaje: 'Saliendo del módulo de realización...'
        1.10.7 De lo contrario:
            1.10.7.1 Mostrar mensaje: 'Opción no válida. Intente nuevamente.'
1.11. Fin del bucle.
```

### 2. INICIAR CONTROL DE ASISTENCIA
```
2.1. Mostrar en pantalla: 'Ingrese ID del evento a iniciar:'
2.2. Leer y guardar en 'id_evento'
2.3. Verificar si el evento existe
2.4. Si evento no existe:
    2.4.1. Mostrar mensaje: 'Evento no encontrado'
    2.4.2. Terminar subproceso
2.5. Si evento existe:
    2.5.1. Verificar si es la fecha del evento
    2.5.2. Si no es la fecha correcta:
        2.5.2.1. Mostrar mensaje: 'El evento no es hoy'
        2.5.2.2. Mostrar fecha del evento
        2.5.2.3. Terminar subproceso
2.6. Verificar si ya está iniciado el control
2.7. Si ya está iniciado:
    2.7.1. Mostrar mensaje: 'El control de asistencia ya está activo'
    2.7.2. Terminar subproceso
2.8. Obtener lista de inscripciones confirmadas y pagadas
2.9. Inicializar registros de asistencia
2.10. Cambiar estado del evento a 'en_curso'
2.11. Mostrar mensaje: 'Control de asistencia iniciado'
2.12. Mostrar resumen: 'Participantes esperados: [cantidad]'
```

### 3. REGISTRAR LLEGADA DE PARTICIPANTES
```
3.1. Mostrar en pantalla: 'Ingrese documento del participante:'
3.2. Leer y guardar en 'documento'
3.3. Buscar participante por documento
3.4. Si participante no encontrado:
    3.4.1. Mostrar mensaje: 'Participante no registrado'
    3.4.2. Terminar subproceso
3.5. Si participante encontrado:
    3.5.1. Buscar inscripción activa del participante para eventos de hoy
    3.5.2. Si no tiene inscripción para hoy:
        3.5.2.1. Mostrar mensaje: 'Participante no inscrito en eventos de hoy'
        3.5.2.2. Terminar subproceso
    3.5.3. Verificar estado de pago de la inscripción
    3.5.4. Si pago no realizado:
        3.5.4.1. Mostrar mensaje: 'Pago pendiente. Dirigirse a caja'
        3.5.4.2. Terminar subproceso
    3.5.5. Verificar si ya registró su llegada
    3.5.6. Si ya registró llegada:
        3.5.6.1. Mostrar mensaje: 'Participante ya registró su llegada'
        3.5.6.2. Mostrar hora de llegada anterior
        3.5.6.3. Terminar subproceso
3.7. Registrar llegada con fecha y hora actual
3.8. Establecer presente = verdadero
3.9. Guardar registro de asistencia
3.10. Mostrar mensaje: 'Llegada registrada exitosamente'
3.11. Mostrar información del evento y ubicación
```

### 4. CONSULTAR ASISTENCIA EN TIEMPO REAL
```
4.1. Mostrar en pantalla: 'Ingrese ID del evento:'
4.2. Leer y guardar en 'id_evento'
4.3. Verificar si el evento existe
4.4. Si evento no existe:
    4.4.1. Mostrar mensaje: 'Evento no encontrado'
    4.4.2. Terminar subproceso
4.5. Si evento existe:
    4.5.1. Obtener estadísticas de asistencia
    4.5.2. Calcular participantes presentes
    4.5.3. Calcular participantes ausentes
    4.5.4. Calcular porcentaje de asistencia
    4.5.5. Mostrar resumen de asistencia:
        4.5.5.1. Total inscriptos
        4.5.5.2. Presentes
        4.5.5.3. Ausentes
        4.5.5.4. Porcentaje de asistencia
    4.5.6. Mostrar lista detallada de participantes presentes
    4.5.7. Mostrar lista de participantes ausentes
```

### 5. GESTIONAR RECURSOS DEL EVENTO
```
5.1. Mostrar en pantalla: 'Ingrese ID del evento:'
5.2. Leer y guardar en 'id_evento'
5.3. Verificar si el evento existe y está en curso
5.4. Si evento no válido:
    5.4.1. Mostrar mensaje: 'Evento no encontrado o no está en curso'
    5.4.2. Terminar subproceso
5.5. Mostrar opciones de gestión de recursos:
    5.5.1. Registrar uso de equipos
    5.5.2. Controlar capacidad de sala
    5.5.3. Gestionar materiales
    5.5.4. Registrar incidencias
5.6. Leer opción del usuario
5.7. Ejecutar acción según opción seleccionada
5.8. Actualizar registro de recursos utilizados
```

### 6. FINALIZAR EVENTO
```
6.1. Mostrar en pantalla: 'Ingrese ID del evento a finalizar:'
6.2. Leer y guardar en 'id_evento'
6.3. Verificar si el evento existe y está en curso
6.4. Si evento no válido:
    6.4.1. Mostrar mensaje: 'Evento no encontrado o no está en curso'
    6.4.2. Terminar subproceso
6.5. Generar resumen final del evento:
    6.5.1. Estadísticas de asistencia
    6.5.2. Recursos utilizados
    6.5.3. Incidencias registradas
6.6. Mostrar en pantalla: '¿Confirma finalización del evento? (S/N):'
6.7. Leer confirmación
6.8. Si confirmación = "S":
    6.8.1. Cambiar estado del evento a 'finalizado'
    6.8.2. Cerrar control de asistencia
    6.8.3. Generar reporte final automático
    6.8.4. Mostrar mensaje: 'Evento finalizado exitosamente'
6.9. Si confirmación = "N":
    6.9.1. Mostrar mensaje: 'Operación cancelada'
```

----
## Pseudocodigo
## Algoritmo

```
ALGORITMO RealizacionEvento

VARIABLES:
    Input: cadena
    id_evento, id_inscripcion: entero
    documento: cadena
    fecha_hora_llegada: fecha_hora
    presente: booleano
    participantes_presentes, participantes_ausentes, total_inscriptos: entero
    porcentaje_asistencia: real
    confirmacion: cadena

INICIO
    REPETIR
        ESCRIBIR '--- MENÚ REALIZACIÓN DEL EVENTO ---'
        ESCRIBIR 'Para iniciar control de asistencia ingresar > I'
        ESCRIBIR 'Para registrar llegada ingresar > L'
        ESCRIBIR 'Para consultar asistencia ingresar > A'
        ESCRIBIR 'Para gestionar recursos ingresar > R'
        ESCRIBIR 'Para finalizar evento ingresar > F'
        ESCRIBIR 'Para salir del módulo ingresar > S'
        LEER Input
        Input <- MAYUSCULA(Input)
        
        SEGUN Input HACER
            CASO "I":
                // Iniciar control de asistencia
                ESCRIBIR 'Ingrese ID del evento a iniciar:'
                LEER id_evento
                SI NO EXISTE_EVENTO(id_evento) ENTONCES
                    ESCRIBIR 'Evento no encontrado'
                    CONTINUAR
                FIN_SI
                
                SI NO ES_FECHA_EVENTO(id_evento) ENTONCES
                    ESCRIBIR 'El evento no es hoy'
                    MOSTRAR_FECHA_EVENTO(id_evento)
                    CONTINUAR
                FIN_SI
                
                SI CONTROL_YA_INICIADO(id_evento) ENTONCES
                    ESCRIBIR 'El control de asistencia ya está activo'
                    CONTINUAR
                FIN_SI
                
                INICIALIZAR_CONTROL_ASISTENCIA(id_evento)
                CAMBIAR_ESTADO_EVENTO(id_evento, 'en_curso')
                total_inscriptos <- CONTAR_INSCRIPTOS_PAGADOS(id_evento)
                ESCRIBIR 'Control de asistencia iniciado'
                ESCRIBIR 'Participantes esperados: ', total_inscriptos
                
            CASO "L":
                // Registrar llegada
                ESCRIBIR 'Ingrese documento del participante:'
                LEER documento
                SI NO EXISTE_PARTICIPANTE(documento) ENTONCES
                    ESCRIBIR 'Participante no registrado'
                    CONTINUAR
                FIN_SI
                
                id_inscripcion <- BUSCAR_INSCRIPCION_HOY(documento)
                SI id_inscripcion = 0 ENTONCES
                    ESCRIBIR 'Participante no inscrito en eventos de hoy'
                    CONTINUAR
                FIN_SI
                
                SI NO PAGO_REALIZADO(id_inscripcion) ENTONCES
                    ESCRIBIR 'Pago pendiente. Dirigirse a caja'
                    CONTINUAR
                FIN_SI
                
                SI YA_REGISTRO_LLEGADA(id_inscripcion) ENTONCES
                    ESCRIBIR 'Participante ya registró su llegada'
                    MOSTRAR_HORA_LLEGADA(id_inscripcion)
                    CONTINUAR
                FIN_SI
                
                fecha_hora_llegada <- FECHA_HORA_ACTUAL
                presente <- VERDADERO
                REGISTRAR_ASISTENCIA(id_inscripcion, fecha_hora_llegada, presente)
                ESCRIBIR 'Llegada registrada exitosamente'
                MOSTRAR_INFO_EVENTO_PARTICIPANTE(id_inscripcion)
                
            CASO "A":
                // Consultar asistencia
                ESCRIBIR 'Ingrese ID del evento:'
                LEER id_evento
                SI NO EXISTE_EVENTO(id_evento) ENTONCES
                    ESCRIBIR 'Evento no encontrado'
                    CONTINUAR
                FIN_SI
                
                participantes_presentes <- CONTAR_PRESENTES(id_evento)
                total_inscriptos <- CONTAR_INSCRIPTOS_PAGADOS(id_evento)
                participantes_ausentes <- total_inscriptos - participantes_presentes
                
                SI total_inscriptos > 0 ENTONCES
                    porcentaje_asistencia <- (participantes_presentes * 100) / total_inscriptos
                SINO
                    porcentaje_asistencia <- 0
                FIN_SI
                
                ESCRIBIR '=== RESUMEN DE ASISTENCIA ==='
                ESCRIBIR 'Total inscriptos: ', total_inscriptos
                ESCRIBIR 'Presentes: ', participantes_presentes
                ESCRIBIR 'Ausentes: ', participantes_ausentes
                ESCRIBIR 'Porcentaje de asistencia: ', porcentaje_asistencia, '%'
                
                MOSTRAR_LISTA_PRESENTES(id_evento)
                MOSTRAR_LISTA_AUSENTES(id_evento)
                
            CASO "R":
                // Gestionar recursos
                ESCRIBIR 'Ingrese ID del evento:'
                LEER id_evento
                SI EVENTO_EN_CURSO(id_evento) ENTONCES
                    GESTIONAR_RECURSOS_EVENTO(id_evento)
                SINO
                    ESCRIBIR 'Evento no está en curso'
                FIN_SI
                
            CASO "F":
                // Finalizar evento
                ESCRIBIR 'Ingrese ID del evento a finalizar:'
                LEER id_evento
                SI EVENTO_EN_CURSO(id_evento) ENTONCES
                    GENERAR_RESUMEN_FINAL(id_evento)
                    ESCRIBIR '¿Confirma finalización del evento? (S/N):'
                    LEER confirmacion
                    SI confirmacion = "S" ENTONCES
                        CAMBIAR_ESTADO_EVENTO(id_evento, 'finalizado')
                        CERRAR_CONTROL_ASISTENCIA(id_evento)
                        GENERAR_REPORTE_FINAL(id_evento)
                        ESCRIBIR 'Evento finalizado exitosamente'
                    SINO
                        ESCRIBIR 'Operación cancelada'
                    FIN_SI
                SINO
                    ESCRIBIR 'Evento no está en curso'
                FIN_SI
                
            CASO "S":
                ESCRIBIR 'Saliendo del módulo de realización...'
                
            DE_LO_CONTRARIO:
                ESCRIBIR 'Opción no válida. Por favor, intente nuevamente.'
        FIN_SEGUN
        
    HASTA_QUE Input = "S"
FIN
```
