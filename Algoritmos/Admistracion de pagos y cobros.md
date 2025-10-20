# Algoritmo de Administración de Pagos y Cobros  

  
1. Se muestra un menu con las distintas opciones del sistema de pagos y cobros.  
2. Se elige una de las opciones.  
3. Se realiza la logica de la opcion elegida.  
4. Se muestra la salida de la opcion elegida.  
  
## Nivel de Refinamiento 1  
  
1.1. El sistema despliega en pantalla un menú con las alternativas disponibles para el usuario (registrar pago, consultar pagos, generar recordatorios, procesar reembolsos o salir).  
  
2.1. El usuario ingresa una opción del menú y el sistema la registra.  
  
3.1. El sistema identifica la opción seleccionada.  
3.2. Si corresponde a una funcionalidad válida (registrar pago, consultar pagos, generar recordatorios o procesar reembolsos), se ejecuta el subproceso asociado.  
3.3. Si la opción ingresada es salir, se prepara la finalización del módulo.  
3.4. Si la opción no es válida, se muestra un mensaje de error solicitando un nuevo intento.  
  
4.1. El sistema presenta en pantalla el resultado del subproceso ejecutado o el mensaje correspondiente según el caso.  
4.2. El ciclo continúa hasta que el usuario elija la opción de salir.  
  
## Nivel de Refinamiento 2  
  
Nivel de Refinamiento 2
  
Se muestra un menú con las distintas opciones del sistema de pagos y cobros.  
1.1. Hacer lo siguiente mientras la opción del usuario no sea "S" (Salir):  
1.2. Mostrar en pantalla: --- MENÚ ADMINISTRACIÓN DE PAGOS ---  
1.3. Mostrar en pantalla: Para registrar pago ingresar > P  
1.4. Mostrar en pantalla: Para consultar pagos ingresar > C  
1.5. Mostrar en pantalla: Para generar recordatorios ingresar > R  
1.6. Mostrar en pantalla: Para procesar reembolsos ingresar > D  
1.8. Mostrar en pantalla: Para salir del módulo ingresar > S  
  
Se elige una de las opciones.  
2.1. Leer y guardar en Input la entrada del usuario.  
  
Se realiza la lógica de la opción elegida.  
3.1. Según el valor de Input:  
3.1.1. Caso "P": Ejecutar el subproceso "Registrar Nuevo Pago".  
3.1.2. Caso "C": Ejecutar el subproceso "Consultar Estado de Pagos".  
3.1.3. Caso "R": Ejecutar el subproceso "Generar Recordatorios".  
3.1.4. Caso "D": Ejecutar el subproceso "Procesar Reembolsos".   
3.1.6. Caso "S": Mostrar mensaje: Saliendo del módulo de pagos...  
3.1.7. De lo contrario: Mostrar mensaje: Opción no válida. Intente nuevamente.  
  
Se muestra la salida de la opción elegida.  
4.1. Finalizar el bucle cuando la opción sea "S".  

# Modulos

 ## Algoritmo: Registrar Nuevo Pago
 1. Solicitar el ID de la inscripción para el pago.
 2. Verificar la existencia de la inscripción.
 3. Obtener la información de la inscripción.
 4. Verificar que el estado de pago de la inscripción no sea "Pagado".
 5. Solicitar el monto y el método de pago.
 6. Validar los datos del pago.
 7. Registrar el pago en la Base de Datos (BD) de pagos.
 8. Actualizar el estado de pago de la inscripción a "Pagado".
 9. Mostrar mensaje de éxito.
 
 ## Refinamiento 
 1. Llamar a la función Solicitar_ID_Inscripcion() para obtener id_inscripcion.
 2. Si Existe_Inscripcion(id_inscripcion) es FALSO, mostrar error y terminar.
 3. Llamar a Obtener_Info_Inscripcion(id_inscripcion) para obtener info_inscripcion.
 4. Si info_inscripcion.estado_pago es igual a "Pagado", mostrar advertencia ("El pago ya fue registrado") y terminar.
 5. Llamar a Solicitar_Monto_Pago() y Solicitar_Metodo_Pago() para obtener monto_pago y metodo_pago.
 6. Validar los datos del pago.
    6.1 Llamar a Obtener_Evento_De_Inscripcion(id_inscripcion) para obtener id_evento.
    6.2 Llamar a Obtener_Info_Evento(id_evento) para obtener info_evento.
    6.3 Si monto_pago es menor que info_evento.precio, mostrar error ("Monto insuficiente") y terminar.
 7. Llamar a Guardar_Pago(id_inscripcion, monto_pago, metodo_pago, fecha_actual) (función de BD abstracta).
 8. Llamar a Actualizar_Estado_Inscripcion(id_inscripcion, "Pagado").
 9. Mostrar "Pago registrado y estado de inscripción actualizado.

 ## Algoritmo: Consultar Estado de Pagos

 1. Solicitar el ID de un evento.
 2. Identificar criterio de busqueda.
 3. Buscar las inscripciones y sus estados de pago asociados al criterio.
 3. Mostrar el listado de resultados (evento, participante, estado de pago).
 4. Si no hay resultados, mostrar un mensaje informativo.
 
 ## Nivel de Refinamiento 
 
 1. Llamar a Solicitar_Criterio_Consulta() para obtener criterio y valor. 
 
 2. Identificar el criterio de búsqueda.

 3. Si criterio es evento
    3.1. Si Existe_Evento(valor) es FALSO, mostrar error y terminar. 
    3.2. Llamar a Buscar_Inscripciones_Por_Evento(valor) para obtener lista_inscripciones.
    Si no 
    3.3. Si Existe_Participante(valor) es FALSO, mostrar error y terminar.
    3.4. Llamar a obtener_ID_participante(valor)
    3.5. Llamar a Buscar_Inscripciones_Por_Participante(id_participante) para obtener lista_inscripciones.

 4. Para cada inscripcion en lista_inscripciones:
    4.1. Obtener info_participante con Obtener_Info_Participante(inscripcion.id_participante).
    4.2. Obtener info_evento con Obtener_Info_Evento(inscripcion.id_evento).
    4.3. Mostrar info_evento.nombre, info_participante.nombre, info_participante.documento, inscripcion.estado_pago.

 5. Si lista_incripciones esta vacia mostrar "No se encontraron inscripciones"

 ## Algoritmo: Generar Recordatorios

 1. Identificar eventos activos y futuros.
 2. Buscar inscripciones con estado de pago "Pendiente" o similar para esos eventos.
 3. Generar un mensaje de recordatorio.
 4. Enviar el recordatorio al email de los participantes morosos.
 5. Registrar el envío del recordatorio.
 
 ## Nivel de Refinamiento 

 1. Llamar a Obtener_Eventos_Activos_Y_Futuros() para obtener lista_eventos_futuros.
 2. Si lista_eventos_futuros está vacía, mostrar mensaje y terminar.
 3. Inicializar contador_enviados en 0.
 4. Para cada evento en lista_eventos_futuros:
    4.1. Llamar a Buscar_Inscripciones_Pendientes_Pago(evento.id) (función de BD abstracta) para obtener inscripciones_pendientes.
    4.2. Para cada inscripcion en inscripciones_pendientes:
        4.2.1. Obtener info_participante con Obtener_Info_Participante(inscripcion.id_participante).
        4.2.2. mensaje ← Construir_Recordatorio_Pago(evento, info_participante).
        4.2.3. Llamar a ENVIAR_EMAIL(info_participante.email, "Recordatorio de Pago - " + evento.nombre, mensaje)
        4.2.4. contador_enviados ← contador_enviados + 1.
 5. Mostrar Mostrar_Exito("Proceso finalizado. Se enviaron " + contador_enviados + " recordatorios de pago.").

## Algoritmo: Procesar Reembolsos

1. Solicitar ID de la inscripción a reembolsar.
2. Validar que la inscripción exista y el evento no haya ocurrido.
3. Verificar que el pago haya sido registrado.
4. Solicitar confirmación para la operación.
5. Registrar el reembolso.
6. Actualizar el estado de la inscripción a "Cancelada" o "Reembolsadao".
7. Mostrar mensaje de éxito.

Nivel de Refinamiento 1

1. Llamar a Solicitar_ID_Inscripcion() para obtener id_inscripcion.
2. Llamar a Validar_Inscripcion_Para_Cancelacion(id_inscripcion). Si es FALSO, terminar.
3. Verificar que el pago haya sido registrado.
    3.1 Llamar a Obtener_Info_Inscripcion(id_inscripcion) para obtener info_inscripcion.
    3.2 Si info_inscripcion.estado_pago es diferente de "Pagado", mostrar "No hay pago registrado para reembolsar" y terminar.
4. Solicitar confirmación para la operación.
    4.2 Mostrar "¿Desea continuar con el reembolso?"
    4.1 Si Usuario_Confirma_Reembolso() es FALSO, mostrar mensaje y terminar.
5. Registrar el reembolso.
    5.1. Llamar a Obtener_Monto_Pagado(id_inscripcion) para obtener monto_reembolsar.
    5.2. Llamar a GUARDAR_REEMBOLSO(id_inscripcion, monto_reembolsar, FECHA_ACTUAL)
6. Llamar a Actualizar_Estado_Inscripcion(id_inscripcion, "Reembolsada").
7. Mostrar"Reembolso de " + monto_reembolsar + " procesado. Estado actualizado a 'Reembolsado'."

# Pseudocodigo

INICIO Programa

    opcion <- ""
    
    MIENTRAS opcion <> "S" HACER
        
        Mostrar("--- MENÚ ADMINISTRACIÓN DE PAGOS ---") // Reusa Mostrar
        Mostrar("Para registrar pago ingresar > P")
        Mostrar("Para consultar pagos ingresar > C")
        Mostrar("Para generar recordatorios ingresar > R")
        Mostrar("Para procesar reembolsos ingresar > D")
        Mostrar("Para salir del módulo ingresar > S")
        
        ESCRIBIR "Ingrese una opción:"
        LEER Input 
        opcion <- MAYUSCULA(Input)
        
        SEGUN opcion HACER
            CASO "P": 
                Registrar_Nuevo_Pago()
            CASO "C": 
                Consultar_Estado_De_Pagos()
            CASO "R": 
                Generar_Recordatorios()
            CASO "D": 
                Procesar_Reembolsos()
            CASO "S": 
                Mostrar("Saliendo del módulo de pagos...")
            OTRO CASO: 
                Mostrar("Opción no válida. Intente nuevamente.")
        FIN SEGUN
        
    FIN MIENTRAS

FIN Programa

// Submodulos

Funcion Registrar_Nuevo_Pago()
INICIO
    id_inscripcion <- Solicitar_ID_Inscripcion()
    
    SI NOT Existe_Inscripcion(id_inscripcion) ENTONCES
        Mostrar("Inscripción no encontrada.")
        RETORNAR
    FIN SI
    
    info_inscripcion <- Obtener_Info_Inscripcion(id_inscripcion)
    
    SI info_inscripcion.estado_pago = "Pagado" ENTONCES
        Mostrar("El pago ya fue registrado para esta inscripción.")
        RETORNAR
    FIN SI
    
    monto_pago <- Solicitar_Monto_Pago() 
    metodo_pago <- Solicitar_Metodo_Pago() 
    
    id_evento <- Obtener_Evento_De_Inscripcion(id_inscripcion)
    info_evento <- Obtener_Info_Evento(id_evento)
    
    SI monto_pago < info_evento.precio ENTONCES
        Mostrar("Monto ingresado (" + monto_pago + ") es insuficiente. Precio requerido: " + info_evento.precio)
        RETORNAR
    FIN SI
    
    GUARDAR_PAGO(id_inscripcion, monto_pago, metodo_pago, FECHA_ACTUAL) 
    
    Actualizar_Estado_Inscripcion(id_inscripcion, "Pagado")
    
    Mostrar("Pago registrado y estado de inscripción actualizado a 'Pagado'.")
FIN Funcion


Funcion Consultar_Estado_De_Pagos()
INICIO
    ESCRIBIR "¿Desea consultar por [E]vento o [P]articipante?"
    LEER opcion
    opcion <- MAYUSCULA(opcion)
    lista_inscripciones <- NULO
    
    SI opcion = "E" ENTONCES
        id_evento <- Solicitar_ID_Evento()
        SI NOT Existe_Evento(id_evento) ENTONCES
            Mostrar("Evento no encontrado")
            RETORNAR
        FIN SI
        lista_inscripciones <- BUSCAR_INSCRIPCIONES_POR_EVENTO(id_evento) 
        
    SINO SI opcion = "P" ENTONCES
        documento <- Solicitar_Documento_Participante()
        SI NOT Existe_Participante(documento) ENTONCES
            Mostrar("Participante no encontrado")
            RETORNAR
        FIN SI
        id_participante <- Obtener_ID_Participante(documento)
        lista_inscripciones <- BUSCAR_INSCRIPCIONES_POR_PARTICIPANTE(id_participante)
        
    SINO
        Mostrar_Error("Opción no válida")
        RETORNAR
    FIN SI
    
    SI lista_inscripciones = NULO O TAMAÑO(lista_inscripciones) = 0 ENTONCES
        Mostrar("No se encontraron inscripciones con pagos asociados para el criterio seleccionado.")
        RETORNAR
    FIN SI
    
    Mostrar("ESTADO DE PAGOS ENCONTRADOS")
    
    PARA CADA inscripcion EN lista_inscripciones HACER
        info_participante <- Obtener_Info_Participante(inscripcion.id_participante)
        info_evento <- Obtener_Info_Evento(inscripcion.id_evento)
        
        ESCRIBIR "Evento: " + info_evento.nombre + " | Participante: " + info_participante.nombre + " (" + info_participante.documento + ") | Estado Pago: " + inscripcion.estado_pago
    FIN PARA
    
FIN Funcion


Funcion Generar_Recordatorios()
INICIO
    lista_eventos_futuros <- OBTENER_EVENTOS_ACTIVOS_Y_FUTUROS() 
    
    SI TAMAÑO(lista_eventos_futuros) = 0 ENTONCES
        RETORNAR
    FIN SI
    
    contador_enviados <- 0
    
    PARA CADA evento EN lista_eventos_futuros HACER
        inscripciones_pendientes <- BUSCAR_INSCRIPCIONES_PENDIENTES_PAGO(evento.id) 
        
        PARA CADA inscripcion EN inscripciones_pendientes HACER
            info_participante <- Obtener_Info_Participante(inscripcion.id_participante)
            mensaje <- "Estimado info_participante.nombre..."
            
            ENVIAR_EMAIL(info_participante.email, "Recordatorio de Pago: " + evento.nombre, mensaje) 
            
            contador_enviados <- contador_enviados + 1
        FIN PARA
    FIN PARA
    
    Mostrar("Proceso finalizado. Se enviaron " + contador_enviados + " recordatorios de pago")
FIN Funcion


Funcion Procesar_Reembolsos()
INICIO
    id_inscripcion <- Solicitar_ID_Inscripcion()
    
    SI NOT Validar_Inscripcion_Para_Cancelacion(id_inscripcion) ENTONCES 
        RETORNAR
    FIN SI
    
    info_inscripcion <- Obtener_Info_Inscripcion(id_inscripcion)
    
    SI info_inscripcion.estado_pago <> "Pagado" ENTONCES
        Mostrar("No hay un pago registrado o confirmado para la inscripción " + id_inscripcion + ". No se procede con el reembolso.")
        RETORNAR
    FIN SI
    
    SI NOT Usuario_Confirma_Operacion() ENTONCES
        Mostrar("Operación de reembolso cancelada por el usuario.")
        RETORNAR
    FIN SI
    
    monto_reembolsar <- OBTENER_MONTO_PAGADO(id_inscripcion) 
    
    GUARDAR_REEMBOLSO(id_inscripcion, monto_reembolsar, FECHA_ACTUAL) 
    
    Actualizar_Estado_Inscripcion(id_inscripcion, "Cancelada")
    
    Mostrar("Reembolso de " + monto_reembolsar + " procesado con éxito. Inscripción cancelada.")
FIN Funcion