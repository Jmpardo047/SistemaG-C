import os
import modules.menus as m
import modules.corefiles as c
import json
def Asign(asignaciones:dict,zonas:dict,personas:dict,activos:dict):
    os.system('cls')
    n = m.MenuAsignacion()
    if (n == 1):
        os.system('cls')
        CreateAsign(asignaciones,zonas,personas,activos)
    elif (n == 2):
        os.system('cls')
        ScrhAsign(asignaciones)   
    elif (n == 3):
        pass

def CreateAsign(asignaciones:dict,zonas:dict,personas:dict,activos:dict):
    os.system('cls')
    lstAsign = []
    print('Ingrese la fecha de la asignación')
    date = c.ValidStr()
    print('Ingrese el id de quién va a realizar la asignación')
    tipo = c.ValidStr()
    IsValid = verifyPerm(personas,tipo)
    if (IsValid == True):
        print('seleccione el número del tipo de asignación que desea hacer')
        print('1. Personal\n2. Zona')
        n = c.ValidStr()
        if (n == '1'):
            os.system('cls')
            tipo = 'personal'
            rta = c.ValidPpl(personas)
            if (bool(rta) == True):
                codigo,tipoperso = rta
                rp = True
                route = asignaciones.get(codigo)
                if (bool(route) == True):
                    lstAsign = AddAct(activos,lstAsign,date,tipo) 
                    actLst = list(route['activos'])
                    for item in lstAsign:
                        if item in actLst:
                            pass
                        else:
                            actLst.append(item)
                    route['activos'] = actLst
                    route['fecha'] = date
                elif (bool(route) == False):
                    lstAsign = AddAct(activos,lstAsign,date,tipo)
                    nroAsg = str(len(asignaciones)+1).zfill(3)
                    nwAsign = {
                        'nro asignacion':nroAsg,
                        'fecha':date,
                        'tipo asignacion':tipo,
                        'asignadoA':codigo,
                        'activos': lstAsign
                    }
                    asignaciones.update({codigo:nwAsign})
            else:
                pass
        elif (n == '2'):
            os.system('cls')
            tipo = 'zona'
            print('ingrese el número de la zona a la que desea asignarle un activo')
            nro = c.ValidZone(zonas)
            if (bool(nro) == True):
                route = asignaciones.get(nro)
                if (bool(route) == True):
                    lstAsign = AddAct(activos,lstAsign,date,tipo) 
                    actLst = list(route['activos'])
                    for item in lstAsign:
                        if item in actLst:
                            pass
                        else:
                            actLst.append(item)
                    route['activos'] = actLst
                    route['fecha'] = date
                elif (bool(route) == False):
                    lstAsign = AddAct(activos,lstAsign,date,tipo)
                    nroAsg = str(len(asignaciones)+1).zfill(3)
                    nwAsign = {
                        'nro asignacion':nroAsg,
                        'fecha':date,
                        'tipo asignacion':tipo,
                        'asignadoA':nro,
                        'activos': lstAsign
                    }
                    asignaciones.update({nro:nwAsign})
            else:
                pass
        else:
            print('digito inválido')
            os.system('pause')
            CreateAsign(asignaciones,zonas,personas,activos)
    else:
        pass

def ScrhAsign(asignaciones:dict):
    os.system('cls')
    print('ingrese el número de la asignación que quiere consultar')
    nro = c.ValidStr()
    if (nro in asignaciones.keys()):
        route = asignaciones.get(nro)
        printRoute = json.dumps(route,indent=4)
        print(printRoute)
        os.system('pause')
    else:
        rp = bool(input('Número de asignación no encontrado, desea volver a intentar? S(Si) - Enter(No)'))
        if (rp == True):
            ScrhAsign(asignaciones)
        else:
            pass

def AddAct(activos:dict,lstAsign:list,date,tipo):
    rp = True
    while rp:
        print('Ingrese el código campus del activo que desea asignar')
        code = c.ValidataCode(activos)
        
        if (bool(code) == True):
            if (code in lstAsign):
                print('Este código ya esta en la lista de asignaciones')
            elif (activos[code]['estado'] == 'en reparacion'):
                print('este activo no puede ser asignado ya que esta en reparación')
            elif (activos[code]['estado'] == 'dado de baja'):
                print('este activo no puede ser asignado ya que esta dado de baja por daños')
            elif (activos[code]['estado'] == 'asignado'):
                print('este activo ya ha sido asignado previamente')
            elif (activos[code]['estado'] == 'no asignado'):
                activos[code]['estado'] = 'asignado'
                AddHist(activos,'asignado',code,date,tipo)
                lstAsign.append(code)
        else:
            print('Código no encontrado')
        rp = bool(input('desea agregar otro activo? S(Si) o Enter(No)'))
    return lstAsign

def AddHist(activos:dict,mov,code,date,tipo):
    route = activos.get(code)['historial']
    idHist = str(len(route)+1).zfill(3)
    nwHist = {
        'NroID':idHist,
        'fecha': date,
        'tipoMov': mov,
        'responsable': tipo
    }
    route.update({idHist:nwHist})


def verifyPerm(personas:dict,tipo):
    line = personas.get('personasn')
    route = line.get(tipo)
    if (bool(route) == True):
        if (route['rol'] == 'admin'):
            return True
        elif (route['rol'] == 'persona'):
            print('Este usuario no tiene permisos de administrador')
            os.system('pause')
            return False
    else:
        print('Usuario no encontrado')
        os.system('pause')
        return False