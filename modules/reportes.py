import os 
import modules.menus as m 
import modules.corefiles as c
def reportes(campus):
    os.system('cls')
    n = m.MenuReportes()
    if (n == 1):
        ListaActivos(file='campus.json')
    elif (n == 2):
        ListaTipoActivo(campus)
    elif (n == 3):
        pass
    elif (n == 4):
        pass
    elif (n == 5):
        pass
    elif (n == 6):
        pass

def ListaActivos(file : dict):
    read = c.ReadFile(file= 'campus.json')
    for key in read['activos']:
        print(key)
    os.system('pause')

def ListaTipoActivo(campus : dict):
    print('Seleccione la clase de activo del cual quieire ver el inventario')
    for item in m.activos:
        select = m.activos[item]['tipo']
        print(select)
    os.system('pause')