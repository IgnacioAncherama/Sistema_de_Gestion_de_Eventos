"""
Sistema de Gestión de Eventos
Main - Punto de entrada principal del sistema

Este programa conecta todos los módulos del sistema de gestión de eventos.
Desarrollado por: Equipo 5
"""

import funciones_comunes as fc
import gestion_eventos
import inscripciones
import pagos
import realizacion_evento
import informes
import gestion_actividades


def mostrar_menu_principal():
    """Muestra el menú principal del sistema."""
    fc.limpiar_pantalla()
    print("=" * 70)
    print("                   SISTEMA DE GESTIÓN DE EVENTOS")
    print("                            EQUIPO 5")
    print("=" * 70)
    print("E. Módulo Gestión de Eventos")
    print("I. Módulo Registro e Inscripciones")
    print("P. Módulo Administración de Pagos")
    print("R. Módulo Realización del Evento")
    print("A. Módulo Gestión de Actividades")
    print("F. Módulo Generación de Informes")
    print("S. Salir del sistema")
    print("=" * 70)


def main():
    """Función principal del sistema."""
    print("\n" + "=" * 70)
    print("    Bienvenido al Sistema de Gestión de Eventos - Equipo 5")
    print("=" * 70)
    print("\nEquipo de Desarrollo:")
    print("  • Gestión de Eventos: Ignacio Ancherama")
    print("  • Inscripciones: Sebastian Stefanelli")
    print("  • Pagos: Joaquin Landra")
    print("  • Realización: Julian Vazquez")
    print("  • Informes: Milagros Trotta")
    print("=" * 70)
    
    fc.pausar()
    
    while True:
        mostrar_menu_principal()
        opcion = input("\nSeleccione una opción: ").upper().strip()
        
        if opcion == 'E':
            fc.mostrar_mensaje("Accediendo a Gestión de Eventos...")
            fc.pausar()
            gestion_eventos.menu_principal_eventos()
        
        elif opcion == 'I':
            fc.mostrar_mensaje("Accediendo a Registro e Inscripciones...")
            fc.pausar()
            inscripciones.menu_principal_inscripciones()
        
        elif opcion == 'P':
            fc.mostrar_mensaje("Accediendo a Administración de Pagos...")
            fc.pausar()
            pagos.menu_principal_pagos()
        
        elif opcion == 'R':
            fc.mostrar_mensaje("Accediendo a Realización del Evento...")
            fc.pausar()
            realizacion_evento.menu_principal_realizacion()
        
        elif opcion == 'A':
            fc.mostrar_mensaje("Accediendo a Gestión de Actividades...")
            fc.pausar()
            gestion_actividades.menu_principal_actividades()
        
        elif opcion == 'F':
            fc.mostrar_mensaje("Accediendo a Generación de Informes...")
            fc.pausar()
            informes.menu_principal_informes()
        
        elif opcion == 'S':
            conn = fc.conectar_bd()
            cursor = conn.cursor()
            
            cursor.execute('SELECT COUNT(*) as total FROM eventos')
            total_eventos = cursor.fetchone()['total']
            
            cursor.execute('SELECT COUNT(*) as total FROM participantes')
            total_participantes = cursor.fetchone()['total']
            
            cursor.execute('SELECT COUNT(*) as total FROM inscripciones')
            total_inscripciones = cursor.fetchone()['total']
            
            cursor.execute('SELECT COUNT(*) as total FROM pagos')
            total_pagos = cursor.fetchone()['total']
            
            conn.close()
            
            print("\n" + "=" * 70)
            print("         Gracias por usar el Sistema de Gestión de Eventos")
            print("=" * 70)
            print("\nEstadísticas del sistema:")
            print(f"  • Eventos registrados: {total_eventos}")
            print(f"  • Participantes registrados: {total_participantes}")
            print(f"  • Inscripciones totales: {total_inscripciones}")
            print(f"  • Pagos procesados: {total_pagos}")
            print("\n¡Hasta pronto!\n")
            break
        
        else:
            fc.mostrar_error("Opción no válida. Por favor, intente nuevamente.")
            fc.pausar()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n  Sistema interrumpido por el usuario")
        print("¡Hasta pronto!\n")
    except Exception as e:
        print(f"\n Error inesperado: {e}")
        print("Por favor, contacte al soporte técnico.\n")
