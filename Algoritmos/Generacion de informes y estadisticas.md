# Algoritmo de Sistemas de Gestion de Eventos
## 5. Módulo de Generación de Informes y Estadísticas
---
## Algoritmo

1.  Mostrar el menú principal de informes.
2.  Solicitar al usuario que elija una opción.
3.  Leer la entrada o entradas del usuario
4.  Procesar datos y generar el informe correspondiente.
5.  Mostrar el informe en pantalla
6.  Volver al menú principal 

### Nivel de Refinamiento 1

		1.  Mostrar menú principal con los tipos de informes disponibles.
		2.  Leer y validar la opción seleccionada por el usuario.
		3.  Ejecutar la funcionalidad correspondiente según la opción:
			3.1. Generar Informe de Asistencia: Calcular y mostrar la comparativa entre registrados y asistentes.
			3.2. Generar Informe Demográfico: Procesar y visualizar la distribución de los asistentes por género, país y edad.
			3.3. Generar Informe de Interés: Analizar la participación en las distintas actividades del evento.
			3.4. Generar Informe de Fidelización: Identificar y cuantificar asistentes recurrentes.
			3.5. Generar Informe Financiero: Desglosar y totalizar los ingresos.
		4.  Una vez generado un informe, mostrarlo en pantalla
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
		     2.4.1. Se llama a Obtener_Datos_Asistencia(id_evento) y se guarda el resultado en datos_asistencia.
			 2.4.2. Se muestran los datos en pantalla usando Mostrar_Datos_Asistencia(datos_asistencia).
		     2.4.3. Terminar subproceso.
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
	        3.4.4.1. Se llama a Analizar_Distribucion_Genero(lista_asistentes) y se muestra en pantalla.
	        3.4.4.2. Se llama a Analizar_Distribucion_Pais(lista_asistentes) y se muestra en pantalla.
	        3.4.4.3. Se llama a Analizar_Distribucion_Edad(lista_asistentes) y se muestra en pantalla.
	        3.4.4.4. Terminar subproceso.
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
	        4.4.4.2. Terminar subproceso.
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

```	


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
	
FIN Funcion

// --- 3. Informe Demográfico ---
Funcion Generar_Informe_Demografico()
INICIO
    id_evento <- Solicitar_ID_Evento()
    SI NOT Validar_Evento_Finalizado(id_evento) ENTONCES 
        RETORNAR
    FIN SI

    lista_asistentes <- OBTENER_LISTA_ASISTENTES_CHECKIN(id_evento)
    
    SI lista_asistentes.longitud = 0 ENTONCES
        Mostrar_Advertencia("No hubo asistentes para generar datos demográficos.")
        RETORNAR
    FIN SI

    datos_demograficos <- OBTENER_DATOS_DEMOGRAFICOS(lista_asistentes) // {genero: {...}, edad: {...}, ...}
    Mostrar_Datos_Demograficos(datos_demograficos)
    

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
    
FIN Funcion

Funcion Generar_Informe_Fidelizacion(tipo_evento: cadena = "Global")
INICIO
    alcance_informe <- SI tipo_evento = "Global" ENTONCES "global" SINO "para tipo de evento: " + tipo_evento FIN SI
    Mostrar_Mensaje("Generando informe de fidelización " + alcance_informe + "...")
    
    datos_fidelizacion <- OBTENER_DATOS_FIDELIZACION(tipo_evento)
    
    SI datos_fidelizacion.unicos = 0 ENTONCES
        Mostrar_Advertencia("No hay suficientes datos históricos para calcular la fidelización en el ámbito " + alcance_informe + ".")
        RETORNAR
    FIN SI
    
    Mostrar_Datos_Fidelizacion(datos_fidelizacion)
    
FIN Funcion


Funcion Generar_Informe_Financiero()
// Utiliza: Validar_Evento_Finalizado
INICIO
    id_evento <- Solicitar_Evento()
    SI NOT Validar_Evento_Finalizado(id_evento) ENTONCES RETORNAR

    datos_financieros <- OBTENER_DATOS_FINANCIEROS(id_evento) // Retorna desglose y total de ingresos
	tipo_grafico <- Obtener_Tipo_Grafico() 
    Mostrar_Datos_Financieros(datos_financieros)
  
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


## Notas

1. **Convención de Nombres**: Todas las funciones comunes usan PascalCase con guiones bajos.
2. **Manejo de Errores**: Las funciones de validación ya incluyen los mensajes de error, por lo que no es necesario repetirlos en los módulos que las llaman.
3. **Retornos Consistentes**: 
   - Funciones de validación retornan booleano
   - Funciones de obtención retornan el tipo de dato correspondiente o 0/NULO si no existe
4. **Abstracción de BD**: Las funciones que acceden a la base de datos están en MAYÚSCULAS para indicar que son operaciones de bajo nivel.

---


## Ventajas de Este Módulo

**Reutilización**: Código escrito una vez, usado en múltiples lugares  
**Mantenimiento**: Un solo lugar para actualizar la lógica  
**Consistencia**: Mismo comportamiento en todos los módulos  
**Legibilidad**: Nombres descriptivos y claros  
**Facilita Testing**: Funciones independientes más fáciles de probar

