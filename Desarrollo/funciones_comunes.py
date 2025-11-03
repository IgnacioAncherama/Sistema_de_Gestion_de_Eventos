"""
Módulo de Funciones Comunes
Sistema de Gestión de Eventos

Este módulo contiene funciones compartidas utilizadas por todos los módulos del sistema.
Utiliza SQLite para persistencia de datos.
"""

import sqlite3
from datetime import datetime, date
from typing import Optional, Dict, Any, List


# CONFIGURACIÓN DE BASE DE DATOS


DB_NAME = 'gestion_eventos.db'


def conectar_bd():
    """Conecta a la base de datos SQLite."""
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def inicializar_bd():
    """Crea las tablas de la base de datos si no existen."""
    conn = conectar_bd()
    cursor = conn.cursor()
    
    # Tabla de eventos
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS eventos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            descripcion TEXT,
            fecha DATE NOT NULL,
            hora_inicio TEXT NOT NULL,
            hora_fin TEXT NOT NULL,
            ubicacion TEXT NOT NULL,
            capacidad_maxima INTEGER NOT NULL,
            precio REAL NOT NULL,
            estado TEXT DEFAULT 'activo'
        )
    ''')
    
    # Tabla de participantes
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS participantes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            apellido TEXT NOT NULL,
            documento TEXT UNIQUE NOT NULL,
            email TEXT NOT NULL,
            telefono TEXT NOT NULL,
            fecha_nacimiento DATE NOT NULL,
            genero TEXT NOT NULL,
            pais TEXT NOT NULL,
            profesion TEXT NOT NULL
        )
    ''')
    
    # Tabla de inscripciones
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS inscripciones (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_evento INTEGER NOT NULL,
            id_participante INTEGER NOT NULL,
            fecha_inscripcion DATE NOT NULL,
            estado TEXT DEFAULT 'confirmada',
            estado_pago TEXT DEFAULT 'pendiente',
            FOREIGN KEY (id_evento) REFERENCES eventos(id),
            FOREIGN KEY (id_participante) REFERENCES participantes(id)
        )
    ''')
    
    # Tabla de pagos
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pagos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_inscripcion INTEGER NOT NULL,
            monto REAL NOT NULL,
            metodo_pago TEXT NOT NULL,
            fecha_pago DATE NOT NULL,
            estado TEXT DEFAULT 'confirmado',
            concepto TEXT,
            numero_comprobante TEXT,
            observaciones TEXT,
            FOREIGN KEY (id_inscripcion) REFERENCES inscripciones(id)
        )
    ''')
    
    # Tabla de reembolsos
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS reembolsos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_inscripcion INTEGER NOT NULL,
            monto REAL NOT NULL,
            fecha_reembolso DATE NOT NULL,
            FOREIGN KEY (id_inscripcion) REFERENCES inscripciones(id)
        )
    ''')
    
    # Tabla de lista de espera
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS lista_espera (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_evento INTEGER NOT NULL,
            id_participante INTEGER NOT NULL,
            posicion INTEGER NOT NULL,
            fecha_registro DATE NOT NULL,
            FOREIGN KEY (id_evento) REFERENCES eventos(id),
            FOREIGN KEY (id_participante) REFERENCES participantes(id)
        )
    ''')
    
    # Tabla de asistencia
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS asistencia (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_inscripcion INTEGER NOT NULL,
            id_actividad INTEGER,
            fecha_hora_llegada DATETIME NOT NULL,
            presente INTEGER DEFAULT 1,
            observaciones TEXT,
            FOREIGN KEY (id_inscripcion) REFERENCES inscripciones(id),
            FOREIGN KEY (id_actividad) REFERENCES actividades(id)
        )
    ''')
    
    # Tabla de actividades
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS actividades (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_evento INTEGER NOT NULL,
            nombre TEXT NOT NULL,
            descripcion TEXT,
            hora_inicio TEXT,
            hora_fin TEXT,
            ubicacion_especifica TEXT,
            capacidad INTEGER,
            FOREIGN KEY (id_evento) REFERENCES eventos(id)
        )
    ''')
    
    # Tabla de recursos
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS recursos_eventos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_evento INTEGER NOT NULL,
            tipo TEXT NOT NULL,
            nombre TEXT,
            cantidad TEXT,
            descripcion TEXT,
            fecha_registro DATETIME NOT NULL,
            FOREIGN KEY (id_evento) REFERENCES eventos(id)
        )
    ''')
    
    conn.commit()
    conn.close()


# 1. FUNCIONES DE VALIDACIÓN


def existe_evento(id_evento: int) -> bool:
    """Verifica si un evento existe en la base de datos."""
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute('SELECT id FROM eventos WHERE id = ?', (id_evento,))
    resultado = cursor.fetchone()
    conn.close()
    return resultado is not None


def existe_participante(documento: str) -> bool:
    """Verifica si un participante existe en la base de datos."""
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute('SELECT id FROM participantes WHERE documento = ?', (documento,))
    resultado = cursor.fetchone()
    conn.close()
    return resultado is not None


def existe_inscripcion(id_inscripcion: int) -> bool:
    """Verifica si una inscripción existe en la base de datos."""
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute('SELECT id FROM inscripciones WHERE id = ?', (id_inscripcion,))
    resultado = cursor.fetchone()
    conn.close()
    return resultado is not None


def validar_evento_activo(id_evento: int) -> bool:
    """
    Valida que el evento existe, está activo y es futuro.
    Se usa para: inscripciones, modificaciones.
    """
    if not existe_evento(id_evento):
        mostrar_error("Evento no encontrado.")
        return False
    
    info_evento = obtener_info_evento(id_evento)
    
    if info_evento['estado'] != 'activo':
        mostrar_error("El evento no está disponible para inscripciones.")
        return False
    
    fecha_evento = datetime.strptime(info_evento['fecha'], '%Y-%m-%d').date()
    if fecha_evento < date.today():
        mostrar_error("Este evento ya se ha realizado.")
        return False
    
    return True


def validar_evento_finalizado(id_evento: int) -> bool:
    """
    Valida que el evento existe y ya finalizó.
    Se usa para: generación de informes.
    """
    if not existe_evento(id_evento):
        mostrar_error("Evento no encontrado.")
        return False
    
    info_evento = obtener_info_evento(id_evento)
    fecha_evento = datetime.strptime(info_evento['fecha'], '%Y-%m-%d').date()
    
    if fecha_evento > date.today():
        mostrar_error("El informe solo puede generarse para eventos que ya han finalizado.")
        return False
    
    return True


def validar_inscripcion_para_cancelacion(id_inscripcion: int) -> bool:
    """Valida que la inscripción existe y el evento no ha pasado."""
    if not existe_inscripcion(id_inscripcion):
        mostrar_error("Inscripción no encontrada.")
        return False
    
    id_evento = obtener_evento_de_inscripcion(id_inscripcion)
    info_evento = obtener_info_evento(id_evento)
    fecha_evento = datetime.strptime(info_evento['fecha'], '%Y-%m-%d').date()
    
    if fecha_evento < date.today():
        mostrar_error("No se puede cancelar. El evento ya se realizó.")
        return False
    
    return True



# 2. FUNCIONES DE SOLICITUD DE DATOS


def solicitar_id_evento() -> int:
    """Solicita al usuario el ID de un evento."""
    while True:
        try:
            id_evento = int(input("Ingrese el ID del evento: "))
            return id_evento
        except ValueError:
            mostrar_error("Por favor ingrese un número válido.")


def solicitar_documento_participante() -> str:
    """Solicita al usuario el documento de un participante."""
    documento = input("Ingrese el documento del participante: ").strip()
    return documento


def solicitar_id_inscripcion() -> int:
    """Solicita al usuario el ID de una inscripción."""
    while True:
        try:
            id_inscripcion = int(input("Ingrese el ID de la inscripción: "))
            return id_inscripcion
        except ValueError:
            mostrar_error("Por favor ingrese un número válido.")



# 3. FUNCIONES DE OBTENCIÓN DE INFORMACIÓN


def obtener_info_evento(id_evento: int) -> Optional[Dict[str, Any]]:
    """Retorna un diccionario con toda la información del evento."""
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM eventos WHERE id = ?', (id_evento,))
    fila = cursor.fetchone()
    conn.close()
    
    if fila:
        return dict(fila)
    return None


def obtener_info_participante(id_participante: int) -> Optional[Dict[str, Any]]:
    """Retorna un diccionario con toda la información del participante."""
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM participantes WHERE id = ?', (id_participante,))
    fila = cursor.fetchone()
    conn.close()
    
    if fila:
        return dict(fila)
    return None


def obtener_info_inscripcion(id_inscripcion: int) -> Optional[Dict[str, Any]]:
    """Retorna un diccionario con toda la información de la inscripción."""
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM inscripciones WHERE id = ?', (id_inscripcion,))
    fila = cursor.fetchone()
    conn.close()
    
    if fila:
        return dict(fila)
    return None


def obtener_evento_de_inscripcion(id_inscripcion: int) -> int:
    """Retorna el ID del evento asociado a una inscripción."""
    info_inscripcion = obtener_info_inscripcion(id_inscripcion)
    return info_inscripcion['id_evento'] if info_inscripcion else 0


def obtener_id_participante(documento: str) -> int:
    """Retorna el ID del participante a partir de su documento."""
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute('SELECT id FROM participantes WHERE documento = ?', (documento,))
    fila = cursor.fetchone()
    conn.close()
    
    return fila['id'] if fila else 0



# 4. FUNCIONES DE INTERACCIÓN CON USUARIO

def usuario_confirma_operacion(mensaje: str) -> bool:
    """Solicita confirmación del usuario para una operación."""
    while True:
        respuesta = input(f"{mensaje} (S/N): ").strip().upper()
        if respuesta in ['S', 'N']:
            return respuesta == 'S'
        mostrar_error("Por favor ingrese S o N.")


def mostrar_error(mensaje: str):
    """Muestra un mensaje de error en pantalla."""
    print(f"\n ERROR: {mensaje}\n")


def mostrar_exito(mensaje: str):
    """Muestra un mensaje de éxito en pantalla."""
    print(f"\n ÉXITO: {mensaje}\n")


def mostrar_mensaje(mensaje: str):
    """Muestra un mensaje informativo en pantalla."""
    print(f"\n  {mensaje}\n")


def mostrar_advertencia(mensaje: str):
    """Muestra un mensaje de advertencia en pantalla."""
    print(f"\n  ADVERTENCIA: {mensaje}\n")


def limpiar_pantalla():
    """Limpia la pantalla de la consola."""
    import os
    os.system('cls' if os.name == 'nt' else 'clear')


def pausar():
    """Pausa la ejecución hasta que el usuario presione Enter."""
    input("\nPresione Enter para continuar...")



# 5. FUNCIONES DE UTILIDAD


def hay_cupos_disponibles(id_evento: int) -> bool:
    """Verifica si el evento tiene cupos disponibles."""
    info_evento = obtener_info_evento(id_evento)
    if not info_evento:
        return False
    
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT COUNT(*) as total FROM inscripciones 
        WHERE id_evento = ? AND estado = 'confirmada'
    ''', (id_evento,))
    resultado = cursor.fetchone()
    conn.close()
    
    inscripciones_confirmadas = resultado['total']
    return inscripciones_confirmadas < info_evento['capacidad_maxima']


def participante_ya_inscrito(id_evento: int, id_participante: int) -> bool:
    """Verifica si un participante ya está inscrito en un evento."""
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT id FROM inscripciones 
        WHERE id_evento = ? AND id_participante = ? 
        AND estado IN ('confirmada', 'pendiente')
    ''', (id_evento, id_participante))
    resultado = cursor.fetchone()
    conn.close()
    
    return resultado is not None


def actualizar_estado_inscripcion(id_inscripcion: int, nuevo_estado: str):
    """Actualiza el estado de una inscripción en la base de datos."""
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE inscripciones SET estado = ? WHERE id = ?
    ''', (nuevo_estado, id_inscripcion))
    conn.commit()
    conn.close()
    mostrar_exito(f"Estado de inscripción actualizado a: {nuevo_estado}")


def obtener_cupos_disponibles(id_evento: int) -> int:
    """Retorna la cantidad de cupos disponibles en un evento."""
    info_evento = obtener_info_evento(id_evento)
    if not info_evento:
        return 0
    
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT COUNT(*) as total FROM inscripciones 
        WHERE id_evento = ? AND estado = 'confirmada'
    ''', (id_evento,))
    resultado = cursor.fetchone()
    conn.close()
    
    inscripciones_confirmadas = resultado['total']
    return info_evento['capacidad_maxima'] - inscripciones_confirmadas


def hay_participantes_en_espera(id_evento: int) -> bool:
    """Verifica si hay participantes en la lista de espera de un evento."""
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) as total FROM lista_espera WHERE id_evento = ?', (id_evento,))
    resultado = cursor.fetchone()
    conn.close()
    
    return resultado['total'] > 0


def actualizar_estado_pago_inscripcion(id_inscripcion: int, estado: str):
    """Actualiza el estado de pago de una inscripción."""
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE inscripciones SET estado_pago = ? WHERE id = ?
    ''', (estado, id_inscripcion))
    conn.commit()
    conn.close()



# 6. FUNCIONES DE OPERACIONES CON BD


def guardar_evento(evento: Dict[str, Any]) -> int:
    """Guarda un evento en la base de datos y retorna su ID."""
    conn = conectar_bd()
    cursor = conn.cursor()
    
    fecha_str = evento['fecha'].strftime('%Y-%m-%d') if isinstance(evento['fecha'], date) else evento['fecha']
    
    cursor.execute('''
        INSERT INTO eventos (nombre, descripcion, fecha, hora_inicio, hora_fin, 
                            ubicacion, capacidad_maxima, precio, estado)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (evento['nombre'], evento['descripcion'], fecha_str, evento['hora_inicio'],
          evento['hora_fin'], evento['ubicacion'], evento['capacidad_maxima'],
          evento['precio'], evento.get('estado', 'activo')))
    
    id_evento = cursor.lastrowid
    conn.commit()
    conn.close()
    return id_evento


def guardar_participante(participante: Dict[str, Any]) -> int:
    """Guarda un participante en la base de datos y retorna su ID."""
    conn = conectar_bd()
    cursor = conn.cursor()
    
    fecha_nacimiento = participante.get('fecha_nacimiento')
    if isinstance(fecha_nacimiento, date):
        fecha_nacimiento = fecha_nacimiento.strftime('%Y-%m-%d')
    
    cursor.execute('''
        INSERT INTO participantes (nombre, apellido, documento, email, telefono, 
                                  fecha_nacimiento, genero, pais, profesion)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (participante['nombre'], participante['apellido'], participante['documento'],
          participante['email'], participante['telefono'], fecha_nacimiento,
          participante['genero'], participante['pais'], participante['profesion']))
    
    id_participante = cursor.lastrowid
    conn.commit()
    conn.close()
    return id_participante


def guardar_inscripcion(inscripcion: Dict[str, Any]) -> int:
    """Guarda una inscripción en la base de datos y retorna su ID."""
    conn = conectar_bd()
    cursor = conn.cursor()
    
    fecha_str = inscripcion['fecha_inscripcion'].strftime('%Y-%m-%d') if isinstance(inscripcion['fecha_inscripcion'], date) else inscripcion['fecha_inscripcion']
    
    cursor.execute('''
        INSERT INTO inscripciones (id_evento, id_participante, fecha_inscripcion, estado, estado_pago)
        VALUES (?, ?, ?, ?, ?)
    ''', (inscripcion['id_evento'], inscripcion['id_participante'], fecha_str,
          inscripcion.get('estado', 'confirmada'), inscripcion.get('estado_pago', 'pendiente')))
    
    id_inscripcion = cursor.lastrowid
    conn.commit()
    conn.close()
    return id_inscripcion


def guardar_pago(pago: Dict[str, Any]) -> int:
    """Guarda un pago en la base de datos y retorna su ID."""
    conn = conectar_bd()
    cursor = conn.cursor()
    
    fecha_str = pago['fecha_pago'].strftime('%Y-%m-%d') if isinstance(pago['fecha_pago'], date) else pago['fecha_pago']
    
    cursor.execute('''
        INSERT INTO pagos (id_inscripcion, monto, metodo_pago, fecha_pago, 
                          estado, concepto, numero_comprobante, observaciones)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (pago['id_inscripcion'], pago['monto'], pago['metodo_pago'], fecha_str,
          pago['estado'], pago['concepto'], 
          pago['numero_comprobante'], pago['observaciones']))
    
    id_pago = cursor.lastrowid
    conn.commit()
    conn.close()
    return id_pago


def obtener_todos_eventos() -> List[Dict[str, Any]]:
    """Retorna todos los eventos de la base de datos."""
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM eventos ORDER BY fecha DESC')
    filas = cursor.fetchall()
    conn.close()
    
    return [dict(fila) for fila in filas]


def obtener_todos_participantes() -> List[Dict[str, Any]]:
    """Retorna todos los participantes de la base de datos."""
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM participantes ORDER BY apellido, nombre')
    filas = cursor.fetchall()
    conn.close()
    
    return [dict(fila) for fila in filas]


def obtener_todas_inscripciones() -> List[Dict[str, Any]]:
    """Retorna todas las inscripciones de la base de datos."""
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM inscripciones ORDER BY fecha_inscripcion DESC')
    filas = cursor.fetchall()
    conn.close()
    
    return [dict(fila) for fila in filas]


def guardar_actividad(actividad: Dict[str, Any]) -> int:
    """Guarda una actividad en la base de datos y retorna su ID."""
    conn = conectar_bd()
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO actividades (id_evento, nombre, descripcion, hora_inicio, 
                                hora_fin, ubicacion_especifica, capacidad)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (actividad['id_evento'], actividad['nombre'], actividad['descripcion'],
          actividad['hora_inicio'], actividad['hora_fin'], 
          actividad['ubicacion_especifica'], actividad['capacidad']))
    
    id_actividad = cursor.lastrowid
    conn.commit()
    conn.close()
    return id_actividad


def obtener_actividades_evento(id_evento: int) -> List[Dict[str, Any]]:
    """Retorna todas las actividades de un evento."""
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM actividades WHERE id_evento = ? ORDER BY hora_inicio', (id_evento,))
    filas = cursor.fetchall()
    conn.close()
    
    return [dict(fila) for fila in filas]


def existe_actividad(id_actividad: int) -> bool:
    """Verifica si una actividad existe en la base de datos."""
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute('SELECT id FROM actividades WHERE id = ?', (id_actividad,))
    resultado = cursor.fetchone()
    conn.close()
    return resultado is not None


def obtener_info_actividad(id_actividad: int) -> Optional[Dict[str, Any]]:
    """Retorna un diccionario con toda la información de la actividad."""
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM actividades WHERE id = ?', (id_actividad,))
    fila = cursor.fetchone()
    conn.close()
    
    if fila:
        return dict(fila)
    return None



# 7. FUNCIONES DE FORMATEO


def formatear_fecha(fecha) -> str:
    """Formatea una fecha para mostrarla."""
    if isinstance(fecha, str):
        try:
            fecha = datetime.strptime(fecha, '%Y-%m-%d').date()
        except:
            return fecha
    
    if isinstance(fecha, date):
        return fecha.strftime("%d/%m/%Y")
    
    return str(fecha)


def formatear_precio(precio: float) -> str:
    """Formatea un precio para mostrarlo."""
    return f"${precio:,.2f}"


def mostrar_separador(caracter: str = "=", longitud: int = 60):
    """Muestra un separador visual."""
    print(caracter * longitud)


# Inicializar la base de datos al importar el módulo
inicializar_bd()
