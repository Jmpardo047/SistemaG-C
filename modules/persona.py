import os
import modules.menus as m
import modules.corefiles as c
def Personas(personas : dict):
    os.system('cls')
    v = m.MenuControl()
    if (v == 1):
        Addpersona(personas)
    elif (v == 2):
        pass
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
