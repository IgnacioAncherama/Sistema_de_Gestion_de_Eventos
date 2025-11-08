"""
Módulo de Administración de Pagos y Cobros
Sistema de Gestión de Eventos

Este módulo maneja el registro de pagos, consultas, recordatorios y reembolsos.
"""

from datetime import date, datetime
import funciones_comunes as fc


def menu_principal_pagos():
    """Muestra el menú principal de administración de pagos."""
    while True:
        fc.limpiar_pantalla()
        print("=" * 60)
        print("           MENÚ ADMINISTRACIÓN DE PAGOS")
        print("=" * 60)
        print("P. Registrar pago")
        print("C. Consultar pagos")
        print("R. Generar recordatorios")
        print("D. Procesar reembolsos")
        print("F. Generar reportes financieros")
        print("S. Salir del módulo")
        print("=" * 60)
        
        opcion = input("\nSeleccione una opción: ").upper().strip()
        
        if opcion == 'P':
            proceso_registrar_pago()
        elif opcion == 'C':
            proceso_consultar_pagos()
        elif opcion == 'R':
            proceso_generar_recordatorios()
        elif opcion == 'D':
            proceso_procesar_reembolsos()
        elif opcion == 'F':
            proceso_generar_reportes_financieros()
        elif opcion == 'S':
            fc.mostrar_mensaje("Saliendo del módulo de pagos...")
            break
        else:
            fc.mostrar_error("Opción no válida. Intente nuevamente.")
            fc.pausar()


def proceso_registrar_pago():
    """Registra un nuevo pago."""
    fc.limpiar_pantalla()
    print("=" * 60)
    print("           REGISTRAR NUEVO PAGO")
    print("=" * 60)
    
    # Paso 1: Mostrar eventos con inscripciones pendientes
    conn = fc.conectar_bd()
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT DISTINCT e.id, e.nombre, e.fecha, e.precio,
               COUNT(i.id) as inscripciones_pendientes
        FROM eventos e
        JOIN inscripciones i ON e.id = i.id_evento
        WHERE i.estado_pago = 'pendiente'
        GROUP BY e.id
        ORDER BY e.fecha DESC
    ''')
    eventos_con_pendientes = cursor.fetchall()
    
    if not eventos_con_pendientes:
        conn.close()
        fc.mostrar_mensaje("No hay eventos con pagos pendientes")
        fc.pausar()
        return
    
    print("\n--- EVENTOS CON PAGOS PENDIENTES ---")
    for evento in eventos_con_pendientes:
        evento = dict(evento)
        print(f"\nID: {evento['id']} - {evento['nombre']}")
        print(f"  Fecha: {fc.formatear_fecha(evento['fecha'])}")
        print(f"  Precio: {fc.formatear_precio(evento['precio'])}")
        print(f"  Inscripciones pendientes: {evento['inscripciones_pendientes']}")
    
    # Paso 2: Seleccionar evento
    print("\n" + "=" * 60)
    try:
        id_evento_seleccionado = int(input("Ingrese el ID del evento: "))
    except ValueError:
        conn.close()
        fc.mostrar_error("ID inválido")
        fc.pausar()
        return
    
    # Verificar que el evento existe y tiene pendientes
    evento_existe = False
    for evento in eventos_con_pendientes:
        if dict(evento)['id'] == id_evento_seleccionado:
            evento_existe = True
            break
    
    if not evento_existe:
        conn.close()
        fc.mostrar_error("Evento no encontrado o sin pagos pendientes")
        fc.pausar()
        return
    
    # Paso 3: Mostrar inscripciones pendientes del evento
    cursor.execute('''
        SELECT i.id, p.nombre, p.apellido, p.documento, i.fecha_inscripcion
        FROM inscripciones i
        JOIN participantes p ON i.id_participante = p.id
        WHERE i.id_evento = ? AND i.estado_pago = 'pendiente'
        ORDER BY i.fecha_inscripcion
    ''', (id_evento_seleccionado,))
    inscripciones_pendientes = cursor.fetchall()
    
    conn.close()
    
    if not inscripciones_pendientes:
        fc.mostrar_mensaje("No hay inscripciones pendientes para este evento")
        fc.pausar()
        return
    
    print("\n--- INSCRIPCIONES PENDIENTES DE PAGO ---")
    for insc in inscripciones_pendientes:
        insc = dict(insc)
        print(f"\nID Inscripción: {insc['id']}")
        print(f"  Participante: {insc['nombre']} {insc['apellido']}")
        print(f"  Documento: {insc['documento']}")
        print(f"  Fecha inscripción: {fc.formatear_fecha(insc['fecha_inscripcion'])}")
    
    # Paso 4: Seleccionar inscripción
    print("\n" + "=" * 60)
    try:
        id_inscripcion = int(input("Ingrese el ID de la inscripción a pagar: "))
    except ValueError:
        fc.mostrar_error("ID inválido")
        fc.pausar()
        return
    
    # Verificar que la inscripción existe y está pendiente
    if not fc.existe_inscripcion(id_inscripcion):
        fc.mostrar_error("Inscripción no encontrada")
        fc.pausar()
        return
    
    info_inscripcion = fc.obtener_info_inscripcion(id_inscripcion)
    
    if info_inscripcion['estado_pago'] == 'pagado':
        fc.mostrar_error("Esta inscripción ya ha sido pagada")
        fc.pausar()
        return
    
    if info_inscripcion['estado_pago'] == 'reembolsado':
        fc.mostrar_error("Esta inscripción fue reembolsada, no se puede pagar")
        fc.pausar()
        return
    
    # Verificar que la inscripción pertenece al evento seleccionado
    if info_inscripcion['id_evento'] != id_evento_seleccionado:
        fc.mostrar_error("La inscripción no pertenece al evento seleccionado")
        fc.pausar()
        return
    
    # Paso 5: Procesar el pago
    id_evento = fc.obtener_evento_de_inscripcion(id_inscripcion)
    info_evento = fc.obtener_info_evento(id_evento)
    id_participante = info_inscripcion['id_participante']
    info_participante = fc.obtener_info_participante(id_participante)
    
    print("\n" + "=" * 60)
    print("           CONFIRMAR DATOS DEL PAGO")
    print("=" * 60)
    print(f"Evento: {info_evento['nombre']}")
    print(f"Participante: {info_participante['nombre']} {info_participante['apellido']}")
    print(f"Documento: {info_participante['documento']}")
    print(f"Monto a pagar: {fc.formatear_precio(info_evento['precio'])}")
    
    print("\nMétodos de pago disponibles:")
    print("1. Efectivo")
    print("2. Tarjeta")
    print("3. Transferencia")
    
    metodo = input("\nSeleccione método de pago (1-3): ").strip()
    metodos = {'1': 'Efectivo', '2': 'Tarjeta', '3': 'Transferencia'}
    metodo_pago = metodos.get(metodo, 'Efectivo')
    
    try:
        monto = float(input("Ingrese monto recibido: "))
    except ValueError:
        fc.mostrar_error("Monto inválido")
        fc.pausar()
        return
    
    if monto < info_evento['precio']:
        fc.mostrar_error(f"Monto insuficiente. Falta: {fc.formatear_precio(info_evento['precio'] - monto)}")
        fc.pausar()
        return
    
    cambio = monto - info_evento['precio']
    
    print("\n--- DATOS ADICIONALES DEL PAGO (obligatorios) ---")
    concepto = input("Concepto del pago: ").strip()
    numero_comprobante = input("Número de comprobante: ").strip()
    observaciones = input("Observaciones: ").strip()
    
    # Validar campos obligatorios
    if not concepto or not numero_comprobante or not observaciones:
        fc.mostrar_error("Todos los campos son obligatorios")
        fc.pausar()
        return
    
    pago = {
        'id_inscripcion': id_inscripcion,
        'monto': info_evento['precio'],
        'metodo_pago': metodo_pago,
        'fecha_pago': date.today(),
        'estado': 'confirmado',
        'concepto': concepto,
        'numero_comprobante': numero_comprobante,
        'observaciones': observaciones
    }
    
    id_pago = fc.guardar_pago(pago)
    fc.actualizar_estado_pago_inscripcion(id_inscripcion, 'pagado')
    
    print("\n" + "=" * 60)
    fc.mostrar_exito(f"Pago registrado exitosamente. ID de pago: {id_pago}")
    print(f"Participante: {info_participante['nombre']} {info_participante['apellido']}")
    print(f"Evento: {info_evento['nombre']}")
    print(f"Monto pagado: {fc.formatear_precio(info_evento['precio'])}")
    if cambio > 0:
        fc.mostrar_mensaje(f"Cambio a devolver: {fc.formatear_precio(cambio)}")
    print("=" * 60)
    
    fc.pausar()


def proceso_consultar_pagos():
    """Consulta pagos según diferentes criterios."""
    fc.limpiar_pantalla()
    print("=" * 60)
    print("           CONSULTA DE PAGOS")
    print("=" * 60)
    print("I. Consultar por inscripción")
    print("E. Consultar por evento")
    print("P. Ver pagos pendientes")
    print("T. Ver todos los pagos")
    print("=" * 60)
    
    opcion = input("\nSeleccione una opción: ").upper().strip()
    
    if opcion == 'I':
        consultar_por_inscripcion()
    elif opcion == 'E':
        consultar_por_evento()
    elif opcion == 'P':
        mostrar_pagos_pendientes()
    elif opcion == 'T':
        mostrar_todos_los_pagos()
    else:
        fc.mostrar_error("Opción no válida")
    
    fc.pausar()


def consultar_por_inscripcion():
    """Consulta el pago de una inscripción específica."""
    id_inscripcion = fc.solicitar_id_inscripcion()
    
    if not fc.existe_inscripcion(id_inscripcion):
        fc.mostrar_error("Inscripción no encontrada")
        return
    
    info_inscripcion = fc.obtener_info_inscripcion(id_inscripcion)
    
    print("\n=== INFORMACIÓN DE PAGO ===")
    print(f"ID Inscripción: {id_inscripcion}")
    print(f"Estado de pago: {info_inscripcion['estado_pago']}")
    
    conn = fc.conectar_bd()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM pagos WHERE id_inscripcion = ?', (id_inscripcion,))
    pago = cursor.fetchone()
    conn.close()
    
    if pago:
        pago = dict(pago)
        print(f"ID Pago: {pago['id']}")
        print(f"Monto: {fc.formatear_precio(pago['monto'])}")
        print(f"Método: {pago['metodo_pago']}")
        print(f"Fecha: {fc.formatear_fecha(pago['fecha_pago'])}")
    else:
        if info_inscripcion['estado_pago'] == 'pendiente':
            print("Este pago aún no ha sido realizado")


def consultar_por_evento():
    """Consulta los pagos de un evento."""
    id_evento = fc.solicitar_id_evento()
    
    if not fc.existe_evento(id_evento):
        fc.mostrar_error("Evento no encontrado")
        return
    
    info_evento = fc.obtener_info_evento(id_evento)
    print(f"\n=== PAGOS DEL EVENTO: {info_evento['nombre']} ===")
    
    conn = fc.conectar_bd()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT p.* FROM pagos p
        JOIN inscripciones i ON p.id_inscripcion = i.id
        WHERE i.id_evento = ?
    ''', (id_evento,))
    pagos = cursor.fetchall()
    conn.close()
    
    if not pagos:
        fc.mostrar_mensaje("No hay pagos registrados para este evento")
        return
    
    total = 0
    for pago in pagos:
        pago = dict(pago)
        print(f"\nID: {pago['id']} | Monto: {fc.formatear_precio(pago['monto'])} | "
              f"Método: {pago['metodo_pago']} | Fecha: {fc.formatear_fecha(pago['fecha_pago'])}")
        total += pago['monto']
    
    print(f"\nTotal recaudado: {fc.formatear_precio(total)}")


def mostrar_pagos_pendientes():
    """Muestra todas las inscripciones con pagos pendientes."""
    print("\n=== PAGOS PENDIENTES ===")
    
    conn = fc.conectar_bd()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM inscripciones WHERE estado_pago = 'pendiente'
    ''')
    pendientes = cursor.fetchall()
    conn.close()
    
    if not pendientes:
        fc.mostrar_mensaje("No hay pagos pendientes")
        return
    
    print(f"Total: {len(pendientes)}")
    
    total_pendiente = 0
    for insc in pendientes:
        insc = dict(insc)
        info_evento = fc.obtener_info_evento(insc['id_evento'])
        info_participante = fc.obtener_info_participante(insc['id_participante'])
        
        print(f"\nInscripción #{insc['id']}")
        print(f"  Participante: {info_participante['nombre']} {info_participante['apellido']}")
        print(f"  Evento: {info_evento['nombre']}")
        print(f"  Monto: {fc.formatear_precio(info_evento['precio'])}")
        
        total_pendiente += info_evento['precio']
    
    print(f"\nMonto total pendiente: {fc.formatear_precio(total_pendiente)}")


def mostrar_todos_los_pagos():
    """Muestra todos los pagos registrados."""
    conn = fc.conectar_bd()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM pagos ORDER BY fecha_pago DESC')
    pagos = cursor.fetchall()
    conn.close()
    
    if not pagos:
        fc.mostrar_mensaje("No hay pagos registrados")
        return
    
    print(f"\n=== TODOS LOS PAGOS ===")
    print(f"Total: {len(pagos)}")
    
    total = 0
    for pago in pagos:
        pago = dict(pago)
        print(f"\nID: {pago['id']} | Inscripción: {pago['id_inscripcion']} | "
              f"Monto: {fc.formatear_precio(pago['monto'])} | Método: {pago['metodo_pago']} | "
              f"Fecha: {fc.formatear_fecha(pago['fecha_pago'])}")
        total += pago['monto']
    
    print(f"\nTotal: {fc.formatear_precio(total)}")


def proceso_generar_recordatorios():
    """Genera recordatorios de pago pendiente."""
    fc.limpiar_pantalla()
    print("=" * 60)
    print("           GENERAR RECORDATORIOS DE PAGO")
    print("=" * 60)
    
    print("Ingrese ID del evento (o 0 para todos los eventos):")
    id_evento = fc.solicitar_id_evento()
    
    conn = fc.conectar_bd()
    cursor = conn.cursor()
    
    if id_evento == 0:
        cursor.execute('''
            SELECT * FROM inscripciones WHERE estado_pago = 'pendiente'
        ''')
    else:
        if not fc.existe_evento(id_evento):
            fc.mostrar_error("Evento no encontrado")
            conn.close()
            fc.pausar()
            return
        
        cursor.execute('''
            SELECT * FROM inscripciones 
            WHERE id_evento = ? AND estado_pago = 'pendiente'
        ''', (id_evento,))
    
    pendientes = cursor.fetchall()
    conn.close()
    
    if not pendientes:
        fc.mostrar_mensaje("No hay pagos pendientes")
        fc.pausar()
        return
    
    print(f"\nSe enviarán {len(pendientes)} recordatorios")
    
    if fc.usuario_confirma_operacion("¿Desea continuar?"):
        contador = 0
        for insc in pendientes:
            insc = dict(insc)
            info_participante = fc.obtener_info_participante(insc['id_participante'])
            info_evento = fc.obtener_info_evento(insc['id_evento'])
            
            fecha_evento = datetime.strptime(info_evento['fecha'], '%Y-%m-%d').date()
            dias_restantes = (fecha_evento - date.today()).days
            
            print(f"\nRecordatorio enviado a: {info_participante['email']}")
            print(f"  Evento: {info_evento['nombre']}")
            print(f"  Días restantes: {dias_restantes}")
            
            contador += 1
        
        fc.mostrar_exito(f"{contador} recordatorios enviados exitosamente")
    else:
        fc.mostrar_mensaje("Operación cancelada")
    
    fc.pausar()


def proceso_procesar_reembolsos():
    """Procesa un reembolso."""
    fc.limpiar_pantalla()
    print("=" * 60)
    print("           PROCESAR REEMBOLSO")
    print("=" * 60)
    
    id_inscripcion = fc.solicitar_id_inscripcion()
    
    if not fc.existe_inscripcion(id_inscripcion):
        fc.mostrar_error("Inscripción no encontrada")
        fc.pausar()
        return
    
    info_inscripcion = fc.obtener_info_inscripcion(id_inscripcion)
    
    if info_inscripcion['estado_pago'] != 'pagado':
        fc.mostrar_error("No se puede reembolsar. El pago no ha sido registrado")
        fc.pausar()
        return
    
    id_evento = fc.obtener_evento_de_inscripcion(id_inscripcion)
    info_evento = fc.obtener_info_evento(id_evento)
    
    fecha_evento = datetime.strptime(info_evento['fecha'], '%Y-%m-%d').date()
    dias_restantes = (fecha_evento - date.today()).days
    porcentaje = calcular_porcentaje_reembolso(dias_restantes)
    monto_reembolso = info_evento['precio'] * (porcentaje / 100)
    
    print(f"\nEvento: {info_evento['nombre']}")
    print(f"Precio pagado: {fc.formatear_precio(info_evento['precio'])}")
    print(f"Días hasta el evento: {dias_restantes}")
    print(f"Porcentaje de reembolso: {porcentaje}%")
    print(f"Monto a reembolsar: {fc.formatear_precio(monto_reembolso)}")
    
    if fc.usuario_confirma_operacion("¿Confirma el reembolso?"):
        conn = fc.conectar_bd()
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO reembolsos (id_inscripcion, monto, fecha_reembolso)
            VALUES (?, ?, ?)
        ''', (id_inscripcion, monto_reembolso, date.today().strftime('%Y-%m-%d')))
        
        id_reembolso = cursor.lastrowid
        conn.commit()
        conn.close()
        
        fc.actualizar_estado_pago_inscripcion(id_inscripcion, 'reembolsado')
        fc.mostrar_exito(f"Reembolso procesado exitosamente. ID: {id_reembolso}")
    else:
        fc.mostrar_mensaje("Operación cancelada")
    
    fc.pausar()


def calcular_porcentaje_reembolso(dias_restantes: int) -> int:
    """Calcula el porcentaje de reembolso según días restantes."""
    if dias_restantes > 30:
        return 100
    elif dias_restantes >= 15:
        return 75
    elif dias_restantes >= 7:
        return 50
    else:
        return 25


def proceso_generar_reportes_financieros():
    """Genera reportes financieros."""
    fc.limpiar_pantalla()
    print("=" * 60)
    print("           REPORTES FINANCIEROS")
    print("=" * 60)
    print("E. Reporte por evento")
    print("G. Reporte general")
    print("=" * 60)
    
    opcion = input("\nSeleccione una opción: ").upper().strip()
    
    if opcion == 'E':
        generar_reporte_evento()
    elif opcion == 'G':
        generar_reporte_general()
    else:
        fc.mostrar_error("Opción no válida")
    
    fc.pausar()


def generar_reporte_evento():
    """Genera un reporte financiero para un evento específico."""
    id_evento = fc.solicitar_id_evento()
    
    if not fc.existe_evento(id_evento):
        fc.mostrar_error("Evento no encontrado")
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
    total_ingresos = cursor.fetchone()['total']
    
    cursor.execute('''
        SELECT COALESCE(SUM(r.monto), 0) as total FROM reembolsos r
        JOIN inscripciones i ON r.id_inscripcion = i.id
        WHERE i.id_evento = ?
    ''', (id_evento,))
    total_reembolsos = cursor.fetchone()['total']
    
    conn.close()
    
    total_pendiente = pagos_pendientes * info_evento['precio']
    ingresos_netos = total_ingresos - total_reembolsos
    
    print("\n" + "=" * 60)
    print("           REPORTE FINANCIERO DEL EVENTO")
    print("=" * 60)
    print(f"Evento: {info_evento['nombre']}")
    print(f"Fecha: {fc.formatear_fecha(info_evento['fecha'])}")
    print(f"\nTotal inscripciones: {total_inscripciones}")
    print(f"Pagos completados: {pagos_completados}")
    print(f"Pagos pendientes: {pagos_pendientes}")
    print(f"\nTotal ingresos: {fc.formatear_precio(total_ingresos)}")
    print(f"Monto pendiente: {fc.formatear_precio(total_pendiente)}")
    print(f"Total reembolsos: {fc.formatear_precio(total_reembolsos)}")
    print(f"Ingresos netos: {fc.formatear_precio(ingresos_netos)}")
    print("=" * 60)


def generar_reporte_general():
    """Genera un reporte financiero general del sistema."""
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
    
    conn.close()
    
    ingresos_netos = total_ingresos - total_reembolsos
    
    print("\n" + "=" * 60)
    print("           REPORTE FINANCIERO GENERAL")
    print("=" * 60)
    print(f"Total eventos activos: {total_eventos}")
    print(f"Total inscripciones: {total_inscripciones}")
    print(f"\nPagos completados: {pagos_completados}")
    print(f"Pagos pendientes: {pagos_pendientes}")
    print(f"\nTotal ingresos: {fc.formatear_precio(total_ingresos)}")
    print(f"Monto pendiente: {fc.formatear_precio(total_pendiente)}")
    print(f"Total reembolsos: {fc.formatear_precio(total_reembolsos)}")
    print(f"Ingresos netos: {fc.formatear_precio(ingresos_netos)}")
    
    if total_inscripciones > 0:
        tasa_pago = (pagos_completados * 100) / total_inscripciones
        print(f"\nTasa de pago: {tasa_pago:.2f}%")
    
    print("=" * 60)
