# Algoritmo de Sistemas de Gestion de Eventos

## Nivel de Refinamiento 1

    1. Permitir al usuario seleccionar una opción de informe
    2. Recopilar los datos del evento necesarios para generar el informe
    3. Procesar los datos
    4. Generar reporte
    5. Implementar la exportación de cada reporte

## Nivel de Refinamiento 2

	- 1.1 Mostrar una lista de opciones de informes disponibles:
		 Asistencia vs. Registro
		 Distribución demográfica
		 Interés por tipo de contenido
		 Tasa de Repetición
		 Ingresos
	 1.2 Capturar la selección del usuario.
	 1.3 Validar la selección para asegurar que sea una opción válida.


	2.1 Identificar el tipo de informe seleccionado por el usuario.
	2.2 En función del tipo de informe, determinar qué conjuntos de datos del evento se necesitan:
		  Para Asistencia vs. Registro: Obtener datos de registro de asistentes y datos de check-in.
		  Para Distribución demográfica: Obtener datos de perfiles de asistentes (edad, género, profesión, país).
		  Para Interés por tipo de contenido: Obtener datos de registro a sesiones/actividades y/o datos de check-in a estas.
		  Para Tasa de Repetición: Obtener el historial de participación de los asistentes en eventos anteriores.
		  Para Estadística Financiera: Obtener datos de transacciones de pago, desglosados por tipo de producto/servicio (entradas, patrocinios, etc.).
	 2.3 Consultar la base de datos para extraer los datos necesarios.

	 3.1 Realizar cálculos y agrupaciones según el tipo de informe:
		 Asistencia vs. Registro: Calcular el total de registrados y el total de asistentes. Determinar el porcentaje de asistencia.
		 Distribución Demográfica: Agrupar asistentes por categoría (ej. por país, por rango de edad), contar el número de asistentes en cada grupo y calcular el porcentaje que representa cada grupo del total.
		 Interés por tipo de contenido: Contar el número de participantes por sesión o actividad y calcular las tasas de participación.
		 Tasa de Repetición: Identificar y contar a los asistentes que han participado en ediciones anteriores del evento. Calcular la tasa de retención o fidelización.
		 Estadísticas Financieras: Sumar los ingresos por cada categoría y calcular el porcentaje que cada una representa del total de ingresos. 
    3.2 Formatear los datos procesados para su visualización.


  	4.1 Seleccionar el tipo de visualización adecuado para cada informe (gráfico de barras para ingresos, gráfico circular para distribución demográfica, etc.).
	  4.2 Utilizar una biblioteca de gráficos para generar las visualizaciones a partir de los datos procesados.
  
    5.1 Proporcionar la opción de exportación para cada formato al usuario (ej. PDF, CSV).
	  5.2 Para CSV: Convertir los datos del informe en un formato de texto separado por comas y permitir la descarga del archivo.
	  5.3 Para PDF Utilizar una biblioteca de generación de PDF para capturar la visualización del informe y generar un documento PDF descargable.

## Pseudocódigo

### Programa principal

```python
INICIO PROGRAMA
    mostrar_menu_informes()
    seleccion_usuario = leer_opcion_usuario()
    
    SI seleccion_es_valida(seleccion_usuario)
        datos_recopilados = recopilar_datos_evento(seleccion_usuario)
        datos_procesados = procesar_datos_informe(datos_recopilados, seleccion_usuario)
        generar_reporte_visual(datos_procesados, seleccion_usuario)
        mostrar_opciones_exportacion()
        opcion_exportacion = leer_opcion_exportacion()
        exportar_informe(datos_procesados, opcion_exportacion)
    SINO
        mostrar_error("Opción no válida. Por favor, intente de nuevo.")
    FIN SI
FIN PROGRAMA
```

### Funciones

#### 1. recopilar_datos_evento

```python
funcion recopilar_datos_evento(tipo_informe)
    datos = []
    SI tipo_informe es "Asistencia vs. Registro"
        consulta_sql = "SELECT count(*) FROM TablaRegistros"
        num_registrados = ejecutar_consulta(consulta_sql)
        consulta_sql = "SELECT count(*) FROM TablaCheckIns"
        num_asistentes = ejecutar_consulta(consulta_sql)
        datos.añadir({"registrados": num_registrados, "asistentes": num_asistentes})
        
    SINO SI tipo_informe es "Distribución Demográfica"
        consulta_sql = "SELECT genero, count(*) AS total FROM TablaAsistentes GROUP BY genero"
        resultado = ejecutar_consulta(consulta_sql)
        datos.añadir(resultado)
        
    SINO SI tipo_informe es "Interés por Contenido"
        consulta_sql = "SELECT actividad, count(*) AS total FROM TablaAsistenciaActividades GROUP BY actividad"
        resultado = ejecutar_consulta(consulta_sql)
        datos.añadir(resultado)
        
    SINO SI tipo_informe es "Tasa de Repetición"
        consulta_sql = "SELECT asistente_id FROM HistorialAsistencias WHERE evento_id = ID_EVENTO_ACTUAL"
        asistentes_actuales = ejecutar_consulta(consulta_sql)
        consulta_sql = "SELECT asistente_id FROM HistorialAsistencias WHERE evento_id != ID_EVENTO_ACTUAL"
        asistentes_anteriores = ejecutar_consulta(consulta_sql)
        datos.añadir({"actuales": asistentes_actuales, "anteriores": asistentes_anteriores})
        
    SINO SI tipo_informe es "Estadísticas Financieras"
        consulta_sql = "SELECT tipo_pago, SUM(monto) AS total FROM TablaPagos GROUP BY tipo_pago"
        resultado = ejecutar_consulta(consulta_sql)
        datos.añadir(resultado)
    FIN SI
    
    RETORNAR datos
FIN FUNCION
```

#### 2. procesar_datos_informe

```python
funcion procesar_datos_informe(datos, tipo_informe)
    datos_procesados = {}
    SI tipo_informe es "Asistencia vs. Registro"
        total_registrados = datos[0]["registrados"]
        total_asistentes = datos[0]["asistentes"]
        tasa_asistencia = (total_asistentes / total_registrados) * 100
        datos_procesados.añadir({"tasa_asistencia": tasa_asistencia, "totales": [total_registrados, total_asistentes]})

    SINO SI tipo_informe es "Distribución Demográfica"
        total_asistentes = 0
        PARA CADA item EN datos[0]
            total_asistentes = total_asistentes + item.total
        FIN PARA

        PARA CADA item EN datos[0]
            porcentaje = (item.total / total_asistentes) * 100
            datos_procesados.añadir({item.categoria: porcentaje})
        FIN PARA
        
    SINO SI tipo_informe es "Interés por Contenido"
        total_participantes = 0
        PARA CADA item EN datos[0]
            total_participantes = total_participantes + item.total
        FIN PARA
        
        datos_procesados.añadir({"total_participantes": total_participantes})

        PARA CADA item EN datos[0]
            porcentaje = (item.total / total_participantes) * 100
            datos_procesados.añadir({item.actividad: {"total": item.total, "porcentaje": porcentaje}})
        FIN PARA

    SINO SI tipo_informe es "Tasa de Repetición"
        asistentes_actuales = datos[0]["actuales"]
        asistentes_anteriores = datos[0]["anteriores"]
        num_asistentes_leales = 0
        
        PARA CADA asistente_id_actual EN asistentes_actuales
            SI asistente_id_actual esta EN asistentes_anteriores
                num_asistentes_leales = num_asistentes_leales + 1
            FIN SI
        FIN PARA
        
        tasa_repeticion = (num_asistentes_leales / asistentes_actuales.longitud) * 100
        datos_procesados.añadir({"tasa_repeticion": tasa_repeticion, "leales": num_asistentes_leales, "total_actual": asistentes_actuales.longitud})

    SINO SI tipo_informe es "Estadísticas Financieras"
        ingresos_totales = 0
        PARA CADA item EN datos[0]
            ingresos_totales = ingresos_totales + item.total
        FIN PARA
        datos_procesados.añadir({"ingresos_totales": ingresos_totales})
        
        PARA CADA item EN datos[0]
            porcentaje = (item.total / ingresos_totales) * 100
            datos_procesados.añadir({item.tipo_pago: {"total": item.total, "porcentaje": porcentaje}})
        FIN PARA
        
    FIN SI
    RETORNAR datos_procesados
FIN FUNCION
```

#### 3. generar_reporte_visual

```python
funcion generar_reporte_visual(datos_procesados, tipo_informe)
    limpiar_contenedor("id_contenedor_reporte")
    crear_titulo("Informe de " + tipo_informe)
    
    SI tipo_informe es "Asistencia vs. Registro"
        etiquetas_barras = ["Registrados", "Asistentes"]
        valores_barras = datos_procesados.totales
        generar_grafico_barras(etiquetas_barras, valores_barras, "id_contenedor_grafico")
        crear_tabla_de_datos({"Concepto": etiquetas_barras, "Total": valores_barras})
        
    SINO SI tipo_informe es "Distribución Demográfica"
        etiquetas_pie = obtener_claves(datos_procesados)
        valores_pie = obtener_valores(datos_procesados)
        generar_grafico_torta(etiquetas_pie, valores_pie, "id_contenedor_grafico")
        crear_tabla_de_datos({"Categoría": etiquetas_pie, "Porcentaje": valores_pie})
        
    SINO SI tipo_informe es "Interés por Contenido"
        etiquetas_barras = obtener_claves(datos_procesados)
        valores_barras = obtener_valores(datos_procesados, "total")
        generar_grafico_barras(etiquetas_barras, valores_barras, "id_contenedor_grafico")
        
        tabla_datos = []
        PARA CADA actividad EN etiquetas_barras
            total = datos_procesados[actividad]["total"]
            porcentaje = datos_procesados[actividad]["porcentaje"]
            tabla_datos.añadir({"Actividad": actividad, "Asistentes": total, "Porcentaje": porcentaje})
        FIN PARA
        crear_tabla_de_datos(tabla_datos)
        
    SINO SI tipo_informe es "Tasa de Repetición"
        leales = datos_procesados.leales
        nuevos = datos_procesados.total_actual - leales
        etiquetas = ["Asistentes Leales", "Nuevos Asistentes"]
        valores = [leales, nuevos]
        generar_grafico_torta(etiquetas, valores, "id_contenedor_grafico")
        crear_tabla_de_datos({"Concepto": etiquetas, "Total": valores})

    SINO SI tipo_informe es "Estadísticas Financieras"
        etiquetas_barras = obtener_claves(datos_procesados)
        valores_barras = obtener_valores(datos_procesados, "total")
        generar_grafico_barras(etiquetas_barras, valores_barras, "id_contenedor_grafico")
        
        tabla_datos = []
        PARA CADA tipo_pago EN etiquetas_barras
            total = datos_procesados[tipo_pago]["total"]
            porcentaje = datos_procesados[tipo_pago]["porcentaje"]
            tabla_datos.añadir({"Tipo de Ingreso": tipo_pago, "Monto": total, "Porcentaje": porcentaje})
        FIN PARA
        crear_tabla_de_datos(tabla_datos)
    FIN SI
FIN FUNCION
```

#### 4. exportar_informe

```python
funcion exportar_informe(datos_procesados, formato)
    SI formato es "CSV"
        contenido_csv = convertir_a_csv(datos_procesados)
        descargar_archivo("informe.csv", contenido_csv)
        
    SINO SI formato es "PDF"
        imagen_reporte = capturar_vista_pantalla("id_contenedor_reporte")
        documento_pdf = crear_pdf()
        añadir_imagen_a_pdf(documento_pdf, imagen_reporte)
        guardar_pdf(documento_pdf, "informe.pdf")
        
    FIN SI
FIN FUNCION
```
