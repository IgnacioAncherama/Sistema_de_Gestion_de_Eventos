"""
Módulo de Generación de Informes y Estadísticas
Sistema de Gestión de Eventos

Este módulo genera informes de asistencia, demográficos, de interés y financieros.
"""

from datetime import date, datetime
from collections import Counter
import funciones_comunes as fc


def menu_principal_informes():
    """Muestra el menú principal de informes y estadísticas."""
    while True:
        fc.limpiar_pantalla()
        print("=" * 60)
        print("           MENÚ DE INFORMES Y ESTADÍSTICAS")
        print("=" * 60)
        print("A. Informe de Asistencia")
        print("D. Informe Demográfico")
        print("I. Informe de Interés por Evento")
        print("F. Informe de Fidelización")
        print("N. Informe Financiero")
        print("S. Salir del módulo")
        print("=" * 60)
        
        opcion = input("\nSeleccione una opción: ").upper().strip()
        
        if opcion == 'A':
            generar_informe_asistencia()
        elif opcion == 'D':
            generar_informe_demografico()
        elif opcion == 'I':
            generar_informe_interes()
        elif opcion == 'F':
            generar_informe_fidelizacion()
        elif opcion == 'N':
            generar_informe_financiero()
        elif opcion == 'S':
            fc.mostrar_mensaje("Saliendo del módulo de informes...")
            break
        else:
            fc.mostrar_error("Opción no válida. Intente nuevamente.")
            fc.pausar()


def generar_informe_asistencia():
    """Genera un informe de asistencia de un evento."""
    fc.limpiar_pantalla()
    print("=" * 60)
    print("           INFORME DE ASISTENCIA")
    print("=" * 60)
    
    id_evento = solicitar_evento_finalizado()
    if not id_evento:
        fc.pausar()
        return
    
    if not fc.validar_evento_finalizado(id_evento):
        fc.pausar()
        return
    
    info_evento = fc.obtener_info_evento(id_evento)
    
    conn = fc.conectar_bd()
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT COUNT(*) as total FROM inscripciones 
        WHERE id_evento = ? AND estado = 'confirmada'
    ''', (id_evento,))
    total_registrados = cursor.fetchone()['total']
    
    cursor.execute('''
        SELECT COUNT(*) as total FROM asistencia a
        JOIN inscripciones i ON a.id_inscripcion = i.id
        WHERE i.id_evento = ?
    ''', (id_evento,))
    total_asistentes = cursor.fetchone()['total']
    
    conn.close()
    
    tasa_asistencia = 0
    if total_registrados > 0:
        tasa_asistencia = (total_asistentes * 100) / total_registrados
    
    print("\n" + "=" * 60)
    print("           INFORME DE ASISTENCIA")
    print("=" * 60)
    print(f"Evento: {info_evento['nombre']}")
    print(f"Fecha: {fc.formatear_fecha(info_evento['fecha'])}")
    print(f"Ubicación: {info_evento['ubicacion']}")
    print("\n--- ESTADÍSTICAS ---")
    print(f"Total Registrados: {total_registrados}")
    print(f"Total Asistentes: {total_asistentes}")
    print(f"Ausentes: {total_registrados - total_asistentes}")
    print(f"Tasa de Asistencia: {tasa_asistencia:.2f}%")
    
    if total_registrados > 0:
        print("\n--- GRÁFICO DE ASISTENCIA ---")
        barra_asistentes = "█" * int((total_asistentes / total_registrados) * 40)
        barra_ausentes = "░" * int(((total_registrados - total_asistentes) / total_registrados) * 40)
        print(f"Asistieron: {barra_asistentes} {total_asistentes}")
        print(f"Ausentes:   {barra_ausentes} {total_registrados - total_asistentes}")
    
    fc.pausar()


def generar_informe_demografico():
    """Genera un informe demográfico de los asistentes."""
    fc.limpiar_pantalla()
    print("=" * 60)
    print("           INFORME DEMOGRÁFICO")
    print("=" * 60)
    
    id_evento = solicitar_evento_finalizado()
    if not id_evento:
        fc.pausar()
        return
    
    if not fc.validar_evento_finalizado(id_evento):
        fc.pausar()
        return
    
    info_evento = fc.obtener_info_evento(id_evento)
    
    conn = fc.conectar_bd()
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT p.* FROM participantes p
        JOIN inscripciones i ON p.id = i.id_participante
        JOIN asistencia a ON i.id = a.id_inscripcion
        WHERE i.id_evento = ?
    ''', (id_evento,))
    asistentes = cursor.fetchall()
    conn.close()
    
    if not asistentes:
        fc.mostrar_mensaje("No hay asistentes registrados para este evento")
        fc.pausar()
        return
    
    print("\n" + "=" * 60)
    print("           INFORME DEMOGRÁFICO")
    print("=" * 60)
    print(f"Evento: {info_evento['nombre']}")
    print(f"Fecha: {fc.formatear_fecha(info_evento['fecha'])}")
    print(f"Total de asistentes: {len(asistentes)}")
    
    # Recolectar datos demográficos
    generos = []
    paises = []
    edades = []
    
    for registro in asistentes:
        # Género
        if registro['genero']:
            generos.append(registro['genero'])
        
        # País
        if registro['pais']:
            paises.append(registro['pais'])
        
        # Calcular edad
        if registro['fecha_nacimiento']:
            try:
                fecha_nac = datetime.strptime(registro['fecha_nacimiento'], '%Y-%m-%d').date()
                edad = (date.today() - fecha_nac).days // 365
                edades.append(edad)
            except:
                pass
    
    # Mostrar distribución por género
    if generos:
        print("\n--- DISTRIBUCIÓN POR GÉNERO ---")
        contador_generos = Counter(generos)
        for genero, cantidad in contador_generos.most_common():
            porcentaje = (cantidad * 100) / len(generos)
            barra = "█" * int(porcentaje / 2)
            print(f"{genero.capitalize():.<30} {barra} {cantidad} ({porcentaje:.1f}%)")
    
    # Mostrar distribución por país
    if paises:
        print("\n--- DISTRIBUCIÓN POR PAÍS ---")
        contador_paises = Counter(paises)
        for pais, cantidad in contador_paises.most_common(10):
            porcentaje = (cantidad * 100) / len(paises)
            barra = "█" * int(porcentaje / 2)
            print(f"{pais.capitalize():.<30} {barra} {cantidad} ({porcentaje:.1f}%)")
    
    # Mostrar distribución por rango de edad
    if edades:
        print("\n--- DISTRIBUCIÓN POR RANGO DE EDAD ---")
        # Calcular rangos de edad
        rangos = {
            '18-25': 0,
            '26-35': 0,
            '36-45': 0,
            '46-55': 0,
            '56+': 0
        }
        
        for edad in edades:
            if edad < 18:
                continue  # Menores no esperados
            elif edad <= 25:
                rangos['18-25'] += 1
            elif edad <= 35:
                rangos['26-35'] += 1
            elif edad <= 45:
                rangos['36-45'] += 1
            elif edad <= 55:
                rangos['46-55'] += 1
            else:
                rangos['56+'] += 1
        
        total_edades = sum(rangos.values())
        if total_edades > 0:
            for rango, cantidad in rangos.items():
                if cantidad > 0:
                    porcentaje = (cantidad * 100) / total_edades
                    barra = "█" * int(porcentaje / 2)
                    print(f"{rango:.<30} {barra} {cantidad} ({porcentaje:.1f}%)")
        
        # Mostrar estadísticas de edad
        if edades:
            edad_promedio = sum(edades) / len(edades)
            edad_minima = min(edades)
            edad_maxima = max(edades)
            print(f"\nEdad promedio: {edad_promedio:.1f} años")
            print(f"Edad mínima: {edad_minima} años")
            print(f"Edad máxima: {edad_maxima} años")
    
    fc.pausar()


def generar_informe_interes():
    """Genera un informe de interés por evento."""
    fc.limpiar_pantalla()
    print("=" * 60)
    print("           INFORME DE INTERÉS POR EVENTO")
    print("=" * 60)
    
    conn = fc.conectar_bd()
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT e.*, 
               (SELECT COUNT(*) FROM inscripciones WHERE id_evento = e.id) as inscripciones,
               (SELECT COUNT(*) FROM asistencia a 
                JOIN inscripciones i ON a.id_inscripcion = i.id 
                WHERE i.id_evento = e.id) as asistentes
        FROM eventos e
        ORDER BY inscripciones DESC
    ''')
    eventos = cursor.fetchall()
    conn.close()
    
    if not eventos:
        fc.mostrar_mensaje("No hay eventos registrados")
        fc.pausar()
        return
    
    print("\n" + "=" * 60)
    print("           RANKING DE EVENTOS POR INTERÉS")
    print("=" * 60)
    
    for i, evento in enumerate(eventos[:10], 1):
        evento = dict(evento)
        ocupacion = (evento['inscripciones'] * 100) / evento['capacidad_maxima'] if evento['capacidad_maxima'] > 0 else 0
        
        print(f"\n{i}. {evento['nombre']}")
        print(f"   Inscripciones: {evento['inscripciones']}")
        print(f"   Asistentes: {evento['asistentes']}")
        print(f"   Ocupación: {ocupacion:.1f}%")
        
        barra = "█" * int(ocupacion / 2.5)
        print(f"   {barra}")
    
    fc.pausar()


def generar_informe_fidelizacion():
    """Genera un informe de fidelización de participantes."""
    fc.limpiar_pantalla()
    print("=" * 60)
    print("           INFORME DE FIDELIZACIÓN")
    print("=" * 60)
    
    conn = fc.conectar_bd()
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT id_participante, COUNT(*) as cantidad
        FROM inscripciones
        GROUP BY id_participante
        ORDER BY cantidad DESC
    ''')
    participacion = cursor.fetchall()
    conn.close()
    
    if not participacion:
        fc.mostrar_mensaje("No hay inscripciones registradas")
        fc.pausar()
        return
    
    total_participantes_unicos = len(participacion)
    participantes_recurrentes = sum(1 for p in participacion if p['cantidad'] > 1)
    
    tasa_retorno = 0
    if total_participantes_unicos > 0:
        tasa_retorno = (participantes_recurrentes * 100) / total_participantes_unicos
    
    print("\n" + "=" * 60)
    print("           ANÁLISIS DE FIDELIZACIÓN")
    print("=" * 60)
    print(f"Total participantes únicos: {total_participantes_unicos}")
    print(f"Participantes recurrentes: {participantes_recurrentes}")
    print(f"Tasa de retorno: {tasa_retorno:.2f}%")
    
    print("\n--- TOP 10 PARTICIPANTES MÁS ACTIVOS ---")
    for i, registro in enumerate(participacion[:10], 1):
        participante = fc.obtener_info_participante(registro['id_participante'])
        if participante:
            print(f"{i}. {participante['nombre']} {participante['apellido']}: "
                  f"{registro['cantidad']} inscripciones")
    
    print("\n--- DISTRIBUCIÓN DE PARTICIPACIÓN ---")
    una_vez = sum(1 for p in participacion if p['cantidad'] == 1)
    dos_veces = sum(1 for p in participacion if p['cantidad'] == 2)
    tres_o_mas = sum(1 for p in participacion if p['cantidad'] >= 3)
    
    print(f"1 evento:     {una_vez} participantes")
    print(f"2 eventos:    {dos_veces} participantes")
    print(f"3+ eventos:   {tres_o_mas} participantes")
    
    fc.pausar()


def generar_informe_financiero():
    """Genera un informe financiero."""
    fc.limpiar_pantalla()
    print("=" * 60)
    print("           INFORME FINANCIERO")
    print("=" * 60)
    print("E. Por evento específico")
    print("G. General del sistema")
    
    opcion = input("\nSeleccione una opción: ").upper().strip()
    
    if opcion == 'E':
        informe_financiero_evento()
    elif opcion == 'G':
        informe_financiero_general()
    else:
        fc.mostrar_error("Opción no válida")
        fc.pausar()


def informe_financiero_evento():
    """Genera informe financiero de un evento específico."""
    id_evento = solicitar_evento_finalizado()
    if not id_evento:
        fc.pausar()
        return
    
    if not fc.validar_evento_finalizado(id_evento):
        fc.pausar()
        return
    
    info_evento = fc.obtener_info_evento(id_evento)
    
    conn = fc.conectar_bd()
    cursor = conn.cursor()
    
    cursor.execute('SELECT COUNT(*) as total FROM inscripciones WHERE id_evento = ?', (id_evento,))
    total_inscripciones = cursor.fetchone()['total']
    
    cursor.execute('''
        SELECT COUNT(*) as total FROM inscripciones 
        WHERE id_evento = ? AND estado_pago = 'pagado'
    ''', (id_evento,))
    pagos_completados = cursor.fetchone()['total']
    
    cursor.execute('''
        SELECT COUNT(*) as total FROM inscripciones 
        WHERE id_evento = ? AND estado_pago = 'pendiente'
    ''', (id_evento,))
    pagos_pendientes = cursor.fetchone()['total']
    
    cursor.execute('''
        SELECT COALESCE(SUM(p.monto), 0) as total FROM pagos p
        JOIN inscripciones i ON p.id_inscripcion = i.id
        WHERE i.id_evento = ?
    ''', (id_evento,))
    ingresos_reales = cursor.fetchone()['total']
    
    cursor.execute('''
        SELECT COALESCE(SUM(r.monto), 0) as total FROM reembolsos r
        JOIN inscripciones i ON r.id_inscripcion = i.id
        WHERE i.id_evento = ?
    ''', (id_evento,))
    total_reembolsos = cursor.fetchone()['total']
    
    conn.close()
    
    ingresos_potenciales = total_inscripciones * info_evento['precio']
    ingresos_pendientes = pagos_pendientes * info_evento['precio']
    ingresos_netos = ingresos_reales - total_reembolsos
    
    print("\n" + "=" * 60)
    print("           INFORME FINANCIERO DEL EVENTO")
    print("=" * 60)
    print(f"Evento: {info_evento['nombre']}")
    print(f"Fecha: {fc.formatear_fecha(info_evento['fecha'])}")
    print(f"Precio: {fc.formatear_precio(info_evento['precio'])}")
    
    print("\n--- INSCRIPCIONES ---")
    print(f"Total: {total_inscripciones}")
    print(f"Pagos completados: {pagos_completados}")
    print(f"Pagos pendientes: {pagos_pendientes}")
    
    print("\n--- INGRESOS ---")
    print(f"Ingresos reales: {fc.formatear_precio(ingresos_reales)}")
    print(f"Ingresos pendientes: {fc.formatear_precio(ingresos_pendientes)}")
    print(f"Ingresos potenciales: {fc.formatear_precio(ingresos_potenciales)}")
    
    print("\n--- EGRESOS ---")
    print(f"Total reembolsos: {fc.formatear_precio(total_reembolsos)}")
    
    print("\n--- BALANCE ---")
    print(f"Ingresos netos: {fc.formatear_precio(ingresos_netos)}")
    
    if ingresos_potenciales > 0:
        print("\n--- DISTRIBUCIÓN DE INGRESOS ---")
        pct_real = (ingresos_reales * 100) / ingresos_potenciales
        pct_pendiente = (ingresos_pendientes * 100) / ingresos_potenciales
        
        barra_real = "" * int(pct_real / 2.5)
        barra_pendiente = "" * int(pct_pendiente / 2.5)
        
        print(f"Cobrado:   {barra_real} {pct_real:.1f}%")
        print(f"Pendiente: {barra_pendiente} {pct_pendiente:.1f}%")
    
    fc.pausar()


def informe_financiero_general():
    """Genera informe financiero general del sistema."""
    conn = fc.conectar_bd()
    cursor = conn.cursor()
    
    cursor.execute('SELECT COUNT(*) as total FROM eventos')
    total_eventos = cursor.fetchone()['total']
    
    cursor.execute('SELECT COUNT(*) as total FROM inscripciones')
    total_inscripciones = cursor.fetchone()['total']
    
    cursor.execute("SELECT COUNT(*) as total FROM inscripciones WHERE estado_pago = 'pagado'")
    pagos_completados = cursor.fetchone()['total']
    
    cursor.execute("SELECT COUNT(*) as total FROM inscripciones WHERE estado_pago = 'pendiente'")
    pagos_pendientes = cursor.fetchone()['total']
    
    cursor.execute('SELECT COALESCE(SUM(monto), 0) as total FROM pagos')
    total_ingresos = cursor.fetchone()['total']
    
    cursor.execute('SELECT COALESCE(SUM(monto), 0) as total FROM reembolsos')
    total_reembolsos = cursor.fetchone()['total']
    
    cursor.execute('''
        SELECT COALESCE(SUM(e.precio), 0) as total 
        FROM inscripciones i
        JOIN eventos e ON i.id_evento = e.id
        WHERE i.estado_pago = 'pendiente'
    ''')
    total_pendiente = cursor.fetchone()['total']
    
    cursor.execute('''
        SELECT e.nombre, COALESCE(SUM(p.monto), 0) as ingresos
        FROM eventos e
        LEFT JOIN inscripciones i ON e.id = i.id_evento
        LEFT JOIN pagos p ON i.id = p.id_inscripcion
        GROUP BY e.id, e.nombre
        ORDER BY ingresos DESC
        LIMIT 5
    ''')
    top_eventos = cursor.fetchall()
    
    conn.close()
    
    ingresos_netos = total_ingresos - total_reembolsos
    
    print("\n" + "=" * 60)
    print("           REPORTE FINANCIERO GENERAL")
    print("=" * 60)
    print(f"Total eventos registrados: {total_eventos}")
    print(f"Total inscripciones: {total_inscripciones}")
    
    print("\n--- PAGOS ---")
    print(f"Completados: {pagos_completados}")
    print(f"Pendientes: {pagos_pendientes}")
    
    if total_inscripciones > 0:
        tasa_pago = (pagos_completados * 100) / total_inscripciones
        print(f"Tasa de pago: {tasa_pago:.2f}%")
    
    print("\n--- INGRESOS ---")
    print(f"Ingresos totales: {fc.formatear_precio(total_ingresos)}")
    print(f"Ingresos pendientes: {fc.formatear_precio(total_pendiente)}")
    print(f"Total reembolsos: {fc.formatear_precio(total_reembolsos)}")
    print(f"Ingresos netos: {fc.formatear_precio(ingresos_netos)}")
    
    if top_eventos:
        print("\n--- TOP 5 EVENTOS MÁS RENTABLES ---")
        for i, evento in enumerate(top_eventos, 1):
            evento = dict(evento)
            print(f"{i}. {evento['nombre']}: {fc.formatear_precio(evento['ingresos'])}")
    
    fc.pausar()


def solicitar_evento_finalizado():
    """Solicita un evento finalizado al usuario."""
    print("\nIngrese el nombre o parte del nombre del evento:")
    criterio = input("> ").strip()
    
    conn = fc.conectar_bd()
    cursor = conn.cursor()
    
    hoy = date.today().strftime('%Y-%m-%d')
    cursor.execute('''
        SELECT * FROM eventos 
        WHERE nombre LIKE ? AND fecha <= ?
        ORDER BY fecha DESC
    ''', (f'%{criterio}%', hoy))
    
    eventos_finalizados = cursor.fetchall()
    conn.close()
    
    if not eventos_finalizados:
        fc.mostrar_error("No se encontraron eventos finalizados con ese criterio")
        return None
    
    print("\n--- Eventos Coincidentes ---")
    for i, evento in enumerate(eventos_finalizados, 1):
        evento = dict(evento)
        print(f"{i}. {evento['nombre']} (ID: {evento['id']}) - {fc.formatear_fecha(evento['fecha'])}")
    
    try:
        opcion = int(input("\nIngrese el número de la opción (0 para cancelar): "))
        if opcion == 0:
            return None
        if 1 <= opcion <= len(eventos_finalizados):
            return dict(eventos_finalizados[opcion - 1])['id']
        else:
            fc.mostrar_error("Opción no válida")
            return None
    except ValueError:
        fc.mostrar_error("Por favor ingrese un número válido")
        return None
