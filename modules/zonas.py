import os
import modules.menus as m
import modules.corefiles as c
import json
def Zonas(zonas:dict):
    os.system('cls')
    n = m.MenuControl()
    if (n == 1):
        os.system('cls')
        AddZona(zonas)
    elif (n == 2):
        os.system('cls')
        EditZona(zonas)
    elif (n == 3):
        os.system('cls')
        DltZona(zonas)
    elif (n == 4):
        os.system('cls')
        SrchZona(zonas)
    elif (n == 5):
        pass

def AddZona(zonas:dict):
    os.system('cls')
    print('ingrese el número de la zona')
    nroZona = ValidNro(zonas)
    print('ingrese el nombre de la zona')
    name = c.ValidStr()
    print('ingrese la capacidad total de la zona')
    capacidad = c.validInt()
    nwZona = {
        'numero': nroZona,
        'nombre': name,
        'capacidad':capacidad
    }
    zonas.update({nroZona:nwZona})

def ValidNro(zonas:dict):
    num = c.ValidStr()
    if num in zonas.keys():
        print('número de zona ya existe, intente con otro')
        return ValidNro(zonas)   
    else:
        return num

def EditZona(zonas:dict):
    print('Ingrese el número de la zona que quiere editar') 
    nro = c.ValidZone(zonas)
    os.system('cls')
    if (bool(nro) == True):
        route = zonas.get(nro)
        lstRoute = list(route.keys())
        print('Ingrese el valor que desea editar')
        for item in lstRoute:
            print(f'----{item}----')
        isAct = True
        while isAct:
            op = input(')..').lower()
            if (op not in lstRoute):
                rp = bool(input('valor inválido, volver a intentar? --- S(Si) o Enter(No)'))
                if (rp == True):
                    pass
                else:
                    isAct = False
            elif(op in lstRoute and op == 'numero'):
                nValue = input(f'Ingrese el valor nuevo para {op}: ')
                zonas.pop(nro)
                zonas.update({nValue:route})
                zonas[nValue][op]=(nValue)
                isAct = False  
            elif(op in lstRoute):
                nValue = input(f'Ingrese el valor nuevo para {op}: ')
                zonas[nro][op]=(nValue)
    else:
        pass
    


    
def DltZona(zonas:dict):
    os.system('cls')
    print('ingrese el número de la zona que desea eliminar')
    nro = c.ValidZone(zonas)
    if (bool(nro) == True):
        zonas.pop(nro)
        print(f'Se ha eliminado la zona de código {nro}')
        os.system('pause')
    else:
        pass

def SrchZona(zonas:dict):
    os.system('cls')
    print('ingrese el número de la zona que desea buscar')
    nro = c.ValidZone(zonas)
    if (bool(nro) == True):
        route = zonas.get(nro)
        jsonNew = json.dumps(route, indent=4)
        print(f'Esta es la información correspondiente a la zona {nro}')
        print(jsonNew)
        os.system('pause')
    else:
        pass