"""
Módulo de Realización del Evento
Sistema de Gestión de Eventos

Este módulo maneja el control de asistencia, registro de llegadas y finalización de eventos.
"""

from datetime import date, datetime
import funciones_comunes as fc


def menu_principal_realizacion():
    """Muestra el menú principal de realización del evento."""
    while True:
        fc.limpiar_pantalla()
        print("=" * 60)
        print("           MENÚ REALIZACIÓN DEL EVENTO")
        print("=" * 60)
        print("I. Iniciar control de asistencia")
        print("L. Registrar llegada de participante")
        print("A. Consultar asistencia en tiempo real")
        print("R. Gestionar recursos del evento")
        print("F. Finalizar evento")
        print("S. Salir del módulo")
        print("=" * 60)
        
        opcion = input("\nSeleccione una opción: ").upper().strip()
        
        if opcion == 'I':
            proceso_iniciar_control_asistencia()
        elif opcion == 'L':
            proceso_registrar_llegada()
        elif opcion == 'A':
            proceso_consultar_asistencia()
        elif opcion == 'R':
            proceso_gestionar_recursos()
        elif opcion == 'F':
            proceso_finalizar_evento()
        elif opcion == 'S':
            fc.mostrar_mensaje("Saliendo del módulo de realización...")
            break
        else:
            fc.mostrar_error("Opción no válida. Intente nuevamente.")
            fc.pausar()


def proceso_iniciar_control_asistencia():
    """Inicia el control de asistencia para un evento."""
    fc.limpiar_pantalla()
    print("=" * 60)
    print("           INICIAR CONTROL DE ASISTENCIA")
    print("=" * 60)
    
    id_evento = fc.solicitar_id_evento()
    
    if not fc.existe_evento(id_evento):
        fc.mostrar_error("Evento no encontrado")
        fc.pausar()
        return
    
    info_evento = fc.obtener_info_evento(id_evento)
    fecha_evento = datetime.strptime(info_evento['fecha'], '%Y-%m-%d').date()
    
    if fecha_evento != date.today():
        fc.mostrar_error(f"El evento no es hoy. Fecha del evento: {fc.formatear_fecha(fecha_evento)}")
        fc.pausar()
        return
    
    if info_evento['estado'] == 'en_curso':
        fc.mostrar_advertencia("El control de asistencia ya está activo para este evento")
        fc.pausar()
        return
    
    conn = fc.conectar_bd()
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT COUNT(*) as total FROM inscripciones 
        WHERE id_evento = ? AND estado = 'confirmada' AND estado_pago = 'pagado'
    ''', (id_evento,))
    total_esperados = cursor.fetchone()['total']
    
    cursor.execute('UPDATE eventos SET estado = ? WHERE id = ?', ('en_curso', id_evento))
    conn.commit()
    conn.close()
    
    fc.mostrar_exito("Control de asistencia iniciado")
    print(f"\nEvento: {info_evento['nombre']}")
    print(f"Participantes esperados: {total_esperados}")
    fc.pausar()


def proceso_registrar_llegada():
    """Registra la llegada de un participante al evento."""
    fc.limpiar_pantalla()
    print("=" * 60)
    print("           REGISTRAR LLEGADA DE PARTICIPANTE")
    print("=" * 60)
    
    documento = fc.solicitar_documento_participante()
    
    if not fc.existe_participante(documento):
        fc.mostrar_error("Participante no registrado")
        fc.pausar()
        return
    
    id_participante = fc.obtener_id_participante(documento)
    participante = fc.obtener_info_participante(id_participante)
    
    conn = fc.conectar_bd()
    cursor = conn.cursor()
    
    hoy = date.today().strftime('%Y-%m-%d')
    cursor.execute('''
        SELECT i.* FROM inscripciones i
        JOIN eventos e ON i.id_evento = e.id
        WHERE i.id_participante = ? AND e.fecha = ? AND i.estado = 'confirmada'
    ''', (id_participante, hoy))
    
    inscripcion = cursor.fetchone()
    
    if not inscripcion:
        conn.close()
        fc.mostrar_error("Participante no inscrito en eventos de hoy")
        fc.pausar()
        return
    
    inscripcion = dict(inscripcion)
    
    if inscripcion['estado_pago'] != 'pagado':
        conn.close()
        fc.mostrar_error("Pago pendiente. Dirigirse a caja")
        fc.pausar()
        return
    
    cursor.execute('''
        SELECT * FROM asistencia 
        WHERE id_evento = ? AND id_participante = ?
    ''', (inscripcion['id_evento'], id_participante))
    
    if cursor.fetchone():
        conn.close()
        fc.mostrar_advertencia("Participante ya registró su llegada")
        fc.pausar()
        return
    
    cursor.execute('''
        INSERT INTO asistencia (id_inscripcion, fecha_hora_llegada, presente)
        VALUES (?, ?, 1)
    ''', (inscripcion['id'], datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    
    conn.commit()
    conn.close()
    
    info_evento = fc.obtener_info_evento(inscripcion['id_evento'])
    
    fc.mostrar_exito("Llegada registrada exitosamente")
    print(f"\nParticipante: {participante['nombre']} {participante['apellido']}")
    print(f"Evento: {info_evento['nombre']}")
    print(f"Ubicación: {info_evento['ubicacion']}")
    fc.pausar()


def proceso_consultar_asistencia():
    """Consulta la asistencia en tiempo real de un evento."""
    fc.limpiar_pantalla()
    print("=" * 60)
    print("           CONSULTAR ASISTENCIA EN TIEMPO REAL")
    print("=" * 60)
    
    id_evento = fc.solicitar_id_evento()
    
    if not fc.existe_evento(id_evento):
        fc.mostrar_error("Evento no encontrado")
        fc.pausar()
        return
    
    info_evento = fc.obtener_info_evento(id_evento)
    
    conn = fc.conectar_bd()
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT COUNT(*) as total FROM inscripciones 
        WHERE id_evento = ? AND estado = 'confirmada' AND estado_pago = 'pagado'
    ''', (id_evento,))
    total_inscriptos = cursor.fetchone()['total']
    
    cursor.execute('''
        SELECT COUNT(*) as total FROM asistencia a
        JOIN inscripciones i ON a.id_inscripcion = i.id
        WHERE i.id_evento = ?
    ''', (id_evento,))
    participantes_presentes = cursor.fetchone()['total']
    
    participantes_ausentes = total_inscriptos - participantes_presentes
    
    porcentaje_asistencia = 0
    if total_inscriptos > 0:
        porcentaje_asistencia = (participantes_presentes * 100) / total_inscriptos
    
    print("\n" + "=" * 60)
    print("           RESUMEN DE ASISTENCIA")
    print("=" * 60)
    print(f"Evento: {info_evento['nombre']}")
    print(f"Fecha: {fc.formatear_fecha(info_evento['fecha'])}")
    print(f"\nTotal inscriptos: {total_inscriptos}")
    print(f"Presentes: {participantes_presentes}")
    print(f"Ausentes: {participantes_ausentes}")
    print(f"Porcentaje de asistencia: {porcentaje_asistencia:.2f}%")
    
    cursor.execute('''
        SELECT a.*, p.nombre, p.apellido, a.fecha_hora_llegada
        FROM asistencia a
        JOIN inscripciones i ON a.id_inscripcion = i.id
        JOIN participantes p ON i.id_participante = p.id
        WHERE i.id_evento = ?
        ORDER BY a.fecha_hora_llegada
    ''', (id_evento,))
    presentes = cursor.fetchall()
    
    if presentes:
        print("\n--- LISTA DE PRESENTES ---")
        for registro in presentes:
            registro = dict(registro)
            hora = datetime.strptime(registro['fecha_hora_llegada'], '%Y-%m-%d %H:%M:%S')
            print(f"  • {registro['nombre']} {registro['apellido']} - Llegada: {hora.strftime('%H:%M:%S')}")
    
    conn.close()
    fc.pausar()


def proceso_gestionar_recursos():
    """Gestiona los recursos utilizados en el evento."""
    fc.limpiar_pantalla()
    print("=" * 60)
    print("           GESTIONAR RECURSOS DEL EVENTO")
    print("=" * 60)
    
    id_evento = fc.solicitar_id_evento()
    
    if not fc.existe_evento(id_evento):
        fc.mostrar_error("Evento no encontrado")
        fc.pausar()
        return
    
    info_evento = fc.obtener_info_evento(id_evento)
    
    if info_evento['estado'] != 'en_curso':
        fc.mostrar_error("El evento no está en curso")
        fc.pausar()
        return
    
    print(f"\nEvento: {info_evento['nombre']}")
    print("\nOpciones de gestión de recursos:")
    print("1. Registrar uso de equipos")
    print("2. Controlar capacidad de sala")
    print("3. Gestionar materiales")
    print("4. Registrar incidencias")
    
    opcion = input("\nSeleccione una opción: ").strip()
    
    conn = fc.conectar_bd()
    cursor = conn.cursor()
    
    if opcion == '1':
        equipo = input("Ingrese nombre del equipo: ").strip()
        cantidad = input("Ingrese cantidad utilizada: ").strip()
        
        cursor.execute('''
            INSERT INTO recursos_eventos (id_evento, tipo, nombre, cantidad, fecha_registro)
            VALUES (?, 'equipo', ?, ?, ?)
        ''', (id_evento, equipo, cantidad, datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        
        conn.commit()
        fc.mostrar_exito("Uso de equipo registrado")
    
    elif opcion == '2':
        cursor.execute('SELECT COUNT(*) as total FROM asistencia WHERE id_evento = ?', (id_evento,))
        asistentes_actuales = cursor.fetchone()['total']
        
        print(f"\nCapacidad máxima: {info_evento['capacidad_maxima']}")
        print(f"Asistentes registrados: {asistentes_actuales}")
        print(f"Espacios disponibles: {info_evento['capacidad_maxima'] - asistentes_actuales}")
        
        if asistentes_actuales >= info_evento['capacidad_maxima']:
            fc.mostrar_advertencia("Capacidad completa")
    
    elif opcion == '3':
        material = input("Ingrese material: ").strip()
        cantidad = input("Ingrese cantidad: ").strip()
        
        cursor.execute('''
            INSERT INTO recursos_eventos (id_evento, tipo, nombre, cantidad, fecha_registro)
            VALUES (?, 'material', ?, ?, ?)
        ''', (id_evento, material, cantidad, datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        
        conn.commit()
        fc.mostrar_exito("Material registrado")
    
    elif opcion == '4':
        incidencia = input("Describa la incidencia: ").strip()
        
        cursor.execute('''
            INSERT INTO recursos_eventos (id_evento, tipo, descripcion, fecha_registro)
            VALUES (?, 'incidencia', ?, ?)
        ''', (id_evento, incidencia, datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        
        conn.commit()
        fc.mostrar_exito("Incidencia registrada")
    
    else:
        fc.mostrar_error("Opción no válida")
    
    conn.close()
    fc.pausar()


def proceso_finalizar_evento():
    """Finaliza un evento y genera el resumen."""
    fc.limpiar_pantalla()
    print("=" * 60)
    print("           FINALIZAR EVENTO")
    print("=" * 60)
    
    id_evento = fc.solicitar_id_evento()
    
    if not fc.existe_evento(id_evento):
        fc.mostrar_error("Evento no encontrado")
        fc.pausar()
        return
    
    info_evento = fc.obtener_info_evento(id_evento)
    
    if info_evento['estado'] != 'en_curso':
        fc.mostrar_error("El evento no está en curso")
        fc.pausar()
        return
    
    print("\n" + "=" * 60)
    print("           RESUMEN FINAL DEL EVENTO")
    print("=" * 60)
    print(f"Evento: {info_evento['nombre']}")
    print(f"Fecha: {fc.formatear_fecha(info_evento['fecha'])}")
    
    conn = fc.conectar_bd()
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT COUNT(*) as total FROM inscripciones 
        WHERE id_evento = ? AND estado = 'confirmada' AND estado_pago = 'pagado'
    ''', (id_evento,))
    total_inscriptos = cursor.fetchone()['total']
    
    cursor.execute('''
        SELECT COUNT(*) as total FROM asistencia a
        JOIN inscripciones i ON a.id_inscripcion = i.id
        WHERE i.id_evento = ?
    ''', (id_evento,))
    participantes_presentes = cursor.fetchone()['total']
    
    print(f"\n--- Asistencia ---")
    print(f"Total inscriptos: {total_inscriptos}")
    print(f"Presentes: {participantes_presentes}")
    print(f"Ausentes: {total_inscriptos - participantes_presentes}")
    
    if total_inscriptos > 0:
        porcentaje = (participantes_presentes * 100) / total_inscriptos
        print(f"Porcentaje de asistencia: {porcentaje:.2f}%")
    
    cursor.execute('''
        SELECT COUNT(*) as total FROM recursos_eventos WHERE id_evento = ?
    ''', (id_evento,))
    total_recursos = cursor.fetchone()['total']
    
    if total_recursos > 0:
        print(f"\n--- Recursos Utilizados ---")
        print(f"Total de recursos registrados: {total_recursos}")
        
        cursor.execute('''
            SELECT COUNT(*) as total FROM recursos_eventos 
            WHERE id_evento = ? AND tipo = 'equipo'
        ''', (id_evento,))
        equipos = cursor.fetchone()['total']
        
        cursor.execute('''
            SELECT COUNT(*) as total FROM recursos_eventos 
            WHERE id_evento = ? AND tipo = 'material'
        ''', (id_evento,))
        materiales = cursor.fetchone()['total']
        
        cursor.execute('''
            SELECT COUNT(*) as total FROM recursos_eventos 
            WHERE id_evento = ? AND tipo = 'incidencia'
        ''', (id_evento,))
        incidencias = cursor.fetchone()['total']
        
        if equipos > 0:
            print(f"  • Equipos: {equipos}")
        if materiales > 0:
            print(f"  • Materiales: {materiales}")
        if incidencias > 0:
            print(f"  • Incidencias reportadas: {incidencias}")
    
    print("\n" + "=" * 60)
    
    if fc.usuario_confirma_operacion("¿Confirma finalización del evento?"):
        cursor.execute('UPDATE eventos SET estado = ? WHERE id = ?', ('finalizado', id_evento))
        conn.commit()
        conn.close()
        
        fc.mostrar_exito("Evento finalizado exitosamente")
        fc.mostrar_mensaje("El reporte final ha sido generado")
    else:
        conn.close()
        fc.mostrar_mensaje("Operación cancelada")
    
    fc.pausar()
