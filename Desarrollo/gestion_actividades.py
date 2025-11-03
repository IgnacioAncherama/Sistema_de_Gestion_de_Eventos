"""
Módulo de Gestión de Actividades
Sistema de Gestión de Eventos

Este módulo maneja la creación y gestión de actividades dentro de eventos.
"""

from datetime import date, datetime
import funciones_comunes as fc


def menu_principal_actividades():
    """Muestra el menú principal de gestión de actividades."""
    while True:
        fc.limpiar_pantalla()
        print("=" * 60)
        print("           MENÚ GESTIÓN DE ACTIVIDADES")
        print("=" * 60)
        print("C. Crear actividad")
        print("M. Consultar actividades")
        print("X. Modificar actividad")
        print("E. Eliminar actividad")
        print("S. Salir del módulo")
        print("=" * 60)
        
        opcion = input("\nSeleccione una opción: ").upper().strip()
        
        if opcion == 'C':
            crear_actividad()
        elif opcion == 'M':
            consultar_actividades()
        elif opcion == 'X':
            modificar_actividad()
        elif opcion == 'E':
            eliminar_actividad()
        elif opcion == 'S':
            fc.mostrar_mensaje("Saliendo del módulo de actividades...")
            break
        else:
            fc.mostrar_error("Opción no válida. Intente nuevamente.")
            fc.pausar()


def crear_actividad():
    """Crea una nueva actividad para un evento."""
    fc.limpiar_pantalla()
    print("=" * 60)
    print("           CREAR NUEVA ACTIVIDAD")
    print("=" * 60)
    
    id_evento = fc.solicitar_id_evento()
    
    if not fc.existe_evento(id_evento):
        fc.mostrar_error("Evento no encontrado")
        fc.pausar()
        return
    
    info_evento = fc.obtener_info_evento(id_evento)
    print(f"\nEvento: {info_evento['nombre']}")
    print(f"Fecha: {fc.formatear_fecha(info_evento['fecha'])}")
    
    nombre = input("\nNombre de la actividad: ").strip()
    descripcion = input("Descripción: ").strip()
    
    hora_inicio = input("Hora de inicio (HH:MM): ").strip()
    hora_fin = input("Hora de fin (HH:MM): ").strip()
    
    if hora_fin <= hora_inicio:
        fc.mostrar_error("La hora de fin debe ser posterior a la de inicio")
        fc.pausar()
        return
    
    ubicacion_especifica = input("Ubicación específica: ").strip()
    
    capacidad_input = input("Capacidad: ").strip()
    try:
        capacidad = int(capacidad_input)
        if capacidad <= 0:
            fc.mostrar_error("La capacidad debe ser mayor a 0")
            fc.pausar()
            return
    except ValueError:
        fc.mostrar_error("Capacidad inválida")
        fc.pausar()
        return
    
    # Validar campos obligatorios
    if not descripcion or not hora_inicio or not hora_fin or not ubicacion_especifica:
        fc.mostrar_error("Todos los campos son obligatorios")
        fc.pausar()
        return
    
    actividad = {
        'id_evento': id_evento,
        'nombre': nombre,
        'descripcion': descripcion,
        'hora_inicio': hora_inicio,
        'hora_fin': hora_fin,
        'ubicacion_especifica': ubicacion_especifica,
        'capacidad': capacidad
    }
    
    id_actividad = fc.guardar_actividad(actividad)
    fc.mostrar_exito(f"Actividad creada exitosamente con ID: {id_actividad}")
    fc.pausar()


def consultar_actividades():
    """Consulta actividades según diferentes criterios."""
    fc.limpiar_pantalla()
    print("=" * 60)
    print("           CONSULTA DE ACTIVIDADES")
    print("=" * 60)
    print("E. Ver por evento")
    print("T. Ver todas las actividades")
    print("S. Volver")
    print("=" * 60)
    
    opcion = input("\nSeleccione una opción: ").upper().strip()
    
    if opcion == 'E':
        consultar_por_evento()
    elif opcion == 'T':
        consultar_todas()
    elif opcion == 'S':
        return
    else:
        fc.mostrar_error("Opción no válida")
    
    fc.pausar()


def consultar_por_evento():
    """Consulta actividades de un evento específico."""
    id_evento = fc.solicitar_id_evento()
    
    if not fc.existe_evento(id_evento):
        fc.mostrar_error("Evento no encontrado")
        return
    
    info_evento = fc.obtener_info_evento(id_evento)
    print(f"\n--- ACTIVIDADES DEL EVENTO: {info_evento['nombre']} ---")
    
    actividades = fc.obtener_actividades_evento(id_evento)
    
    if not actividades:
        fc.mostrar_mensaje("No hay actividades registradas para este evento")
        return
    
    for actividad in actividades:
        mostrar_actividad_detallada(actividad)


def consultar_todas():
    """Consulta todas las actividades."""
    conn = fc.conectar_bd()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT a.*, e.nombre as evento_nombre 
        FROM actividades a
        JOIN eventos e ON a.id_evento = e.id
        ORDER BY e.fecha DESC, a.hora_inicio
    ''')
    actividades = cursor.fetchall()
    conn.close()
    
    if not actividades:
        fc.mostrar_mensaje("No hay actividades registradas")
        return
    
    print("\n--- TODAS LAS ACTIVIDADES ---")
    for actividad in actividades:
        actividad = dict(actividad)
        print(f"\n--- Actividad ID: {actividad['id']} ---")
        print(f"Evento: {actividad['evento_nombre']}")
        print(f"Nombre: {actividad['nombre']}")
        if actividad['descripcion']:
            print(f"Descripción: {actividad['descripcion']}")
        if actividad['hora_inicio']:
            print(f"Horario: {actividad['hora_inicio']} - {actividad['hora_fin']}")
        if actividad['ubicacion_especifica']:
            print(f"Ubicación: {actividad['ubicacion_especifica']}")
        if actividad['capacidad']:
            print(f"Capacidad: {actividad['capacidad']}")
        print("-" * 60)


def mostrar_actividad_detallada(actividad: dict):
    """Muestra la información detallada de una actividad."""
    print(f"\n--- Actividad ID: {actividad['id']} ---")
    print(f"Nombre: {actividad['nombre']}")
    if actividad['descripcion']:
        print(f"Descripción: {actividad['descripcion']}")
    if actividad['hora_inicio']:
        print(f"Horario: {actividad['hora_inicio']} - {actividad['hora_fin']}")
    if actividad['ubicacion_especifica']:
        print(f"Ubicación: {actividad['ubicacion_especifica']}")
    if actividad['capacidad']:
        print(f"Capacidad: {actividad['capacidad']}")
    print("-" * 60)


def modificar_actividad():
    """Modifica una actividad existente."""
    fc.limpiar_pantalla()
    print("=" * 60)
    print("           MODIFICAR ACTIVIDAD")
    print("=" * 60)
    
    id_actividad = int(input("Ingrese el ID de la actividad: "))
    
    if not fc.existe_actividad(id_actividad):
        fc.mostrar_error("Actividad no encontrada")
        fc.pausar()
        return
    
    actividad = fc.obtener_info_actividad(id_actividad)
    print("\nInformación actual de la actividad:")
    mostrar_actividad_detallada(actividad)
    
    print("\n¿Qué desea modificar?")
    print("N. Nombre")
    print("D. Descripción")
    print("H. Horario")
    print("U. Ubicación")
    print("C. Capacidad")
    
    opcion = input("\nSeleccione una opción: ").upper().strip()
    
    conn = fc.conectar_bd()
    cursor = conn.cursor()
    
    if opcion == 'N':
        nuevo_nombre = input("Ingrese el nuevo nombre: ").strip()
        if nuevo_nombre:
            cursor.execute('UPDATE actividades SET nombre = ? WHERE id = ?', (nuevo_nombre, id_actividad))
            conn.commit()
            fc.mostrar_exito("Actividad modificada exitosamente")
        else:
            fc.mostrar_error("El nombre no puede estar vacío")
    
    elif opcion == 'D':
        nueva_descripcion = input("Ingrese la nueva descripción: ").strip()
        cursor.execute('UPDATE actividades SET descripcion = ? WHERE id = ?', (nueva_descripcion, id_actividad))
        conn.commit()
        fc.mostrar_exito("Actividad modificada exitosamente")
    
    elif opcion == 'H':
        nueva_hora_inicio = input("Ingrese la nueva hora de inicio (HH:MM): ").strip()
        nueva_hora_fin = input("Ingrese la nueva hora de fin (HH:MM): ").strip()
        
        if nueva_hora_fin and nueva_hora_inicio and nueva_hora_fin <= nueva_hora_inicio:
            fc.mostrar_error("La hora de fin debe ser posterior a la de inicio")
        else:
            cursor.execute('UPDATE actividades SET hora_inicio = ?, hora_fin = ? WHERE id = ?', 
                         (nueva_hora_inicio, nueva_hora_fin, id_actividad))
            conn.commit()
            fc.mostrar_exito("Actividad modificada exitosamente")
    
    elif opcion == 'U':
        nueva_ubicacion = input("Ingrese la nueva ubicación: ").strip()
        cursor.execute('UPDATE actividades SET ubicacion_especifica = ? WHERE id = ?', (nueva_ubicacion, id_actividad))
        conn.commit()
        fc.mostrar_exito("Actividad modificada exitosamente")
    
    elif opcion == 'C':
        try:
            nueva_capacidad = int(input("Ingrese la nueva capacidad: "))
            if nueva_capacidad > 0:
                cursor.execute('UPDATE actividades SET capacidad = ? WHERE id = ?', (nueva_capacidad, id_actividad))
                conn.commit()
                fc.mostrar_exito("Actividad modificada exitosamente")
            else:
                fc.mostrar_error("La capacidad debe ser mayor a cero")
        except ValueError:
            fc.mostrar_error("Por favor ingrese un número válido")
    
    else:
        fc.mostrar_error("Opción de modificación no válida")
    
    conn.close()
    fc.pausar()


def eliminar_actividad():
    """Elimina una actividad."""
    fc.limpiar_pantalla()
    print("=" * 60)
    print("           ELIMINAR ACTIVIDAD")
    print("=" * 60)
    
    id_actividad = int(input("Ingrese el ID de la actividad: "))
    
    if not fc.existe_actividad(id_actividad):
        fc.mostrar_error("Actividad no encontrada")
        fc.pausar()
        return
    
    actividad = fc.obtener_info_actividad(id_actividad)
    print(f"\nActividad a eliminar: {actividad['nombre']}")
    
    if fc.usuario_confirma_operacion("¿Está seguro que desea eliminar esta actividad?"):
        conn = fc.conectar_bd()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM actividades WHERE id = ?', (id_actividad,))
        conn.commit()
        conn.close()
        fc.mostrar_exito("Actividad eliminada exitosamente")
    else:
        fc.mostrar_mensaje("Operación cancelada")
    
    fc.pausar()
