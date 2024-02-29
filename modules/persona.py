import os
import modules.menus as m
import modules.corefiles as c
def Personas(personas : dict):
    os.system('cls')
    v = m.MenuControl()
    if (v == 1):
        Addpersona(personas)
    elif (v == 2):
        editpersonas(personas)
    elif (v == 3):
        pass
    elif (v == 4):  
        pass
    elif (v == 5):
        pass

def Addpersona(personas : dict):
    os.system('cls')
    listTipos = ['movil','casa','personal','oficina']
    print('Escriba el tipo de persona que es (natural (N) o juridica (J))')
    tipo = c.ValidStr().upper()
    if (tipo == 'N'):
        print('Ingrese el número de cedula de la persona')
        cc = c.validInt()
        print(f'Ingrese el nombre de {cc}')
        name = c.ValidStr()
        print(f'Ingrese el email de {name}')
        email = c.ValidStr()
        nwPersona = {
            'cc' : cc,
            'name' :  name,
            'email': email,
            'telefono':{
                'movil': [],
                'casa' : [],
                'personal' : [],
                'oficina' : []
            }
        }
        add = bool(input(f'Desea agregar un telefono al registro de {name}? S(Si) Enter(No)'))
        if (add == True):
            isactive = True
            while isactive:
                print('Que tipo telefono quiere agregar')
                print(listTipos)
                tipo = c.ValidStr().lower()
                if (tipo in listTipos):
                    print('Escriba el numuero de telefono que desea agregar')
                    tel = c.validInt()
                    nwPersona['telefono'][tipo].append(tel)
                    rt = bool(input('Desea agregar otro telefono? S(Si) Enter(No)'))
                    if (rt == True):
                        isactive = True
                    elif(rt == False):
                        isactive = False
                        personas['personasn'].update({cc:nwPersona})
                    else:
                        isactive = False
                        print('Opcion escrita no es correcta, no se agregó ningun registro al sistema de personas')
                        os.system('pause')
                        return
                else:
                    print('No se pudo encontrar el tipo de telefono, vuelvalo a intentar')
                    isactive = True            
        personas['personasn'].update({cc:nwPersona})
        os.system('pause')
        return
    elif (tipo == 'J'):
        print('Ingrese el numuero NIT del usuario')
        nit = c.validInt()
        print(f'Ingrese el nombre del usuario {nit}')
        name = c.ValidStr()
        print(f'Ingrese el email de {name}')
        email = c.ValidStr()
        nwPersona = {
            'nit' : nit,
            'name' :  name,
            'email': email,
            'telefono':{
                'movil': [],
                'casa' : [],
                'personal' : [],
                'oficina' : []
            }
        }
        add = bool(input(f'Desea agregar un telefono al registro de {name}? S(Si) Enter(No)'))
        if (add == True):
            isactive = True
            while isactive:
                print('Que tipo telefono quiere agregar')
                print(listTipos)
                tipo = c.ValidStr().lower()
                if (tipo in listTipos):
                    print('Escriba el número de telefono que desea agregar')
                    tel = c.validInt()
                    nwPersona['telefono'][tipo].append(tel)
                    rt = bool(input('Desea agregar otro telefono? S(Si) Enter(No)'))
                    if (rt == True):
                        isactive = True
                    elif(rt == False):
                        isactive = False
                        personas['personasj'].update({nit:nwPersona})
                    else:
                        isactive = False
                        print('Opcion escrita no es correcta, no se agregó ninugn registro al sistema de personas')
                        os.system('pause')
                        return
                else:
                    print('No se pudo encontrar el tipo de telefono, vuelvalo a intentar')
                    isactive = True            
        personas['personasj'].update({nit:nwPersona})
        os.system('pause')
        return
    else:
        print('El tipo de persona seleccionado no es valido')
        os.system('pause')
        Addpersona(personas)

def validatecode(personas : dict):
    print('Ingrese el tipo de persona donde desea buscar su codigo')
    listtipo = list(personas.keys())
    print(listtipo)
    tipoperso = c.ValidStr().lower()
    if (tipoperso in listtipo):
        print('Ingrese el codigo de la persona')
        code = input(':)_')
        if (code not in personas[tipoperso]):
            print('Código ingresado no coincide con ningún activo')
            rp = bool(input('Desea volver a intentar? --- S(Si) o Enter(No)'))
            if (rp == True):
                return(validatecode(personas))
            else:
                pass
        else:
            return code
    else:
        print('Tipo de persona seleccionada no encontrada')
        rp = bool(input('Desea volver a intentar? --- S(Si) o Enter(No)'))
        if (rp == True):
            return(validatecode(personas))
        else:
                pass

def editpersonas(personas : dict):
    os.system('cls')
    codigo = validatecode(personas)
    print('Ingrese el tipo de persona donde desea hacer los cambios')
    listtipo = list(personas.keys())
    print(listtipo)
    tipoperso = c.ValidStr().lower()
    if (codigo in personas[tipoperso]):
        print('Escoja el item que desea modificar')
        listitem = list(personas[tipoperso][codigo])
        print(listitem)
        change = c.ValidStr().lower()
        if (change not in listitem):
            print('Valor ingresado no coincide con ninguna opcion')
            rp = bool(input('Desea volver a intentar? --- S(Si) o Enter(No)'))
            if (rp == True):
                return(editpersonas(personas))
            else:
                pass
        else:
            if (change == 'telefono'):
                listtelefonos = list(personas[tipoperso][codigo]['telefono'])
                print(listtelefonos)
                cambio = c.ValidStr().lower()
                if (cambio not in listtelefonos):
                    print('Valor ingresado no coincide con ninguna opcion')
                    rp = bool(input('Desea volver a intentar? --- S(Si) o Enter(No)'))
                    if (rp == True):
                        return(editpersonas(personas))
                    else:
                        pass
                else:
                    newtel = c.validInt()
                    personas[tipoperso][codigo][change][cambio] = newtel
                    print(F'El valor {cambio} ha sido actualizado correctamente, desea hacer otro?')
                    rp = bool(input('Desea hacer otro cambio? --- S(Si) o Enter(No)'))
                    if (rp == True):
                        return(editpersonas(personas))
                    else:
                        pass
            else:
                print(f'Seleccione el nuevo valor que le quiere dar a {change}')
                newvalue = input(':)_ ')
                personas[tipoperso][codigo][change] = newvalue
                print(F'El valor {change} ha sido actualizado correctamente, desea hacer otro?')
                rp = bool(input('Desea hacer otro cambio? --- S(Si) o Enter(No)'))
                if (rp == True):
                    return(editpersonas(personas))
                else:
                    pass
    else:
        print('No se encuentra el tipo de persona seleccioando')
        rp = bool(input('Desea volver a intentar? --- S(Si) o Enter(No)'))
        if (rp == True):
            return(editpersonas(personas))
        else:
            pass