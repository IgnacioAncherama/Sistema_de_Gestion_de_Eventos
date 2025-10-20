# Algoritmo de Sistemas de Gestion de Eventos
## 5. Módulo de Generación de Informes y Estadísticas
---
## Algoritmo

1.  Mostrar el menú principal de informes.
2.  Solicitar al usuario que elija una opción.
3.  Leer la entrada o entradas del usuario
4.  Procesar datos y generar el informe correspondiente.
5.  Mostrar el informe en pantalla , y ofrecer la opción de exportarlo.
6.  Volver al menú principal 

### Nivel de Refinamiento 1

		1.  Mostrar menú principal con los tipos de informes disponibles.
		2.  Leer y validar la opción seleccionada por el usuario.
		3.  Ejecutar la funcionalidad correspondiente según la opción:
			3.1. Generar Informe de Asistencia:Calcular y mostrar la comparativa entre registrados y asistentes.
			3.2. Generar Informe Demográfico:Procesar y visualizar la distribución de los asistentes
			3.3. Generar Informe de Interés:Analizar la participación en las distintas actividades del evento
			3.4. Generar Informe de Fidelización:Identificar y cuantificar asistentes recurrentes
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
		 2.2. Verificar la validez del evento llamando a Validar_Evento_Finalizado(id_evento) y  a a Existe_Evento(id_evento)
		 2.3. Si no es válido:
		     2.3.1. Terminar subproceso.
		 2.4. Si es válido:
		     2.4.1. Se llama a Obtener_Datos_Asistencia(id_evento) y se guarda el resultado en datos_asistencia.Los registrados, los 						asistentes y la tasa
			 2.4.2. Se muestran los datos en pantalla usando Mostrar_Datos_Asistencia(datos_asistencia) 
		     2.4.3. Consultar tipo de grafico llamando al modulo Obtener_Tipo_Grafico() y guardar la entrada en tipo_grafico
			 2.4.4  Generar_Grafico_Asistencia(datos_asistencia, tipo_grafico) y se guarda en grafico.
		     2.4.5. Se muestra el gráfico con Mostrar_Grafico(grafico).
		     2.4.6. Se empaquetan los datos llamando a Empaquetar_datos_y_grafico(datos_asistencia, grafico) y se guarda en  
			 		informe_completo.
			 2.4.6. Se llama a Exportar_Informe(informe_completo, "Asistencia_Evento_" + id_evento) para que el usuario decida si lo	
					guarda.
#### **3. GENERAR INFORME DEMOGRÁFICO**
```
	3.1. Llamar a la función Solicitar_ID_Evento() y guardar la entrada en la variable id_evento
	3.2. Verificar la validez del evento llamando a Validar_Evento_Finalizado(id_evento) y a a Existe_Evento(id_evento)
	3.3. Si no es válido:
	    3.3.1. Terminar subproceso.
	3.4. Si es válido:
	    3.4.1. Se llama a Obtener_Lista_Asistentes_Checkin(id_evento) y se guarda el resultado en lista_asistentes.
	    3.4.2. Se verifica si la longitud de lista_asistentes es 0.
	    3.4.3. Si es 0:
	        3.4.3.1. Se llama a Mostrar_Advertencia("No hubo asistentes para generar datos demográficos.")
	        3.4.3.2. Terminar subproceso.
	    3.4.4. Si es mayor a 0:
	        3.4.4.1. Se llama a Obtener_Datos_Demograficos(lista_asistentes) y se guarda en datos_demograficos.
	        3.4.4.2. Se muestran los datos en pantalla usando Mostrar_Datos_Demograficos(datos_demograficos).
	        3.4.4.3. Consultar tipo de grafico llamando al modulo Obtener_Tipo_Grafico() y guardar la entrada en tipo_grafico.
	        3.4.4.4. Se generan los gráficos llamando a Generar_Graficos_Demograficos(datos_demograficos, tipo_grafico) y se guarda en graficos.
	        3.4.4.5. Se muestran los gráficos con Mostrar_Graficos(graficos).
	        3.4.4.6. Se empaquetan los datos llamando a Empaquetar_Datos_y_Grafico(datos_demograficos, graficos) y se guarda en informe_completo.
	        3.4.4.7. Se llama a Exportar_Informe(informe_completo, "Demografico_Evento_" + id_evento) para que el usuario decida si lo guarda.
```
#### **4.GENERAR INFORME DE INTERÉS POR ACTIVIDAD**
		
```
	4.1. Llamar a la función Solicitar_ID_Evento() y guardar la entrada en la variable id_evento
	4.2. Verificar la validez del evento llamando a Validar_Evento_Finalizado(id_evento) y a a Existe_Evento(id_evento)
	4.3. Si no es válido:
	    4.3.1. Terminar subproceso.
	4.4. Si es válido:
	    4.4.1. Se llama a Obtener_Datos_Interes_Actividades(id_evento) y se guarda el resultado en datos_interes.
	    4.4.2. Se verifica si la longitud de datos_interes es 0.
	    4.4.3. Si es 0:
	        4.4.3.1. Se llama a Mostrar_Advertencia("El evento no tuvo actividades registradas o check-ins.")
	        4.4.3.2. Terminar subproceso.
	    4.4.4. Si es mayor a 0:
	        4.4.4.1. Se muestran los datos en pantalla usando Mostrar_Ranking_Actividades(datos_interes).
	        4.4.4.2. Consultar tipo de grafico llamando al modulo Obtener_Tipo_Grafico() y guardar la entrada en tipo_grafico.
	        4.4.4.3. Se genera el gráfico llamando a Generar_Grafico_Ranking(datos_interes, tipo_grafico) y se guarda en grafico.
	        4.4.4.4. Se muestra el gráfico con Mostrar_Grafico(grafico).
	        4.4.4.5. Se empaquetan los datos llamando a Empaquetar_Datos_y_Grafico(datos_interes, grafico) y se guarda en informe_completo.
	        4.4.4.6. Se llama a Exportar_Informe(informe_completo, "Interes_Actividades_" + id_evento) para que el usuario decida si lo guarda.
```
#### **5.GENERAR INFORME DE fIDELIZACIÓN POR TIPO DE EVENTO**

```	   5.1. Llamar a la función Solicitar_ID_Evento() y guardar la entrada en la variable id_evento
       5.2. Verificar la validez del evento llamando a Validar_Evento_Finalizado(id_evento) y a Existe_Evento(id_evento)
       5.3. Si no es válido:
              Terminar subproceso.
	   5.3 Permitir ingresar al usuario el tipo de evento y guardar en tipo_evento
       5.3 Si tipo_evento es igual a "Global", asignar "global" a la variable alcance_informe.
       5.4 Si no es "Global", asignar "para tipo de evento: " concatenado con tipo_evento a la variable alcance_informe.
       5.5 Si tipo_evento no es igual a "Global":
            5.5.1 Llamar a Validar_Tipo_Evento(tipo_evento) y guardar el resultado en tipo_valido.
            5.5.2 Si tipo_valido es FALSO:
					 Terminar subproceso (RETORNAR).
       5.6 Se llama a OBTENER_DATOS_FIDELIZACION(tipo_evento) y se guarda el resultado en datos_fidelizacion.
       5.7 Se verifica si el campo unicos de datos_fidelizacion es igual a 0.
       5.8 Si es 0:
            Se llama a Mostrar_Advertencia("No hay suficientes datos históricos para calcular la fidelización en el ámbito " +
					alcance_informe + ".")
            Terminar subproceso (RETORNAR).
       5.9 Se muestran los datos en pantalla usando Mostrar_Datos_Fidelizacion(datos_fidelizacion).
       5.10 Se exporta el informe llamando a Exportar_Informe(datos_fidelizacion, "Fidelizacion_" + tipo_evento).

```
#### **5. GENERAR INFORME FINANCIERO**
```
	6.1 Llamar a la función Solicitar_ID_Evento() y guardar el resultado en la variable id_evento.
    6.2 Llamar a Validar_Evento_Finalizado(id_evento) y a Existe_Evento(id_evento)
    6.3 Si el resultado es FALSO:
        6.3.1 Terminar subproceso (RETORNAR).
    6.4 Se llama a OBTENER_DATOS_FINANCIEROS(id_evento) y se guarda el resultado en datos_financieros.
    6.5 Se verifica si el campo total de datos_financieros es igual a 0.
    6.6 Si es 0:
        6.6.1 Llamar a Mostrar_Advertencia("No se registraron ingresos para este evento.")
        6.6.2 Terminar subproceso (RETORNAR).
    6.7 Se muestran los datos en pantalla usando Mostrar_Datos_Financieros(datos_financieros).
    6.8 Consultar tipo de grafico llamando a Obtener_Tipo_Grafico() y guardar la entrada en tipo_grafico.
    6.9 Se genera el gráfico llamando a GENERAR_GRAFICO_INGRESOS(datos_financieros, tipo_grafico) y se guarda en grafico.
    6.10 Se muestra el gráfico con Mostrar_Grafico(grafico).
    6.11 Se empaquetan los datos llamando a EMPAQUETAR_DATOS_Y_GRAFICO(datos_financieros, grafico) y se guarda en informe_completo.
    6.12 Se llama a Exportar_Informe(informe_completo, "Financiero_Evento_" + id_evento) para que el usuario decida si lo guarda.
```	
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
```
```python
// --- Procesos de Generación de informes---

Funcion Generar_Informe_Asistencia()
INICIO
    id_evento <- Solicitar_ID_Evento()
    SI NOT Validar_Evento_Finalizado(id_evento) ENTONCES 
        RETORNAR // El mensaje de error ya lo muestra la función de validación
    FIN SI

    datos_asistencia <- OBTENER_DATOS_ASISTENCIA(id_evento) // {registrados, asistentes, tasa}
    Mostrar_Datos_Asistencia(datos_asistencia)
	
    tipo_grafico <- Obtener_Tipo_Grafico() 
    grafico <- GENERAR_GRAFICO_ASISTENCIA(datos_asistencia, tipo_grafico)
    Mostrar_Grafico(grafico)
    
    informe_completo <- EMPAQUETAR_DATOS_Y_GRAFICO(datos_asistencia, grafico)
    Exportar_Informe(informe_completo, "Asistencia_Evento_" + id_evento)
FIN Funcion

// --- 3. Informe Demográfico ---
Funcion Generar_Informe_Demografico()
INICIO
    id_evento <- Solicitar_ID_Evento()
    SI NOT Validar_Evento_Finalizado(id_evento) ENTONCES 
        RETORNAR
    FIN SI

    // Obtiene la lista de asistentes que hicieron check-in
    lista_asistentes <- OBTENER_LISTA_ASISTENTES_CHECKIN(id_evento)
    
    SI lista_asistentes.longitud = 0 ENTONCES
        Mostrar_Advertencia("No hubo asistentes para generar datos demográficos.")
        RETORNAR
    FIN SI

    // Procesa los datos y calcula porcentajes
    datos_demograficos <- OBTENER_DATOS_DEMOGRAFICOS(lista_asistentes) // {genero: {...}, edad: {...}, ...}
    Mostrar_Datos_Demograficos(datos_demograficos)
    
	tipo_grafico <- Obtener_Tipo_Grafico() 
    graficos <- GENERAR_GRAFICOS_DEMOGRAFICOS(datos_demograficos, tipo_grafico)
    Mostrar_Graficos(graficos) // Muestra múltiples gráficos

    informe_completo <- EMPAQUETAR_DATOS_Y_GRAFICO(datos_demograficos, graficos)
    Exportar_Informe(informe_completo, "Demografico_Evento_" + id_evento)
FIN Funcion

// --- 4. Informe de Interés por Actividad ---
Funcion Generar_Informe_Interes()
INICIO
    id_evento <- Solicitar_ID_Evento()
    SI NOT Validar_Evento_Finalizado(id_evento) ENTONCES 
        RETORNAR
    FIN SI

    // Obtiene ranking de actividades {nombre_actividad, num_asistentes}
    datos_interes <- OBTENER_DATOS_INTERES_ACTIVIDADES(id_evento) 
    
    SI datos_interes.longitud = 0 ENTONCES
        Mostrar_Advertencia("El evento no tuvo actividades registradas o check-ins.")
        RETORNAR
    FIN SI
    
    Mostrar_Ranking_Actividades(datos_interes)
    
	tipo_grafico <- Obtener_Tipo_Grafico("horizontal") // Sugiere horizontal por defecto
    grafico <- GENERAR_GRAFICO_RANKING(datos_interes, tipo_grafico)
    Mostrar_Grafico(grafico)
    
    informe_completo <- EMPAQUETAR_DATOS_Y_GRAFICO(datos_interes, grafico)
    Exportar_Informe(informe_completo, "Interes_Actividades_" + id_evento)
FIN Funcion

Funcion Generar_Informe_Fidelizacion(tipo_evento: cadena = "Global")
INICIO
    // Determina el alcance del informe para el mensaje y el nombre del archivo
    alcance_informe <- SI tipo_evento = "Global" ENTONCES "global" SINO "para tipo de evento: " + tipo_evento FIN SI
    Mostrar_Mensaje("Generando informe de fidelización " + alcance_informe + "...")
    
    // Pasa el tipo de evento a la función OBTENER_DATOS_FIDELIZACION
    datos_fidelizacion <- OBTENER_DATOS_FIDELIZACION(tipo_evento)
    
    SI datos_fidelizacion.unicos = 0 ENTONCES
        Mostrar_Advertencia("No hay suficientes datos históricos para calcular la fidelización en el ámbito " + alcance_informe + ".")
        RETORNAR
    FIN SI
    
    Mostrar_Datos_Fidelizacion(datos_fidelizacion)
    
    Exportar_Informe(datos_fidelizacion, "Fidelizacion_" + tipo_evento)
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


```
```python
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
```

```python
// --- Funciones consultas   base de datos---

Funcion OBTENER_DATOS_ASISTENCIA(id_evento) : registro
INICIO
    total_registrados <- CONSULTA_BD("CONTAR inscripciones DONDE id_evento = " + id_evento + " Y estado = 'Confirmada'")
    total_asistentes <- CONSULTA_BD("CONTAR inscripciones DONDE id_evento = " + id_evento + " AND check_in = VERDADERO")
    
    tasa_asistencia <- 0
    SI total_registrados > 0 ENTONCES
        tasa_asistencia <- (total_asistentes / total_registrados) * 100
    FIN SI
    
    RETORNAR {registrados: total_registrados, asistentes: total_asistentes, tasa: tasa_asistencia}
FIN Funcion

Funcion OBTENER_LISTA_ASISTENTES_CHECKIN(id_evento) : lista
INICIO
    lista_ids_participantes <- CONSULTA_BD("SELECCIONAR id_participante DONDE id_evento = " + id_evento + " AND check_in = VERDADERO")
    lista_completa <- []
    PARA CADA id_participante EN lista_ids_participantes HACER
        info_participante <- Obtener_Info_Participante(id_participante) // Función común
        AGREGAR info_participante A lista_completa
    FIN PARA
    RETORNAR lista_completa
FIN Funcion

Funcion OBTENER_DATOS_DEMOGRAFICOS(lista_asistentes) : registro
INICIO
    total <- lista_asistentes.longitud
    datos_finales <- {}
    categorias <- ["género", "país", "profesión", "rango_edad"]
    
     PARA CADA categoria EN categorias HACER
        conteo_categoria <- AGRUPAR_Y_CONTAR(lista_asistentes, categoria) // Ej: {Masculino: 50, Femenino: 30}
        datos_porcentaje <- {}
        PARA CADA sub_atributo, valor EN conteo_categoria HACER
            porcentaje <- (valor / total) * 100
            datos_porcentaje[sub_atributo] <- {conteo: valor, porcentaje: porcentaje}
        FIN PARA
        datos_finales[categoria] <- datos_porcentaje
    FIN PARA
    
    RETORNAR datos_finales // {genero: {Masculino: {conteo: 50, porc: 62.5}}, ...}
FIN Funcion

Funcion OBTENER_DATOS_INTERES_ACTIVIDADES(id_evento) : lista
INICIO
    lista_actividades <- CONSULTA_BD("SELECCIONAR id, nombre FROM actividades DONDE id_evento = " + id_evento)
    ranking <- []
    
    PARA CADA actividad EN lista_actividades HACER
        num_asistentes <- CONSULTA_BD("CONTAR check_ins_actividad DONDE id_actividad = " + actividad.id)
        AGREGAR {nombre: actividad.nombre, asistentes: num_asistentes} A ranking
    FIN PARA
    
    ORDENAR_LISTA(ranking, "asistentes", "DESC")
    
    RETORNAR ranking
FIN Funcion

Funcion OBTENER_DATOS_FIDELIZACION(tipo_evento: cadena) : registro
INICIO
      ambito <- SI tipo_evento <> "Global" ENTONCES 
                  "Por_Tipo_Evento_" + tipo_evento 
              SINO 
                  "Global" 
              FIN SI
    total_unicos <- CONSULTA_BD("CONTAR_PARTICIPANTES_UNICOS", ambito)
    lista_recurrentes <- CONSULTA_BD("SELECCIONAR_PARTICIPANTES_RECURRENTES", ambito)
    total_recurrentes <- lista_recurrentes.longitud
    
    tasa_retorno <- 0
    SI total_unicos > 0 ENTONCES
        tasa_retorno <- (total_recurrentes / total_unicos) * 100
    FIN SI
    
    RETORNAR {unicos: total_unicos, recurrentes: total_recurrentes, tasa: tasa_retorno}
FIN Funcion

Funcion OBTENER_DATOS_FINANCIEROS(id_evento) : registro
INICIO
    // Obtiene todos los pagos (entradas, sponsor, etc.)
    lista_pagos <- CONSULTA_BD("SELECCIONAR concepto, monto FROM pagos DONDE id_evento = " + id_evento)
    
    desglose <- {}
    total_general <- 0
    PARA CADA pago EN lista_pagos HACER
        SI NOT desglose.contiene(pago.concepto) ENTONCES
            desglose[pago.concepto] <- 0
        FIN SI
        desglose[pago.concepto] <- desglose[pago.concepto] + pago.monto
        total_general <- total_general + pago.monto
    FIN PARA
    
    RETORNAR {desglose: desglose, total: total_general} // {desglose: {Entradas: 5000, Sponsor: 2000}, total: 7000}
FIN Funcion

```

```python
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

```
