import os 
import modules.menus as m 
import modules.corefiles as c

def reportes(campus):
    os.system('cls')
    n = m.MenuReportes()
    if (n == 1):
        ActivosList(campus)
    elif (n == 2):
        Categoria(campus)
    elif (n == 3):
        DadoBaja(campus)
    elif (n == 4):
        ListActAsg(campus)
    elif (n == 5):
        Historial(campus)
    elif (n == 6):
        pass

def ActivosList(campus):
    print("Lista de todos los activos:")
    for key, value in campus['activos'].items():
        print(f"Código: {key}, Nombre: {value['nombre']}, Estado: {value['estado']}")
    os.system('pause')

def Categoria(campus):
    categoria = input("Ingrese la categoría de los activos a listar: ")
    print(f"Lista de activos de la categoría '{categoria}':")
    for key, value in campus['activos'].items():
        if value['categoria'] == categoria:
            print(f"Código: {key}, Nombre: {value['nombre']}, Estado: {value['estado']}")
    os.system('pause')

def DadoBaja(campus):
    print("Lista de activos dados de baja por daño:")
    for key, value in campus['activos'].items():
        if value['estado'] == 'dado de baja':
            print(f"Código: {key}, Nombre: {value['nombre']}, Estado: {value['estado']}")
    os.system('pause')

def ListActAsg(campus):
    print("Lista de activos y sus asignaciones:")
    for asignacion in campus['asignaciones'].values():
        print(f"Número de asignación: {asignacion['nro asignacion']}")
        print("Activos asignados:")
        for activo in asignacion['activos']:
            activo_info = campus['activos'][activo]
            print(f"Código: {activo}, Nombre: {activo_info['nombre']}, Estado: {activo_info['estado']}")
        print()
    os.system('pause')

def Historial(campus):
    codigo_activo = input("Ingrese el código del activo para ver su historial de movimientos: ")
    if codigo_activo in campus['activos']:
        activo = campus['activos'][codigo_activo]
        print(f"Historial de movimientos del activo '{activo['nombre']}':")
        for movimiento in activo['historial'].values():
            print(f"Fecha: {movimiento['fecha']}, Tipo de movimiento: {movimiento['tipoMov']}, Responsable: {movimiento['responsable']}")
    else:
        print("Activo no encontrado.")
    os.system('pause')
