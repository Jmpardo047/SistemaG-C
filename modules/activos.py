import os
import modules.menus as m
import modules.corefiles as c
from tabulate import tabulate
def Activos(activos:dict):
    os.system('cls')
    n = m.MenuControl()
    if (n == 1):
        os.system('cls')
        AddActivo(activos)
    elif (n == 2):
        os.system('cls')
        EditActivo(activos)
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
    print('Ingrese el número de formulario')
    nroForm = c.validInt()
    print('Ingrese el código campus')
    codCampus = c.validInt()
    print('Ingrese la marca del activo')
    brand = c.ValidStr()
    print('Ingrese la Categoria del activo')
    cat = c.ValidStr()
    print('Ingrese el tipo del activo')
    tipo = c.ValidStr()
    print('Ingrese el valor del activo')
    val = c.validFloat()
    print('Ingrese el proveedor del activo')
    prov = c.ValidStr()
    print('Ingrese el número serial del activo')
    nroSerial = c.validInt()
    print('Ingrese la empresa responsable del activo')    
    empresa = c.ValidStr()
    nwAct = {
        'codtransaccion': codTrans,
        'nroformulario': nroForm,
        'codecampus': codCampus,
        'nombre': name,
        'marca': brand,
        'categoria': cat,
        'tipo': tipo,
        'valor': val,
        'proovdeor': prov,
        'nroserial': nroSerial,
        'empresa': empresa,
        'estado': 'no asignado',
        'historial': {}
    }
    activos.update({str(codCampus):nwAct})

def ValidataCode(activos:dict):
    cod = input(')..')
    if (cod not in activos.keys()):
        print('Código ingresado no coincide con ningún activo')
        rp = bool(input('Desea volver a intentar? --- S(Si) o Enter(No)'))
        if (rp == True):
            return(ValidataCode(activos))
        else:
            pass
    else:
        return cod



def EditActivo(activos:dict):
    os.system('cls')
    print('ingrese el código campus del activo que desea editar')
    cCampus = ValidataCode(activos)
    if (bool(cCampus) == True):
        route = activos.get(cCampus)
        lstoute = list(route.keys())
        print('Ingrese el valor que desea editar (No es posible editar el CodCampus, el estado o el historial')
        for item in lstoute:
            if (item == 'codecampus' or item == 'estado' or item == 'historial'):
                pass
            else:
                print(f'----{item}----')
        isAct = True
        while isAct:
            op = input(')..').lower()
            if (op not in lstoute or op == 'codecampus' or op =='estado' or op =='historial'):
                rp = bool(input('valor inválido, volver a intentar? --- S(Si) o Enter(No)'))
                if (rp == True):
                    pass
                else:
                    isAct = False
            elif(op in lstoute):
                nValue = input(f'Ingrese el valor nuevo para {op}: ')
                activos[cCampus][op]=(nValue)
                isAct = False


        
