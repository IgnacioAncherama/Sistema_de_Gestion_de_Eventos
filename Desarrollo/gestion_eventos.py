"""
Módulo de Gestión de Eventos
Sistema de Gestión de Eventos

Este módulo maneja la creación, consulta, modificación y eliminación de eventos.
"""

from datetime import date, datetime
import funciones_comunes as fc


def menu_principal_eventos():
    """Muestra el menú principal de gestión de eventos."""
    while True:
        fc.limpiar_pantalla()
        print("=" * 60)
        print("           MENÚ GESTIÓN DE EVENTOS")
        print("=" * 60)
        print("C. Crear un evento")
        print("M. Consultar eventos")
        print("X. Modificar un evento")
        print("E. Eliminar un evento")
        print("S. Salir del módulo")
        print("=" * 60)
        
        opcion = input("\nSeleccione una opción: ").upper().strip()
        
        if opcion == 'C':
            crear_evento()
        elif opcion == 'M':
            consultar_eventos()
        elif opcion == 'X':
            modificar_evento()
        elif opcion == 'E':
            eliminar_evento()
        elif opcion == 'S':
            fc.mostrar_mensaje("Saliendo del módulo de gestión de eventos...")
            break
        else:
            fc.mostrar_error("Opción no válida. Intente nuevamente.")
            fc.pausar()


def crear_evento():
    """Proceso para crear un nuevo evento."""
    fc.limpiar_pantalla()
    print("=" * 60)
    print("           CREAR NUEVO EVENTO")
    print("=" * 60)
    
    nombre = input("\nIngrese nombre del evento: ").strip()
    descripcion = input("Ingrese descripción del evento: ").strip()
    
    while True:
        try:
            fecha_str = input("Ingrese fecha del evento (DD/MM/AAAA): ")
            dia, mes, anio = map(int, fecha_str.split('/'))
            fecha_evento = date(anio, mes, dia)
            
            if fecha_evento <= date.today():
                fc.mostrar_error("La fecha debe ser posterior a hoy")
                continue
            break
        except ValueError:
            fc.mostrar_error("Formato de fecha inválido. Use DD/MM/AAAA")
    
    hora_inicio = input("Ingrese hora de inicio (HH:MM): ").strip()
    hora_fin = input("Ingrese hora de fin (HH:MM): ").strip()
    
    if hora_fin <= hora_inicio:
        fc.mostrar_error("La hora de fin debe ser posterior a la de inicio")
        fc.pausar()
        return
    
    ubicacion = input("Ingrese ubicación del evento: ").strip()
    
    while True:
        try:
            capacidad = int(input("Ingrese capacidad máxima: "))
            if capacidad <= 0:
                fc.mostrar_error("La capacidad debe ser mayor a 0")
                continue
            break
        except ValueError:
            fc.mostrar_error("Por favor ingrese un número válido")
    
    while True:
        try:
            precio = float(input("Ingrese precio del evento: "))
            if precio < 0:
                fc.mostrar_error("El precio no puede ser negativo")
                continue
            break
        except ValueError:
            fc.mostrar_error("Por favor ingrese un número válido")
    
    evento = {
        'nombre': nombre,
        'descripcion': descripcion,
        'fecha': fecha_evento,
        'hora_inicio': hora_inicio,
        'hora_fin': hora_fin,
        'ubicacion': ubicacion,
        'capacidad_maxima': capacidad,
        'precio': precio,
        'estado': 'activo'
    }
    
    id_evento = fc.guardar_evento(evento)
    fc.mostrar_exito(f"Evento creado exitosamente con ID: {id_evento}")
    fc.pausar()


def consultar_eventos():
    """Proceso para consultar eventos."""
    fc.limpiar_pantalla()
    print("=" * 60)
    print("           CONSULTA DE EVENTOS")
    print("=" * 60)
    print("T. Ver todos los eventos")
    print("I. Buscar por ID")
    print("N. Buscar por nombre")
    print("F. Buscar por fecha")
    print("S. Volver")
    print("=" * 60)
    
    opcion = input("\nSeleccione una opción: ").upper().strip()
    
    if opcion == 'T':
        mostrar_todos_los_eventos()
    elif opcion == 'I':
        buscar_evento_por_id()
    elif opcion == 'N':
        buscar_eventos_por_nombre()
    elif opcion == 'F':
        buscar_eventos_por_fecha()
    elif opcion == 'S':
        return
    else:
        fc.mostrar_error("Opción no válida")
    
    fc.pausar()


def mostrar_todos_los_eventos():
    """Muestra todos los eventos registrados."""
    eventos = fc.obtener_todos_eventos()
    
    if not eventos:
        fc.mostrar_mensaje("No hay eventos registrados")
        return
    
    print("\n" + "=" * 60)
    print("           LISTA DE TODOS LOS EVENTOS")
    print("=" * 60)
    
    for evento in eventos:
        mostrar_evento_detallado(evento)


def mostrar_evento_detallado(evento: dict):
    """Muestra la información detallada de un evento."""
    print(f"\n--- Evento ID: {evento['id']} ---")
    print(f"Nombre: {evento['nombre']}")
    print(f"Descripción: {evento['descripcion']}")
    print(f"Fecha: {fc.formatear_fecha(evento['fecha'])}")
    print(f"Horario: {evento['hora_inicio']} - {evento['hora_fin']}")
    print(f"Ubicación: {evento['ubicacion']}")
    print(f"Capacidad: {evento['capacidad_maxima']} personas")
    print(f"Precio: {fc.formatear_precio(evento['precio'])}")
    print(f"Estado: {evento['estado']}")
    cupos = fc.obtener_cupos_disponibles(evento['id'])
    print(f"Cupos disponibles: {cupos}")
    print("-" * 60)


def buscar_evento_por_id():
    """Busca y muestra un evento por su ID."""
    id_evento = fc.solicitar_id_evento()
    
    if not fc.existe_evento(id_evento):
        fc.mostrar_error("Evento no encontrado")
        return
    
    evento = fc.obtener_info_evento(id_evento)
    mostrar_evento_detallado(evento)


def buscar_eventos_por_nombre():
    """Busca eventos que contengan el nombre especificado."""
    nombre = input("Ingrese nombre del evento a buscar: ").strip()
    
    conn = fc.conectar_bd()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM eventos WHERE nombre LIKE ? ORDER BY fecha DESC
    ''', (f'%{nombre}%',))
    eventos = cursor.fetchall()
    conn.close()
    
    if not eventos:
        fc.mostrar_mensaje("No se encontraron eventos con ese nombre")
        return
    
    print(f"\nSe encontraron {len(eventos)} evento(s):")
    for evento in eventos:
        mostrar_evento_detallado(dict(evento))


def buscar_eventos_por_fecha():
    """Busca eventos en una fecha específica."""
    while True:
        try:
            fecha_str = input("Ingrese fecha (DD/MM/AAAA): ")
            dia, mes, anio = map(int, fecha_str.split('/'))
            fecha_busqueda = date(anio, mes, dia)
            break
        except ValueError:
            fc.mostrar_error("Formato de fecha inválido. Use DD/MM/AAAA")
            return
    
    fecha_bd = fecha_busqueda.strftime('%Y-%m-%d')
    
    conn = fc.conectar_bd()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM eventos WHERE fecha = ?', (fecha_bd,))
    eventos = cursor.fetchall()
    conn.close()
    
    if not eventos:
        fc.mostrar_mensaje("No se encontraron eventos en esa fecha")
        return
    
    print(f"\nSe encontraron {len(eventos)} evento(s):")
    for evento in eventos:
        mostrar_evento_detallado(dict(evento))


def modificar_evento():
    """Proceso para modificar un evento existente."""
    fc.limpiar_pantalla()
    print("=" * 60)
    print("           MODIFICAR EVENTO")
    print("=" * 60)
    
    id_evento = fc.solicitar_id_evento()
    
    if not fc.existe_evento(id_evento):
        fc.mostrar_error("Evento no encontrado")
        fc.pausar()
        return
    
    evento = fc.obtener_info_evento(id_evento)
    
    print("\nInformación actual del evento:")
    mostrar_evento_detallado(evento)
    
    print("\n¿Qué desea modificar?")
    print("N. Nombre")
    print("F. Fecha")
    print("U. Ubicación")
    print("C. Capacidad")
    print("P. Precio")
    
    opcion = input("\nSeleccione una opción: ").upper().strip()
    
    conn = fc.conectar_bd()
    cursor = conn.cursor()
    
    if opcion == 'N':
        nuevo_nombre = input("Ingrese el nuevo nombre: ").strip()
        if nuevo_nombre:
            cursor.execute('UPDATE eventos SET nombre = ? WHERE id = ?', (nuevo_nombre, id_evento))
            conn.commit()
            fc.mostrar_exito("Evento modificado exitosamente")
        else:
            fc.mostrar_error("El nombre no puede estar vacío")
    
    elif opcion == 'F':
        try:
            fecha_str = input("Ingrese la nueva fecha (DD/MM/AAAA): ")
            dia, mes, anio = map(int, fecha_str.split('/'))
            nueva_fecha = date(anio, mes, dia)
            
            if nueva_fecha > date.today():
                fecha_bd = nueva_fecha.strftime('%Y-%m-%d')
                cursor.execute('UPDATE eventos SET fecha = ? WHERE id = ?', (fecha_bd, id_evento))
                conn.commit()
                fc.mostrar_exito("Evento modificado exitosamente")
            else:
                fc.mostrar_error("La fecha debe ser posterior a hoy")
        except ValueError:
            fc.mostrar_error("Formato de fecha inválido")
    
    elif opcion == 'U':
        nueva_ubicacion = input("Ingrese la nueva ubicación: ").strip()
        cursor.execute('UPDATE eventos SET ubicacion = ? WHERE id = ?', (nueva_ubicacion, id_evento))
        conn.commit()
        fc.mostrar_exito("Evento modificado exitosamente")
    
    elif opcion == 'C':
        try:
            nueva_capacidad = int(input("Ingrese la nueva capacidad: "))
            if nueva_capacidad > 0:
                cursor.execute('UPDATE eventos SET capacidad_maxima = ? WHERE id = ?', (nueva_capacidad, id_evento))
                conn.commit()
                fc.mostrar_exito("Evento modificado exitosamente")
            else:
                fc.mostrar_error("La capacidad debe ser mayor a cero")
        except ValueError:
            fc.mostrar_error("Por favor ingrese un número válido")
    
    elif opcion == 'P':
        try:
            nuevo_precio = float(input("Ingrese el nuevo precio: "))
            if nuevo_precio >= 0:
                cursor.execute('UPDATE eventos SET precio = ? WHERE id = ?', (nuevo_precio, id_evento))
                conn.commit()
                fc.mostrar_exito("Evento modificado exitosamente")
            else:
                fc.mostrar_error("El precio no puede ser negativo")
        except ValueError:
            fc.mostrar_error("Por favor ingrese un número válido")
    
    else:
        fc.mostrar_error("Opción de modificación no válida")
    
    conn.close()
    fc.pausar()


def eliminar_evento():
    """Proceso para eliminar un evento."""
    fc.limpiar_pantalla()
    print("=" * 60)
    print("           ELIMINAR EVENTO")
    print("=" * 60)
    
    id_evento = fc.solicitar_id_evento()
    
    if not fc.existe_evento(id_evento):
        fc.mostrar_error("Evento no encontrado")
        fc.pausar()
        return
    
    # Verificar si hay inscripciones
    conn = fc.conectar_bd()
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) as total FROM inscripciones WHERE id_evento = ?', (id_evento,))
    resultado = cursor.fetchone()
    
    if resultado['total'] > 0:
        conn.close()
        fc.mostrar_error("No se puede eliminar. Hay inscripciones asociadas")
        fc.pausar()
        return
    
    evento = fc.obtener_info_evento(id_evento)
    print(f"\nEvento a eliminar: {evento['nombre']}")
    
    if fc.usuario_confirma_operacion("¿Está seguro que desea eliminar este evento?"):
        cursor.execute('DELETE FROM eventos WHERE id = ?', (id_evento,))
        conn.commit()
        fc.mostrar_exito("Evento eliminado exitosamente")
    else:
        fc.mostrar_mensaje("Operación cancelada")
    
    conn.close()
    fc.pausar()
