# Algoritmo de Administración de Pagos y Cobros  

  
1. Se muestra un menu con las distintas opciones del sistema de pagos y cobros.  
2. Se elige una de las opciones.  
3. Se realiza la logica de la opcion elegida.  
4. Se muestra la salida de la opcion elegida.  
  
## Nivel de Refinamiento 1  
  
1.1. El sistema despliega en pantalla un menú con las alternativas disponibles para el usuario (registrar pago, consultar pagos, generar recordatorios, procesar reembolsos, generar reportes financieros o salir).  
  
2.1. El usuario ingresa una opción del menú y el sistema la registra.  
  
3.1. El sistema identifica la opción seleccionada.  
3.2. Si corresponde a una funcionalidad válida (registrar pago, consultar pagos, generar recordatorios, procesar reembolsos o generar reportes financieros), se ejecuta el subproceso asociado.  
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
1.7. Mostrar en pantalla: Para generar reportes financieros ingresar > F  
1.8. Mostrar en pantalla: Para salir del módulo ingresar > S  
  
Se elige una de las opciones.  
2.1. Leer y guardar en Input la entrada del usuario.  
  
Se realiza la lógica de la opción elegida.  
3.1. Según el valor de Input:  
3.1.1. Caso "P": Ejecutar el subproceso "Registrar Nuevo Pago".  
3.1.2. Caso "C": Ejecutar el subproceso "Consultar Estado de Pagos".  
3.1.3. Caso "R": Ejecutar el subproceso "Generar Recordatorios".  
3.1.4. Caso "D": Ejecutar el subproceso "Procesar Reembolsos".  
3.1.5. Caso "F": Ejecutar el subproceso "Generar Reportes Financieros".  
3.1.6. Caso "S": Mostrar mensaje: Saliendo del módulo de pagos...  
3.1.7. De lo contrario: Mostrar mensaje: Opción no válida. Intente nuevamente.  
  
Se muestra la salida de la opción elegida.  
4.1. Finalizar el bucle cuando la opción sea "S".  

