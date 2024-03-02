import os
import modules.menus as m
import modules.corefiles as c
import modules.asignaciones as asg
def Movimientos(activos:dict,personas:dict,asignaciones:dict):
    os.system('cls')
    n = m.MenuMovs()
    if (n == 1):
        os.system('cls')
        ReturnAct(activos,asignaciones,personas)
    elif (n == 2):
        os.system('cls')
        BajaAct(activos,personas)     
    elif (n == 3):
        os.system('cls')
        pass
    elif (n == 4):
        os.system('cls')
        RepairAct(activos,personas)  
    elif (n == 5):
        pass

def ReturnAct(activos:dict,asignaciones:dict,personas:dict):
    os.system('cls')
    print('Ingrese la fecha de devolución')
    date = c.ValidStr()
    print('Ingrese el id de quién va a realizar la devolución')
    respons = c.ValidStr()
    IsValid = asg.verifyPerm(personas,respons)
    if (IsValid == True):
        print('Ingrese el código campus del activo que quiere devolver')
        code = c.ValidataCode(activos)
        if (bool(code) == True):
            route = activos.get(code)
            if (route['estado'] == 'en reparacion'):
                print('Un activo en reparación no se puede desasignar del responsable')
                os.system('pause')
            else:
                route['estado'] = 'no asignado'
                for keys, values in asignaciones.items():
                    for item in values['activos']:
                        if (code == item):
                            values['activos'].remove(item)
                asg.AddHist(activos,'devolucion',code,date,respons)
        else:
            pass
    else:
        pass

def BajaAct(activos:dict,personas:dict):
    os.system('cls')
    print('Ingrese la fecha en que el activo será dado de baja')
    date = c.ValidStr()
    print('Ingrese el id de quién va a realizar el movimiento')
    respons = c.ValidStr()
    IsValid = asg.verifyPerm(personas,respons)
    if (IsValid == True):
        print('Ingrese el código campus del activo que quiere dar de baja')
        code = c.ValidataCode(activos)
        if (bool(code) == True):
            route = activos.get(code)
            route['estado'] = 'dado de baja'
            asg.AddHist(activos,'dado de baja',code,date,respons)
        else:
            pass
    else:
        pass

def RepairAct(activos:dict,personas:dict):
    os.system('cls')
    print('Ingrese la fecha en que el activo será mandado a reparación')
    date = c.ValidStr()
    print('Ingrese el id de quién va a realizar el movimiento')
    respons = c.ValidStr()
    IsValid = asg.verifyPerm(personas,respons)
    if (IsValid == True):
        print('Ingrese el código campus del activo que quiere enviar a reparación')
        code = c.ValidataCode(activos)
        if (bool(code) == True):
            route = activos.get(code)
            route['estado'] = 'en reparacion'
            asg.AddHist(activos,'en reparacion',code,date,respons)
        else:
            pass
    else:
        pass

def ChangeAsign(activos:dict,personas:dict,zonas:dict,asignaciones:dict):
    os.system('cls')
    print('Ingrese la fecha en que el activo será reasignado')
    date = c.ValidStr()
    print('Ingrese el id de quién va a realizar el movimiento')
    respons = c.ValidStr()
    IsValid = asg.verifyPerm(personas,respons)
    if (IsValid == True):
        pass
    else:
        pass