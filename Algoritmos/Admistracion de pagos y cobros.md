# Algoritmo de Sistemas de Gestion de Eventos  
  
1. Se muestra un menu con las distintas opciones del sistema de pagos y cobros.  
2. Se elige una de las opciones.  
3. Se realiza la logica de la opcion elegida.  
4. Se muestra la salida de la opcion elegida.  
  
## Nivel de Refinamiento 1  
  
1.1. El sistema despliega en pantalla un menú con las alternativas disponibles para el usuario (registrar pago, consultar pagos, generar recordatorios, procesar reembolsos, generar reportes financieros o salir).  
  
2.1. El usuario ingresa una opción del menú y el sistema la registra.  
  
3.1. El sistema identifica la opción seleccionada.  
3.2. Si corresponde a una funcionalidad válida (registrar pago, consultar pagos, generar recordatorios, procesar reembolsos), se ejecuta la Funcion asociada.  
3.3. Si la opción ingresada es salir, se prepara la finalización del módulo.  
3.4. Si la opción no es válida, se muestra un mensaje de error solicitando un nuevo intento.  
  
4.1. El sistema presenta en pantalla el resultado del Funcion ejecutado o el mensaje correspondiente según el caso.  
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
3.1.1. Caso "P": Ejecutar el Funcion "Registrar Nuevo Pago".  
3.1.2. Caso "C": Ejecutar el Funcion "Consultar Estado de Pagos".  
3.1.3. Caso "R": Ejecutar el Funcion "Generar Recordatorios".  
3.1.4. Caso "D": Ejecutar el Funcion "Procesar Reembolsos".  
3.1.6. Caso "S": Mostrar mensaje: Saliendo del módulo de pagos...  
3.1.7. De lo contrario: Mostrar mensaje: Opción no válida. Intente nuevamente.  
  
Se muestra la salida de la opción elegida.  
4.1. Finalizar el bucle cuando la opción sea "S".  

## Pseudocodigo

Algoritmo Sistema_Gestion_Pagos
    Repetir
        Escribir "--- MENÚ ADMINISTRACIÓN DE PAGOS ---"
        Escribir "Para registrar pago ingresar         > P"
        Escribir "Para consultar pagos ingresar        > C"
        Escribir "Para generar recordatorios ingresar  > R"
        Escribir "Para procesar reembolsos ingresar    > D"
        Escribir "Para salir del módulo ingresar       > S"
        Escribir "--------------------------------------"
        Escribir "Ingrese su opción:"

        Leer opcion
        Mayusculas(opcion)

        Segun opcion Hacer
            Caso "P":
                RegistrarNuevoPago()
            Caso "C":
                ConsultarEstadoDePagos()
            Caso "R":
                GenerarRecordatorios()
            Caso "D":
                ProcesarReembolsos()
    Hasta Que opcion = "S"
FinAlgoritmo

Funcion RegistrarNuevoPago
    Definir ID_Evento, ID_Cliente, Monto, FechaPago, MetodoPago Como Cadena
    Definir PagoValido Como Logico
    
    PagoValido <- Falso
    
    Mientras PagoValido = Falso Hacer
        Escribir "--- REGISTRAR NUEVO PAGO ---"
        
        Escribir "Ingrese ID del Evento:"
        Leer ID_Evento
        Escribir "Ingrese ID del Participante/Cliente:"
        Leer ID_Participante
        Escribir "Ingrese Monto del Pago (Ej: 150.00):"
        Leer Monto
        Escribir "Ingrese Fecha del Pago (Formato AAAA-MM-DD):"
        Leer FechaPago
        Escribir "Ingrese Método de Pago (Ej: Tarjeta, Transferencia, Efectivo):"
        Leer MetodoPago
        
        Si ID_Evento <> "" Y ID_Participante <> "" Y Monto > 0 Y EsFechaValida(FechaPago) Entonces
            ID_Transaccion <- GenerarIDUnico()
            
            GuardarRegistro(ID_Transaccion, ID_Evento, ID_Participante, Monto, FechaPago, MetodoPago, "Completado")
            
            Escribir "Exito: Pago con ID " + ID_Transaccion + " registrado correctamente."
            Escribir "Monto: " + Monto + ", Metodo: " + MetodoPago
            
            PagoValido <- Verdadero
        Sino
            Escribir "Error de Validacion"
        FinSi
    FinMientras
FinFuncion

Funcion ConsultarEstadoDePagos
    Definir Resultados Como ArregloDePagos
    
    Escribir "--- CONSULTAR ESTADO DE PAGOS ---"
        
    Escribir "Ingrese ID del Evento a consultar:"
    Leer ValorBusqueda
    Resultados <- BuscarPagosPorEvento(ValorBusqueda)

    Si Tamaño(Resultados) > 0 Entonces    
        Escribir "ID Transaccion: " + Pago.ID_Transaccion
        Escribir "Participante: " + Pago.ID_Participante
        Escribir "Monto: " + Pago.Monto + ", Estado: " + Pago.Estado
        Escribir "Fecha de Pago: " + Pago.FechaPago
    Sino
        Escribir "No se encontraron pagos para id de evento ingresado."
    FinSi
FinFuncion

Funcion GenerarRecordatorios
    Definir ID_Evento, FechaLimite Como Cadena
    Definir Cliente Como ArregloDeCliente
    
    Escribir "--- GENERAR RECORDATORIOS DE PAGO ---"
    
    Escribir "Ingrese ID del Evento para el cual generar recordatorios:"
    Leer ID_Evento
    Escribir "Ingrese Fecha Limite de Pago Vencida (Formato AAAA-MM-DD):"
    Leer FechaLimite
    
    ContadorEnviados <- 0
    
  
    Cliente <- ClientePagoPendiente(ID_Evento, FechaLimite)
    
    Si Tamaño(Cliente) > 0 Entonces
        Escribir "Se encontro cliente con pago pendiente."
        Si EnviarNotificacion(Cliente.Email, "Recordatorio de Pago Pendiente", Cliente.MontoPendiente) Entonces
            RegistrarLog("Recordatorio enviado a: " + Cliente.ID_Cliente)
        FinSi
        FinPara
    Sino
        Escribir "No se encontraron pagos pendientes que requieran recordatorio."
    FinSi
FinFuncion

Funcion ProcesarReembolsos
    Definir ID_Transaccion, Motivo Como Cadena
    Definir PagoEncontrado, Aprobado, ReembolsoExitoso Como Logico
    
    Escribir "--- PROCESAR REEMBOLSOS ---"
    
    Escribir "Ingrese ID de la Transaccion a Reembolsar:"
    Leer ID_TransaccionOriginal
    
    PagoEncontrado <- ConsultarTransaccion(ID_TransaccionOriginal)
    
    Si PagoEncontrado = Verdadero Y PagoEncontrado.Estado = "Completado" Entonces
        
        Escribir "Monto Pagado: " + PagoEncontrado.Monto + ". Fecha: " + PagoEncontrado.FechaPago

        Escribir "Ingrese Motivo del Reembolso:"
        Leer Motivo
        
        Aprobado <- SolicitarAprobacion(ID_TransaccionOriginal, Motivo)
        
        Si Aprobado = Verdadero Entonces
            ReembolsoExitoso <- EjecutarDevolucion(ID_TransaccionOriginal, PagoEncontrado.Monto, PagoEncontrado.MetodoPago)
            
            Si ReembolsoExitoso = Verdadero Entonces
                ActualizarEstadoPago(ID_TransaccionOriginal, "Reembolsado")
                RegistrarNuevoReembolso(ID_TransaccionOriginal, PagoEncontrado.Monto, Motivo, "Exito")
                
                Escribir "Exito: Reembolso de " + PagoEncontrado.Monto + " procesado para la transaccion " + ID_TransaccionOriginal
            Sino
                Escribir "Error: No se pudo ejecutar el reembolso con el proveedor de pagos."
                RegistrarNuevoReembolso(ID_TransaccionOriginal, PagoEncontrado.Monto, Motivo, "Fallo en Proveedor")
            FinSi
        Sino
            Escribir "Proceso cancelado: La solicitud de reembolso no fue aprobada."
        FinSi
        
    Sino Si PagoEncontrado = Verdadero Y PagoEncontrado.Estado = "Reembolsado" Entonces
        Escribir "Error: La transaccion ya ha sido marcada como Reembolsada."
    Sino
        Escribir "Error: La transaccion " + ID_TransaccionOriginal + " no fue encontrada o no es valida para reembolso."
    FinSi
FinFuncion