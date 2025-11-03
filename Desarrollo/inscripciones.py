"""
Módulo de Registro y Administración de Inscripciones
Sistema de Gestión de Eventos

Este módulo maneja el registro, consulta, modificación y cancelación de inscripciones.
"""

from datetime import date
import funciones_comunes as fc


def menu_principal_inscripciones():
    """Muestra el menú principal de inscripciones."""
    while True:
        fc.limpiar_pantalla()
        print("=" * 60)
        print("           MENÚ DE INSCRIPCIONES")
        print("=" * 60)
        print("R. Registrar inscripción")
        print("C. Consultar inscripciones")
        print("M. Modificar inscripción")
        print("X. Cancelar inscripción")
        print("L. Gestionar lista de espera")
        print("S. Salir del módulo")
        print("=" * 60)
        
        opcion = input("\nSeleccione una opción: ").upper().strip()
        
        if opcion == 'R':
            proceso_registrar_inscripcion()
        elif opcion == 'C':
            proceso_consultar_inscripciones()
        elif opcion == 'M':
            proceso_modificar_inscripcion()
        elif opcion == 'X':
            proceso_cancelar_inscripcion()
        elif opcion == 'L':
            proceso_gestionar_lista_espera()
        elif opcion == 'S':
            fc.mostrar_mensaje("Saliendo del módulo de inscripciones...")
            break
        else:
            fc.mostrar_error("Opción no válida. Intente nuevamente.")
            fc.pausar()


def proceso_registrar_inscripcion():
    """Registra una nueva inscripción."""
    fc.limpiar_pantalla()
    print("=" * 60)
    print("           REGISTRAR NUEVA INSCRIPCIÓN")
    print("=" * 60)
    
    id_evento = fc.solicitar_id_evento()
    
    if not fc.validar_evento_activo(id_evento):
        fc.pausar()
        return
    
    evento = fc.obtener_info_evento(id_evento)
    print(f"\nEvento: {evento['nombre']}")
    print(f"Fecha: {fc.formatear_fecha(evento['fecha'])}")
    print(f"Precio: {fc.formatear_precio(evento['precio'])}")
    
    documento = fc.solicitar_documento_participante()
    
    id_participante = obtener_o_registrar_participante(documento)
    if not id_participante:
        fc.pausar()
        return
    
    if fc.participante_ya_inscrito(id_evento, id_participante):
        fc.mostrar_error("El participante ya está inscrito en este evento")
        fc.pausar()
        return
    
    if not fc.hay_cupos_disponibles(id_evento):
        if fc.usuario_confirma_operacion("Evento completo. ¿Desea agregarse a lista de espera?"):
            agregar_a_lista_espera(id_evento, id_participante)
        fc.pausar()
        return
    
    inscripcion = {
        'id_evento': id_evento,
        'id_participante': id_participante,
        'fecha_inscripcion': date.today(),
        'estado': 'confirmada',
        'estado_pago': 'pendiente'
    }
    
    id_inscripcion = fc.guardar_inscripcion(inscripcion)
    fc.mostrar_exito(f"Inscripción registrada exitosamente. ID: {id_inscripcion}")
    fc.pausar()


def obtener_o_registrar_participante(documento: str) -> int:
    """Obtiene el ID de un participante o lo registra si no existe."""
    if fc.existe_participante(documento):
        id_participante = fc.obtener_id_participante(documento)
        participante = fc.obtener_info_participante(id_participante)
        print(f"\nParticipante encontrado: {participante['nombre']} {participante['apellido']}")
        return id_participante
    else:
        fc.mostrar_mensaje("Participante no registrado. Se solicitarán datos adicionales.")
        return registrar_nuevo_participante(documento)


def registrar_nuevo_participante(documento: str) -> int:
    """Registra un nuevo participante."""
    print("\n--- REGISTRO DE NUEVO PARTICIPANTE ---")
    
    nombre = input("Nombre: ").strip()
    apellido = input("Apellido: ").strip()
    email = input("Email: ").strip()
    telefono = input("Teléfono: ").strip()

    fecha_nacimiento = input("Fecha de nacimiento (DD/MM/AAAA): ").strip()
    genero = input("Género: ").strip()
    pais = input("País: ").strip()
    profesion = input("Profesión: ").strip()
    
    # Validar campos obligatorios
    if not fecha_nacimiento or not genero or not pais or not profesion:
        fc.mostrar_error("Todos los campos son obligatorios")
        fc.pausar()
        return None
    
    # Procesar fecha de nacimiento
    try:
        dia, mes, anio = map(int, fecha_nacimiento.split('/'))
        fecha_nac = date(anio, mes, dia)
    except ValueError:
        fc.mostrar_error("Formato de fecha inválido. Use DD/MM/AAAA")
        fc.pausar()
        return None
    
    participante = {
        'nombre': nombre,
        'apellido': apellido,
        'documento': documento,
        'email': email,
        'telefono': telefono,
        'fecha_nacimiento': fecha_nac,
        'genero': genero,
        'pais': pais,
        'profesion': profesion
    }
    
    id_participante = fc.guardar_participante(participante)
    fc.mostrar_exito("Participante registrado exitosamente")
    return id_participante


def agregar_a_lista_espera(id_evento: int, id_participante: int):
    """Agrega un participante a la lista de espera."""
    conn = fc.conectar_bd()
    cursor = conn.cursor()
    
    # Verificar si ya está en lista
    cursor.execute('''
        SELECT id FROM lista_espera 
        WHERE id_evento = ? AND id_participante = ?
    ''', (id_evento, id_participante))
    
    if cursor.fetchone():
        conn.close()
        fc.mostrar_error("El participante ya se encuentra en la lista de espera")
        return
    
    # Obtener siguiente posición
    cursor.execute('''
        SELECT MAX(posicion) as max_pos FROM lista_espera WHERE id_evento = ?
    ''', (id_evento,))
    resultado = cursor.fetchone()
    posicion = (resultado['max_pos'] or 0) + 1
    
    # Agregar a lista
    cursor.execute('''
        INSERT INTO lista_espera (id_evento, id_participante, posicion, fecha_registro)
        VALUES (?, ?, ?, ?)
    ''', (id_evento, id_participante, posicion, date.today().strftime('%Y-%m-%d')))
    
    conn.commit()
    conn.close()
    fc.mostrar_exito(f"Participante agregado a lista de espera en la posición: {posicion}")


def proceso_consultar_inscripciones():
    """Consulta inscripciones según diferentes criterios."""
    fc.limpiar_pantalla()
    print("=" * 60)
    print("           CONSULTA DE INSCRIPCIONES")
    print("=" * 60)
    print("E. Ver por evento")
    print("P. Ver por participante")
    print("T. Ver todas las inscripciones")
    print("=" * 60)
    
    opcion = input("\nSeleccione una opción: ").upper().strip()
    
    if opcion == 'E':
        consultar_por_evento()
    elif opcion == 'P':
        consultar_por_participante()
    elif opcion == 'T':
        consultar_todas()
    else:
        fc.mostrar_error("Opción no válida")
    
    fc.pausar()


def consultar_por_evento():
    """Consulta inscripciones de un evento específico."""
    id_evento = fc.solicitar_id_evento()
    
    if not fc.existe_evento(id_evento):
        fc.mostrar_error("Evento no encontrado")
        return
    
    evento = fc.obtener_info_evento(id_evento)
    print(f"\n--- INSCRIPCIONES DEL EVENTO: {evento['nombre']} ---")
    
    conn = fc.conectar_bd()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM inscripciones WHERE id_evento = ?', (id_evento,))
    inscripciones = cursor.fetchall()
    conn.close()
    
    if not inscripciones:
        fc.mostrar_mensaje("No hay inscripciones para este evento")
        return
    
    for insc in inscripciones:
        mostrar_inscripcion_detallada(dict(insc))


def consultar_por_participante():
    """Consulta inscripciones de un participante."""
    documento = fc.solicitar_documento_participante()
    
    if not fc.existe_participante(documento):
        fc.mostrar_error("Participante no encontrado")
        return
    
    id_participante = fc.obtener_id_participante(documento)
    participante = fc.obtener_info_participante(id_participante)
    
    print(f"\n--- INSCRIPCIONES DE: {participante['nombre']} {participante['apellido']} ---")
    
    conn = fc.conectar_bd()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM inscripciones WHERE id_participante = ?', (id_participante,))
    inscripciones = cursor.fetchall()
    conn.close()
    
    if not inscripciones:
        fc.mostrar_mensaje("No hay inscripciones para este participante")
        return
    
    for insc in inscripciones:
        mostrar_inscripcion_detallada(dict(insc))


def consultar_todas():
    """Consulta todas las inscripciones."""
    inscripciones = fc.obtener_todas_inscripciones()
    
    if not inscripciones:
        fc.mostrar_mensaje("No hay inscripciones registradas")
        return
    
    print("\n--- TODAS LAS INSCRIPCIONES ---")
    for insc in inscripciones:
        mostrar_inscripcion_detallada(insc)


def mostrar_inscripcion_detallada(inscripcion: dict):
    """Muestra la información detallada de una inscripción."""
    participante = fc.obtener_info_participante(inscripcion['id_participante'])
    evento = fc.obtener_info_evento(inscripcion['id_evento'])
    
    print(f"\n--- Inscripción ID: {inscripcion['id']} ---")
    print(f"Participante: {participante['nombre']} {participante['apellido']}")
    print(f"Evento: {evento['nombre']}")
    print(f"Fecha inscripción: {fc.formatear_fecha(inscripcion['fecha_inscripcion'])}")
    print(f"Estado: {inscripcion['estado']}")
    print(f"Estado pago: {inscripcion['estado_pago']}")
    print("-" * 60)


def proceso_modificar_inscripcion():
    """Modifica una inscripción existente."""
    fc.limpiar_pantalla()
    print("=" * 60)
    print("           MODIFICAR INSCRIPCIÓN")
    print("=" * 60)
    
    id_inscripcion = fc.solicitar_id_inscripcion()
    
    if not fc.existe_inscripcion(id_inscripcion):
        fc.mostrar_error("Inscripción no encontrada")
        fc.pausar()
        return
    
    inscripcion = fc.obtener_info_inscripcion(id_inscripcion)
    mostrar_inscripcion_detallada(inscripcion)
    
    print("\n¿Qué desea modificar?")
    print("E. Cambiar de evento")
    print("S. Cambiar estado de la inscripción")
    
    opcion = input("\nSeleccione una opción: ").upper().strip()
    
    if opcion == 'E':
        cambiar_evento_inscripcion(id_inscripcion, inscripcion)
    elif opcion == 'S':
        cambiar_estado_inscripcion(id_inscripcion)
    else:
        fc.mostrar_error("Opción no válida")
    
    fc.pausar()


def cambiar_evento_inscripcion(id_inscripcion: int, inscripcion: dict):
    """Cambia el evento de una inscripción."""
    id_evento_actual = inscripcion['id_evento']
    
    print("\nIngrese el ID del nuevo evento:")
    id_evento_nuevo = fc.solicitar_id_evento()
    
    if id_evento_nuevo == id_evento_actual:
        fc.mostrar_error("El nuevo evento es el mismo que el actual")
        return
    
    if not fc.validar_evento_activo(id_evento_nuevo):
        return
    
    if not fc.hay_cupos_disponibles(id_evento_nuevo):
        fc.mostrar_error("El nuevo evento no tiene cupos disponibles")
        return
    
    if fc.participante_ya_inscrito(id_evento_nuevo, inscripcion['id_participante']):
        fc.mostrar_error("El participante ya está inscrito en el evento de destino")
        return
    
    conn = fc.conectar_bd()
    cursor = conn.cursor()
    cursor.execute('UPDATE inscripciones SET id_evento = ? WHERE id = ?', 
                   (id_evento_nuevo, id_inscripcion))
    conn.commit()
    conn.close()
    
    promover_desde_lista_espera(id_evento_actual)
    fc.mostrar_exito("El cambio de evento se realizó correctamente")


def cambiar_estado_inscripcion(id_inscripcion: int):
    """Cambia el estado de una inscripción."""
    print("\nEstados disponibles: confirmada, pendiente, cancelada")
    nuevo_estado = input("Ingrese el nuevo estado: ").strip().lower()
    
    if nuevo_estado in ['confirmada', 'pendiente', 'cancelada']:
        fc.actualizar_estado_inscripcion(id_inscripcion, nuevo_estado)
    else:
        fc.mostrar_error("Estado no válido")


def proceso_cancelar_inscripcion():
    """Cancela una inscripción."""
    fc.limpiar_pantalla()
    print("=" * 60)
    print("           CANCELAR INSCRIPCIÓN")
    print("=" * 60)
    
    id_inscripcion = fc.solicitar_id_inscripcion()
    
    if not fc.validar_inscripcion_para_cancelacion(id_inscripcion):
        fc.pausar()
        return
    
    inscripcion = fc.obtener_info_inscripcion(id_inscripcion)
    mostrar_inscripcion_detallada(inscripcion)
    
    id_evento = inscripcion['id_evento']
    evento = fc.obtener_info_evento(id_evento)
    fecha_evento = datetime.strptime(evento['fecha'], '%Y-%m-%d').date()
    dias_restantes = (fecha_evento - date.today()).days
    
    if dias_restantes < 1:
        fc.mostrar_advertencia("Cancelación tardía. Se podrían aplicar penalizaciones.")
    
    if fc.usuario_confirma_operacion("¿Confirma la cancelación?"):
        fc.actualizar_estado_inscripcion(id_inscripcion, 'cancelada')
        
        if fc.hay_participantes_en_espera(id_evento):
            promover_desde_lista_espera(id_evento)
    else:
        fc.mostrar_mensaje("Operación cancelada")
    
    fc.pausar()


def promover_desde_lista_espera(id_evento: int):
    """Promueve al primer participante de la lista de espera."""
    conn = fc.conectar_bd()
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT * FROM lista_espera 
        WHERE id_evento = ? 
        ORDER BY posicion ASC 
        LIMIT 1
    ''', (id_evento,))
    
    primer_espera = cursor.fetchone()
    
    if not primer_espera:
        conn.close()
        return
    
    id_participante = primer_espera['id_participante']
    
    inscripcion = {
        'id_evento': id_evento,
        'id_participante': id_participante,
        'fecha_inscripcion': date.today(),
        'estado': 'confirmada',
        'estado_pago': 'pendiente'
    }
    
    id_inscripcion = fc.guardar_inscripcion(inscripcion)
    
    cursor.execute('DELETE FROM lista_espera WHERE id = ?', (primer_espera['id'],))
    
    cursor.execute('''
        UPDATE lista_espera 
        SET posicion = posicion - 1 
        WHERE id_evento = ? AND posicion > ?
    ''', (id_evento, primer_espera['posicion']))
    
    conn.commit()
    conn.close()
    
    participante = fc.obtener_info_participante(id_participante)
    fc.mostrar_mensaje(f"Se ha promovido a {participante['nombre']} {participante['apellido']} desde la lista de espera")


def proceso_gestionar_lista_espera():
    """Gestiona la lista de espera de un evento."""
    fc.limpiar_pantalla()
    print("=" * 60)
    print("           GESTIONAR LISTA DE ESPERA")
    print("=" * 60)
    
    id_evento = fc.solicitar_id_evento()
    
    if not fc.existe_evento(id_evento):
        fc.mostrar_error("Evento no encontrado")
        fc.pausar()
        return
    
    if not fc.hay_participantes_en_espera(id_evento):
        fc.mostrar_mensaje("No hay participantes en lista de espera")
        fc.pausar()
        return
    
    evento = fc.obtener_info_evento(id_evento)
    print(f"\n--- LISTA DE ESPERA: {evento['nombre']} ---")
    
    conn = fc.conectar_bd()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM lista_espera 
        WHERE id_evento = ? 
        ORDER BY posicion ASC
    ''', (id_evento,))
    lista = cursor.fetchall()
    conn.close()
    
    for registro in lista:
        participante = fc.obtener_info_participante(registro['id_participante'])
        print(f"{registro['posicion']}. {participante['nombre']} {participante['apellido']} - {participante['documento']}")
    
    print("\n1. Promover un participante")
    print("2. Eliminar un participante")
    
    opcion = input("\nSeleccione una opción: ").strip()
    
    if opcion == '1':
        if fc.hay_cupos_disponibles(id_evento):
            try:
                posicion = int(input("Ingrese la posición del participante a promover: "))
                
                conn = fc.conectar_bd()
                cursor = conn.cursor()
                cursor.execute('''
                    SELECT * FROM lista_espera 
                    WHERE id_evento = ? AND posicion = ?
                ''', (id_evento, posicion))
                registro = cursor.fetchone()
                
                if registro:
                    id_participante = registro['id_participante']
                    
                    inscripcion = {
                        'id_evento': id_evento,
                        'id_participante': id_participante,
                        'fecha_inscripcion': date.today(),
                        'estado': 'confirmada',
                        'estado_pago': 'pendiente'
                    }
                    
                    id_inscripcion = fc.guardar_inscripcion(inscripcion)
                    
                    cursor.execute('DELETE FROM lista_espera WHERE id = ?', (registro['id'],))
                    cursor.execute('''
                        UPDATE lista_espera 
                        SET posicion = posicion - 1 
                        WHERE id_evento = ? AND posicion > ?
                    ''', (id_evento, posicion))
                    
                    conn.commit()
                    fc.mostrar_exito(f"Participante promovido exitosamente. ID inscripción: {id_inscripcion}")
                else:
                    fc.mostrar_error("Posición no válida")
                
                conn.close()
            except ValueError:
                fc.mostrar_error("Por favor ingrese un número válido")
        else:
            fc.mostrar_error("No hay cupos disponibles para promover")
    
    elif opcion == '2':
        try:
            posicion = int(input("Ingrese la posición del participante a eliminar: "))
            
            conn = fc.conectar_bd()
            cursor = conn.cursor()
            cursor.execute('''
                SELECT * FROM lista_espera 
                WHERE id_evento = ? AND posicion = ?
            ''', (id_evento, posicion))
            registro = cursor.fetchone()
            
            if registro:
                participante = fc.obtener_info_participante(registro['id_participante'])
                
                if fc.usuario_confirma_operacion(f"¿Confirma eliminar a {participante['nombre']} {participante['apellido']}?"):
                    cursor.execute('DELETE FROM lista_espera WHERE id = ?', (registro['id'],))
                    cursor.execute('''
                        UPDATE lista_espera 
                        SET posicion = posicion - 1 
                        WHERE id_evento = ? AND posicion > ?
                    ''', (id_evento, posicion))
                    conn.commit()
                    fc.mostrar_exito("Participante eliminado de la lista de espera")
                else:
                    fc.mostrar_mensaje("Operación cancelada")
            else:
                fc.mostrar_error("Posición no válida")
            
            conn.close()
        except ValueError:
            fc.mostrar_error("Por favor ingrese un número válido")
    
    fc.pausar()
