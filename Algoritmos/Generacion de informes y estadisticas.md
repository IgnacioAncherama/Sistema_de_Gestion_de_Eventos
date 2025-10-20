# Algoritmo de Sistemas de Gestion de Eventos
## 5. Módulo de Generación de Informes y Estadísticas
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
		 2.1. Llamar a la función Solicitar_ID_Evento() y guardar la entrada en la variable id_evento
		 2.2. Verificar la validez del evento llamando a Validar_Evento(id_evento)
		 2.3. Si no es válido:
		     2.3.1. Terminar subproceso.
		 2.4. Si es válido:
		     2.4.1. Obtener `total_registrados` de la base de datos para `id_evento`.
			 2.4.2. Obtener `total_asistentes` (check-ins) de la base de datos para `id_evento`.
		     2.4.3. Calcular `tasa_asistencia = (total_asistentes / total_registrados) * 100`.
		     2.4.4. Mostrar datos en pantalla: 'Total Registrados: \[valor]', 'Total Asistentes: \[valor]', 'Tasa de Asistencia: \[valor]%'.
		     2.4.5. Consultar tipo de grafico llamando al modulo Obtener_Tipo_Grafico() y guardar la entrada en tipo_grafico
			 2.4.6  Generar_Grafico(tipo_grafico,total_registrados,total_asistentes,tasa_asistencia) y mostrar gráfico.
		     2.4.7. Guardar los datos y el gráfico en una variable `datos_informe`.
		     2.4.8. Ejecutar subproceso "Exportar Informe" pasando `datos_informe`.
#### **3. GENERAR INFORME DEMOGRÁFICO**

		 3.1. Llamar a la función Solicitar_ID_Evento() y guardar la entrada en la variable id_evento
		 3.2. Verificar la validez del evento llamando a Validar_Evento(id_evento)
		 3.3. Si no es válido:
		     3.3.1. Terminar subproceso.
		Si la función devuelve VERDADERO:
   			 4.1. Obtener la lista de asistentes (lista_asistentes) del evento de la base de datos.
    		 4.2. Inicializar la variable datos_informe_demografico para almacenar todos los resultados y gráficos.
			 4.3. Para cada categoría (género, rango de edad, país, profesión):
        			4.3.1. Agrupar y contar los asistentes de lista_asistentes por cada sub-atributo de la categoría (ej: "Masculino", "Femenino"). Guardar en datos_conte
					4.3.2. Calcular el porcentaje de cada sub-atributo con respecto al total de lista_asistentes. Guardar en datos_porcentaje.
					4.3.3. Mostrar en pantalla los resultados de la categoría (usando datos_porcentaje).
					4.3.4. Consultar tipo de gráfico llamando al módulo Obtener_Tipo_Grafico() y guardar la entrada en tipo_grafico.
					4.3.5. Generar el gráfico demográfico específico gráfico <- Generar_Grafico(tipo_grafico, datos_porcentaje, categoría)
					4.3.6. Guardar la categoría, datos_porcentaje y gráfico en la variable datos_informe_demografico.
			4.4. Ejecutar subproceso "Exportar Informe" pasando datos_informe_demografico.

#### **4.GENERAR INFORME DE INTERÉS POR ACTIVIDAD**
		
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

**NOTA**: Este módulo utiliza funciones del archivo `Funciones_Comunes.md`

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
// Utiliza: Validar_Evento_Finalizado
INICIO
    id_evento <- Solicitar_Evento()
    SI NOT Validar_Evento_Finalizado(id_evento) ENTONCES RETORNAR

    datos_asistencia <- OBTENER_DATOS_ASISTENCIA(id_evento) // Retorna {registrados, asistentes, tasa}
    Mostrar_Datos_Asistencia(datos_asistencia)
	tipo_grafico <- Obtener_Tipo_Grafico() 
    grafico <- GENERAR_GRAFICO_ASISTENCIA(datos_asistencia,tipo_grafico)
    Mostrar_Grafico(grafico)
    
    informe_completo <- EMPAQUETAR_DATOS_Y_GRAFICO(datos_asistencia, grafico)
    Exportar_Informe(informe_completo, "Asistencia")
FIN Funcion

Funcion Generar_Informe_Demografico()
// Utiliza: Validar_Evento_Finalizado
INICIO
    id_evento <- Solicitar_Evento()
    SI NOT Validar_Evento_Finalizado(id_evento) ENTONCES RETORNAR

    datos_demograficos <- OBTENER_DATOS_DEMOGRAFICOS(id_evento) // Retorna {genero, edad, pais...}
	tipo_grafico <- Obtener_Tipo_Grafico() 
    Mostrar_Datos_Demograficos(datos_demograficos)
    graficos <- GENERAR_GRAFICOS_DEMOGRAFICOS(datos_demograficos,tipo_grafico)
    Mostrar_Graficos(graficos)

    informe_completo <- EMPAQUETAR_DATOS_Y_GRAFICO(datos_demograficos, graficos)
    Exportar_Informe(informe_completo, "Demografico")
FIN Funcion

Funcion Generar_Informe_Interes()
// Utiliza: Validar_Evento_Finalizado
INICIO
    id_evento <- Solicitar_Evento()
    SI NOT Validar_Evento_Finalizado(id_evento) ENTONCES RETORNAR

    datos_interes <- OBTENER_DATOS_INTERES_ACTIVIDADES(id_evento) // Retorna ranking de actividades
	tipo_grafico <- Obtener_Tipo_Grafico() 
    Mostrar_Ranking_Actividades(datos_interes)
    grafico <- GENERAR_GRAFICO_RANKING(datos_interes,tipo_grafico)
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
// Utiliza: Validar_Evento_Finalizado
INICIO
    id_evento <- Solicitar_Evento()
    SI NOT Validar_Evento_Finalizado(id_evento) ENTONCES RETORNAR

    datos_financieros <- OBTENER_DATOS_FINANCIEROS(id_evento) // Retorna desglose y total de ingresos
	tipo_grafico <- Obtener_Tipo_Grafico() 
    Mostrar_Datos_Financieros(datos_financieros)
    grafico <- GENERAR_GRAFICO_INGRESOS(datos_financieros,tipo_grafico)
    Mostrar_Grafico(grafico)

    informe_completo <- EMPAQUETAR_DATOS_Y_GRAFICO(datos_financieros, grafico)
    Exportar_Informe(informe_completo, "Financiero")
FIN Funcion

// --- Función de Exportación de informes---


Funcion Exportar_Informe(datos, nombre_base_informe)
// Utiliza: Usuario_Confirma_Operacion, Mostrar_Exito, Mostrar_Error
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
Funcion Obtener_Tipo_Grafico(): cadena
INICIO
    ESCRIBIR "Seleccione el tipo de visualización "
    ESCRIBIR "(1: Gráfico de Barras / 2: Gráfico de torta / 3: Grafico barras horizonales):"
    LEER opcion
    SI opcion = 1 ENTONCES RETORNAR "Barras"
    SI opcion = 2 ENTONCES RETORNAR "Torta"
	SI opcion = 2 ENTONCES RETORNAR "Barras horizontales"
    RETORNAR "Ninguno"
FIN Funcion

// NOTA: Validar_Evento_Finalizado ahora está en Funciones_Comunes.md

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

// NOTA: Las siguientes funciones ahora están en Funciones_Comunes.md:
// - Usuario_Confirma_Operacion(mensaje)
// - Mostrar_Error(mensaje)
// - Mostrar_Exito(mensaje)
// - Mostrar_Mensaje(mensaje)
