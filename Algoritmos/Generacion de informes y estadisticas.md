# Algoritmo de Sistemas de Gestion de Eventos
## 5. Módulo de Generación de Informes y Estadísticas

### Objetivo
Proporcionar a los organizadores del evento herramientas para analizar el rendimiento del mismo, facilitando la toma de decisiones. 📊


### Objetivos Específicos

* **Generar informes de asistencia y participación:**
    * **Gráfico de Asistencia vs. Registro:** Muestra de forma visual la diferencia entre el número de personas que se registraron para 			el evento y el número real de asistentes que hicieron check-in.
    * **Distribución demográfica de los asistentes:** Muestra el porcentaje de asistentes por diferentes categorías como edad, género, 				profesión o país. 
    * **Interés por tipo de contenido o actividad:** Evalúa el nivel de participación y asistencia a sesiones, talleres, conferencias o 			cualquier otra actividad específica dentro del evento.
    * **Tasa de repetición y fidelización:** Se enfoca en el comportamiento de los asistentes a través del tiempo, determinando cuántos 		regresan para participar en futuras ediciones.

* **Presentar estadísticas financieras:**
    * **Pagos registrados por actividad, servicio o ticketing:** Muestra un desglose completo de los ingresos generados (entradas, patrocinios, productos, etc.), permitiendo a los organizadores ver de dónde proviene el dinero.

* **Permitir la exportación de informes:**
    * Ofrecer la posibilidad de descargar los datos y visualizaciones en formatos útiles como **PDF** y **CSV**.
 
---
## Algoritmo

1.  Mostrar el menú principal de informes.
2.  Solicitar al usuario que elija una opción.
3.  Leer la entrada o entradas del usuario (ej. ID del evento).
4.  Procesar datos y generar el informe correspondiente.
5.  Mostrar el informe en pantalla (datos y gráficos), y ofrecer la opción de exportarlo.
6.  Volver al menú principal 

### Nivel de Refinamiento 1

		1.  Mostrar menú principal con los tipos de informes disponibles.
		2.  Leer y validar la opción seleccionada por el usuario.
		3.  Ejecutar la funcionalidad correspondiente según la opción:
			3.1. Generar Informe de Asistencia:Calcular y mostrar la comparativa entre registrados y asistentes.
			3.2. Generar Informe Demográfico:Procesar y visualizar la distribución de los asistentes
			3.3. Generar Informe de Interés:Analizar la participación en las distintas actividades del evento
			3.4. Generar Informe de Fidelización:Identificar y cuantificar asistentes recurrentes.
			3.5. Generar Informe Financiero: Desglosar y totalizar los ingresos.
		4.  Una vez generado un informe, ofrecer la opción de exportarlo (PDF, CSV).
		5.  Repetir el proceso hasta que el usuario decida salir.
		6.  Finalizar el módulo y retornar al menú principal.

### Nivel de Refinamiento 2
		Menú Principal
		1.1. Hacer lo siguiente mientras la opción del usuario no sea "S" (Salir):
		1.2. Mostrar en pantalla: '--- MENÚ DE INFORMES Y ESTADÍSTICAS ---'
		1.3. Mostrar en pantalla: 'Para informe de Asistencia ingresar > A'
		1.4. Mostrar en pantalla: 'Para informe Demográfico ingresar > D'
		1.5. Mostrar en pantalla: 'Para informe de Interés por Actividad ingresar > I'
		1.6. Mostrar en pantalla: 'Para informe de Fidelización ingresar > F'
		1.7. Mostrar en pantalla: 'Para informe Financiero ingresar > N'
		1.8. Mostrar en pantalla: 'Para salir del módulo ingresar > S'
		1.9. Leer y guardar en 'Input' la entrada del usuario (convertir a mayúscula).
		1.10. Según el valor de Input:
			1.10.1. Caso "A": Ejecutar el subproceso "Generar Informe de Asistencia"
			1.10.2. Caso "D": Ejecutar el subproceso "Generar Informe Demográfico".
			1.10.3. Caso "I": Ejecutar el subproceso "Generar Informe de Interés".
			1.10.4. Caso "F": Ejecutar el subproceso "Generar Informe de Fidelización".
			1.10.5. Caso "N": Ejecutar el subproceso "Generar Informe Financiero".
			1.10.6. Caso "S": Mostrar mensaje: 'Saliendo del módulo de informes...'
			1.10.7. De lo contrario: Mostrar mensaje: 'Opción no válida. Intente nuevamente.'
		1.11. Fin del bucle.

#### **2. GENERAR INFORME DE ASISTENCIA**
		 2.1. Permitir elegir el evento 
		 2.2. Leer y guardar en 'id\_evento'.
		 2.3. Verificar si el evento existe y ha finalizado.
		 2.4. Si no es válido:
		     2.4.1. Mostrar mensaje de error.
		     2.4.2. Terminar subproceso.
		 2.5. Si es válido:
		     2.5.1. Obtener `total_registrados` de la base de datos para `id_evento`.
			 2.5.2. Obtener `total_asistentes` (check-ins) de la base de datos para `id_evento`.
		     2.5.3. Calcular `tasa_asistencia = (total_asistentes / total_registrados) * 100`.
		     2.5.4. Mostrar datos en pantalla: 'Total Registrados: \[valor]', 'Total Asistentes: \[valor]', 'Tasa de Asistencia: \[valor]%'.
		     2.5.5. Consultar tipo de grafico, generar y mostrar gráfico seleccionado.
		     2.5.6. Guardar los datos y el gráfico en una variable `datos_informe`.
		     2.5.7. Ejecutar subproceso "Exportar Informe" pasando `datos_informe`.
#### **3. GENERAR INFORME DEMOGRÁFICO**

		 3.1. Permitir elegir el evento 
		 3.2. Leer y guardar en 'id\_evento'.
		 3.3. Verificar si el evento es válido. Si no, terminar.
		 3.4. Obtener la lista de asistentes (`lista_asistentes`) del evento.
		 3.5. Para cada categoría (género, rango de edad, país, profesión):
		     3.5.1. Agrupar y contar los asistentes de `lista_asistentes`.
		     3.5.2. Calcular porcentajes.
		     3.5.3. Mostrar en pantalla los resultados.
		     3.5.4. Consultar tipo de grafico, generar y mostrar gráficos  para cada categoría.
		 3.6. Guardar los datos y gráficos en `datos_informe`.
		 3.7. Ejecutar subproceso "Exportar Informe" pasando `datos_informe`.

#### **4. GENERAR INFORME DE INTERÉS POR ACTIVIDAD**
		
		 4.1. Permitir elegir el evento
		 4.2. Leer y guardar en 'id\_evento'.
		 4.3. Verificar si el evento es válido. Si no, terminar.
		 4.4. Obtener la lista de actividades (`lista_actividades`) del evento.
		 4.5. Para cada actividad en `lista_actividades`:
		     4.5.1. Contar el número de check-ins o asistentes a esa actividad.
		     4.5.2. Guardar el resultado.
		 4.6. Ordenar las actividades de mayor a menor asistencia.
		 4.7. Mostrar en pantalla la lista ordenada: '\[Nombre Actividad]: \[Nº Asistentes]'.
		 4.8. Consultar tipo de grafico, generar y mostrar gráfico seleccionado horizontal con el ranking de actividades.
		 4.9. Guardar datos y gráfico en `datos_informe`.
		 4.10. Ejecutar subproceso "Exportar Informe" pasando `datos_informe`.

#### **5. GENERAR INFORME FINANCIERO**
		
		 5.1. Permitir elegir el evento
		 5.2. Leer y guardar en 'id\_evento'.
		 5.3. Verificar si el evento es válido. Si no, terminar.
		 5.4. Obtener todos los registros de pago (`lista_pagos`) asociados a `id_evento`.
		 5.5. Agrupar `lista_pagos` por categoría (venta de entradas, patrocinios, merchandising, etc.).
		 5.6. Calcular el total de ingresos por cada categoría y el total general.
		 5.7. Mostrar en pantalla el desglose: '\[Categoría]: $\[monto]' y 'Ingresos Totales: $\[monto_total]'.
		 5.8. Consultar tipo de grafico, generar y mostrar gráfico seleccionado con la distribución de ingresos por categoría.
		 5.9. Guardar datos y gráfico en `datos_informe`.
		 5.10. Ejecutar subproceso "Exportar Informe" pasando `datos_informe`.
		
#### **6. SUBPROCESO DE EXPORTACIÓN**

		 6.1. Recibir `datos_informe`.
		 6.2. Mostrar en pantalla: '¿Desea exportar el informe? (S/N)'.
		 6.3. Leer respuesta.
		 6.4. Si respuesta = "S":
		     6.4.1. Mostrar en pantalla: 'Seleccione formato: PDF o CSV'.
		     6.4.2. Leer formato.
		     6.4.3. Si formato = "PDF":
		         6.4.3.1. Generar archivo PDF con `datos_informe`.
		         6.4.3.2. Mostrar mensaje: 'Informe exportado a \[nombre\_archivo.pdf]'.
		     6.4.4. Si formato = "CSV":
		         6.4.4.1. Generar archivo CSV con `datos_informe`.
		         6.4.4.2. Mostrar mensaje: 'Informe exportado a \[nombre\_archivo.csv]'.
		     6.4.5. De lo contrario: Mostrar mensaje: 'Formato no válido'.
		 6.5. Si respuesta = "N":
		     6.5.1. Mostrar mensaje: 'Regresando al menú de informes...'.

---

### Pseudocódigo

#### Programa principal

```python
Menu principal
INICIO
    opcion_usuario = ""
    MIENTRAS opcion_usuario <> "S" HACER
        Mostrar_Menu_Informes()
        LEER opcion_usuario
        opcion_usuario <- MAYUSCULA(opcion_usuario)
        SEGUN opcion_usuario HACER
            CASO "A": Generar_Informe_Asistencia()
            CASO "D": Generar_Informe_Demografico()
            CASO "I": Generar_Informe_Interes()
            CASO "F": Generar_Informe_Fidelizacion()
            CASO "N": Generar_Informe_Financiero()
            CASO "S": Mostrar_Mensaje("Saliendo del módulo...")
            DE LO CONTRARIO: Mostrar_Error("Opción no válida.")
        FIN SEGUN
    FIN MIENTRAS
FIN Proceso

// --- Procesos de Generación de informes---

Funcion Generar_Informe_Asistencia()
INICIO
    id_evento <- Solicitar_Evento()
    SI NOT Validar_Evento_Para_Informe(id_evento) ENTONCES RETORNAR

    datos_asistencia <- OBTENER_DATOS_ASISTENCIA(id_evento) // Retorna {registrados, asistentes, tasa}
    Mostrar_Datos_Asistencia(datos_asistencia)
    grafico <- GENERAR_GRAFICO_ASISTENCIA(datos_asistencia)
    Mostrar_Grafico(grafico)
    
    informe_completo <- EMPAQUETAR_DATOS_Y_GRAFICO(datos_asistencia, grafico)
    Exportar_Informe(informe_completo, "Asistencia")
FIN Funcion

Funcion Generar_Informe_Demografico()
INICIO
    id_evento <- Solicitar_Evento()
    SI NOT Validar_Evento_Para_Informe(id_evento) ENTONCES RETORNAR

    datos_demograficos <- OBTENER_DATOS_DEMOGRAFICOS(id_evento) // Retorna {genero, edad, pais...}
    Mostrar_Datos_Demograficos(datos_demograficos)
    graficos <- GENERAR_GRAFICOS_DEMOGRAFICOS(datos_demograficos)
    Mostrar_Graficos(graficos)

    informe_completo <- EMPAQUETAR_DATOS_Y_GRAFICO(datos_demograficos, graficos)
    Exportar_Informe(informe_completo, "Demografico")
FIN Funcion

Funcion Generar_Informe_Interes()
INICIO
    id_evento <- Solicitar_Evento()
    SI NOT Validar_Evento_Para_Informe(id_evento) ENTONCES RETORNAR

    datos_interes <- OBTENER_DATOS_INTERES_ACTIVIDADES(id_evento) // Retorna ranking de actividades
    Mostrar_Ranking_Actividades(datos_interes)
    grafico <- GENERAR_GRAFICO_RANKING(datos_interes)
    Mostrar_Grafico(grafico)
    
    informe_completo <- EMPAQUETAR_DATOS_Y_GRAFICO(datos_interes, grafico)
    Exportar_Informe(informe_completo, "Interes_Actividades")
FIN Funcion

Funcion Generar_Informe_Fidelizacion()
INICIO
    
    datos_fidelizacion <- OBTENER_DATOS_FIDELIZACION() // Retorna {total_asistentes_unicos, recurrentes, tasa_retorno}
    Mostrar_Datos_Fidelizacion(datos_fidelizacion)
    
    // Se retorna un listado, no un grafico.
    Exportar_Informe(datos_fidelizacion, "Fidelizacion")
FIN Funcion

Funcion Generar_Informe_Financiero()
INICIO
    id_evento <- Solicitar_Evento()
    SI NOT Validar_Evento_Para_Informe(id_evento) ENTONCES RETORNAR

    datos_financieros <- OBTENER_DATOS_FINANCIEROS(id_evento) // Retorna desglose y total de ingresos
    Mostrar_Datos_Financieros(datos_financieros)
    grafico <- GENERAR_GRAFICO_INGRESOS(datos_financieros)
    Mostrar_Grafico(grafico)

    informe_completo <- EMPAQUETAR_DATOS_Y_GRAFICO(datos_financieros, grafico)
    Exportar_Informe(informe_completo, "Financiero")
FIN Funcion

// --- Función de Exportación de informes---


Funcion Exportar_Informe(datos, nombre_base_informe)
INICIO
    SI Usuario_Confirma_Operacion("¿Desea exportar este informe?") ENTONCES
        ESCRIBIR "Seleccione formato de exportación (PDF / CSV):"
        LEER formato
        formato <- MAYUSCULA(formato)
        SEGUN formato HACER
            CASO "PDF":
                nombre_archivo <- GENERAR_PDF(datos, nombre_base_informe)
                Mostrar_Exito("Informe exportado a: " + nombre_archivo)
            CASO "CSV":
                nombre_archivo <- GENERAR_CSV(datos, nombre_base_informe)
                Mostrar_Exito("Informe exportado a: " + nombre_archivo)
            DE LO CONTRARIO:
                Mostrar_Error("Formato no válido.")
        FIN SEGUN
    FIN SI
FIN Funcion

// --- Funciones de Utilidad ---


Funcion Validar_Evento_Para_Informe(id_evento) : booleano
INICIO
    SI NO EXISTE_EVENTO(id_evento) ENTONCES
        Mostrar_Error("Evento no encontrado.")
        RETORNAR FALSO
    FIN SI
    info_evento <- OBTENER_INFO_EVENTO(id_evento)
    SI info_evento.fecha > FECHA_ACTUAL ENTONCES
        Mostrar_Error("El informe solo puede generarse para eventos que ya han finalizado.")
        RETORNAR FALSO
    FIN SI
    RETORNAR VERDADERO
FIN Funcion

Funcion Solicitar_Evento() : entero
INICIO
    ESCRIBIR "Ingrese el nombre o parte del nombre del evento:"
    LEER criterio_busqueda

    // 1. Ejecutar búsqueda en la base de datos
    // La búsqueda debe filtrar por eventos que contengan 'criterio_busqueda' en su nombre  y que ya hayan 'finalizado' 
    lista_coincidentes <- BUSCAR_EVENTOS_FINALIZADOS(criterio_busqueda) 

    SI TAMAÑO(lista_coincidentes) = 0 ENTONCES
        ESCRIBIR "No se encontraron eventos finalizados con ese nombre."
        RETORNAR 0 // Retorna 0 o nulo para indicar fallo
    FIN SI

    // 2. Mostrar la lista de opciones al usuario
    ESCRIBIR "--- Eventos Coincidentes ---"
    contador <- 1
    PARA CADA evento EN lista_coincidentes HACER
        ESCRIBIR contador, ". ", evento.nombre, " (ID: ", evento.id, ")"
        contador <- contador + 1
    FIN PARA
    
    // 3. Solicitar la selección
    ESCRIBIR "Ingrese el número de la opción deseada (o 0 para cancelar):"
    LEER opcion_seleccionada

    // 4. Validar y obtener el ID real
    SI opcion_seleccionada = 0 O opcion_seleccionada < 1 O opcion_seleccionada >= contador ENTONCES
        ESCRIBIR "Selección cancelada o no válida."
        RETORNAR 0 // Retorna 0 si la selección es inválida o cancelada
    FIN SI
    
    // Obtener el ID del evento que corresponde a la opción seleccionada
    indice <- opcion_seleccionada - 1 
    id_evento_seleccionado <- lista_coincidentes[indice].id
    
    // 5. Retornar el ID real
    RETORNAR id_evento_seleccionado
FIN Funcion

Funcion Usuario_Confirma_Operacion(mensaje) : booleano
    ESCRIBIR mensaje + " (S/N):"
    LEER respuesta
    RETORNAR (MAYUSCULA(respuesta) = "S")
FIN Funcion
