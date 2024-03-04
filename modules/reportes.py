import os 
import modules.menus as m 
import modules.corefiles as c

def Reportes(campus):
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
    os.system('cls')
    print("Lista de todos los activos:")
    for key, value in campus['activos'].items():
        print(f"Código: {key}, Nombre: {value['nombre']}, Estado: {value['estado']}")
    os.system('pause')

def Categoria(campus):
    os.system('cls')
    rp = True
    while rp:
        lstCat = []
        route  = campus.get('activos')
        for keys,values in route.items():
            if (values['categoria'] not in lstCat):
                lstCat.append(values['categoria'])
            else:
                pass
        for item in lstCat:
            print (f'---{item}---')
        categoria = input("Ingrese la categoría de los activos a listar: ")
        if (categoria in lstCat):
            print(f"Lista de activos de la categoría '{categoria}':")
            for key, value in campus['activos'].items():
                if value['categoria'] == categoria:
                    print(f"Código: {key}, Nombre: {value['nombre']}, Estado: {value['estado']}")
            os.system('pause')
        else: 
            rp = bool(input('No activos que cuenten con esta categoría, reintentar? S(si) - Enter(No)'))
            os.system('pause')

def DadoBaja(campus):
    os.system('cls')
    print("Lista de activos dados de baja por daño:")
    for key, value in campus['activos'].items():
        if value['estado'] == 'dado de baja':
            print(f"Código: {key}, Nombre: {value['nombre']}, Estado: {value['estado']}")
    os.system('pause')

def ListActAsg(campus):
    os.system('cls')
    print("Lista de activos y sus asignaciones:")
    print('Ingrese el número de zona o documento de quien se quiere consultar asignaciones')
    code = c.ValidStr()
    if ((code in campus['zonas']) or (code in campus['personas']['personasj']) or (code in campus['personas']['personasn'])):
        for keys,values in campus['asignaciones'].items():
            if (code in values['asignadoA']):
                print(f'Estos son los activos asignados a {code}')
                for item in values['activos']:
                    print(f'---{item}---')
        os.system('pause')
    else:
        print('el valor ingresado no existe o aun no cuenta con activos asignados')
        os.system('pause')

def Historial(campus):
    os.system('cls')
    codigo_activo = input("Ingrese el código del activo para ver su historial de movimientos: ")
    if codigo_activo in campus['activos']:
        activo = campus['activos'][codigo_activo]
        print(f"Historial de movimientos del activo '{activo['nombre']}':")
        for movimiento in activo['historial'].values():
            print(f"Fecha: {movimiento['fecha']}, Tipo de movimiento: {movimiento['tipoMov']}, Responsable: {movimiento['responsable']}")
    else:
        print("Activo no encontrado.")
    os.system('pause')
