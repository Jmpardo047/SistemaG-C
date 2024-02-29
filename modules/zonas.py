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
    nro = ValidataCode(zonas)
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
            elif(op in lstRoute):
                nValue = input(f'Ingrese el valor nuevo para {op}: ')
                zonas[nro][op]=(nValue)
                isAct = False  
    else:
        pass
    

def ValidataCode(zonas:dict):
    cod = input(')..')
    if (cod not in zonas.keys()):
        print('Nùmero ingresado no coincide con ninguna zona')
        rp = bool(input('Desea volver a intentar? --- S(Si) o Enter(No)'))
        if (rp == True):
            return(ValidataCode(zonas))
        else:
            pass
    else:
        return cod
    
def DltZona(zonas:dict):
    os.system('cls')
    print('ingrese el código campus del activo que desea eliminar')
    nro = ValidataCode(zonas)
    if (bool(nro) == True):
        zonas.pop(nro)
        print(f'Se ha eliminado el activo de código {nro}')
        os.system('pause')
    else:
        pass

def SrchZona(zonas:dict):
    os.system('cls')
    print('ingrese el código campus del activo que desea buscar')
    nro = ValidataCode(zonas)
    if (bool(nro) == True):
        route = zonas.get(nro)
        jsonNew = json.dumps(route, indent=4)
        print(f'Esta es la información correspondiente al activo {nro}')
        print(jsonNew)
        os.system('pause')
    else:
        pass