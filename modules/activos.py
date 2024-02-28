import os
import modules.menus as m
import modules.corefiles as c
def Activos(activos:dict):
    n = m.MenuControl()
    if (n == 1):
        AddActivo(activos)
    elif (n == 2):
        pass
    elif (n == 3):
        pass
    elif (n == 4):
        pass
    elif (n == 5):
        pass

def AddActivo(activos:dict):
    print('Ingrese el nombre del Activo')
    name = c.ValidStr()
    print('Ingrese el código de transacción')
    codTrans = c.validInt()