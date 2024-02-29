import os
import modules.menus as m
import modules.corefiles as c
def Asign(asignaciones:dict,zonas:dict,personas:dict,activos:dict):
    os.system('cls')
    n = m.MenuAsignacion()
    if (n == 1):
        os.system('cls')
        CreateAsign(asignaciones,zonas,personas,activos)
    elif (n == 2):
        os.system('cls')
        pass
    elif (n == 3):
        pass

def CreateAsign(asignaciones:dict,zonas:dict,personas:dict,activos:dict):
    os.system('cls')
    lstAsign = []
    print('Ingrese la fecha de la asignación')
    date = c.ValidStr()
    print('seleccione el número del tipo de asignación que desea hacer')
    print('1. Personal\n2. Zona')
    n = c.ValidStr()
    if (n == '1'):
        os.system('cls')
        tipo = 'personal'
    elif (n == '2'):
        os.system('cls')
        tipo = 'zona'
        print('ingrese el número de la zona a la que desea asignarle un activo')
        nro = c.ValidZone(zonas)
        rp = True
        while rp:
            print('Ingrese el código campus del activo que desea asignar')
            code = c.ValidataCode(activos)
            if (code in lstAsign):
                print('Este código ya esta en la lista de asignaciones')
            elif (activos[code]['estado'] == 'en reparacion'):
                print('este activo no puede ser asignado ya que esta en reparación')
            elif (activos[code]['estado'] == 'dado de baja'):
                print('este activo no puede ser asignado ya que esta dado de baja por daños')
            elif (activos[code]['estado'] == 'asignado'):
                print('este activo ya ha sido asignado previamente')
            elif (activos[code]['estado'] == 'no asignado'):
                lstAsign.append(code)
            rp = bool(input('desea agregar otro activo? S(Si) o Enter(No)'))
        nroAsg = str(len(asignaciones)+1).zfill(3)
        nwAsign = {
            'nro asignacion':nroAsg,
            'fecha':date,
            'tipo asignacion':tipo,
            'asignadoA':nro,
            'activos': lstAsign
        }
        asignaciones.update({nroAsg:nwAsign})

    else:
        print('digito inválido')
        os.system('pause')
        CreateAsign(asignaciones,zonas,personas,activos)