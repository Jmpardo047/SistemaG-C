import os
import modules.menus as m
import modules.corefiles as c
def menpersonas(personas : dict):
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
    listtipos = ['movil','casa','personal','oficina']
    print('Bienvenido al sistema de añadir personas')
    print('Escriba el tipo de persona que es (natural (N) o juridica (J))')
    tipo = c.ValidStr().upper()
    if (tipo == 'N'):
        print('Ingrese el numuero de cedula de la persona')
        cc = c.validInt()
        print(f'Ingrese el nombre de {cc}')
        name = c.ValidStr()
        print(f'Ingrese el email de {name}')
        email = c.ValidStr()
        persona = {
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
        print(f'Desea agregar un telefono al registro de {name}? S(si) N(no)')
        add = c.ValidStr().upper()
        if (add == 'S'):
            isactive = True
            while isactive:
                print('Que tipo telefono quiere agregar')
                print(listtipos)
                tipo = c.ValidStr().lower()
                if (tipo in listtipos):
                    print('Escriba el numuero de telefono que desea agregar')
                    tel = c.validInt()
                    persona['telefono'][tipo].append(tel)
                    print('Desea agregar otro telefono? Si (S) No (N)')
                    rete = c.ValidStr().upper()
                    if (rete == 'S'):
                        isactive = True
                    elif(rete == 'N'):
                        isactive = False
                        personas['personasn'].update({cc:persona})
                    else:
                        isactive = False
                        print('Opcion escrita no es correcta, no se agregó ninugn registro al sistema de personas')
                        os.system('pause')
                        return
                else:
                    print('No se pudo encontrar el tipo de telefono, vuelvalo a intentar')
                    isactive = True            
        elif (add == 'N'):
            personas['personasn'].update({cc:persona})
            print(f'La persona {name} ha sido agregada correctamente')
            os.system('pause')
            return
        else:
            print('opcion ingresada no valida')
            os.system('pause')
            Addpersona(personas)
    elif (tipo == 'J'):
        print('Ingrese el numuero NIT del usuario')
        nit = c.validInt()
        print(f'Ingrese el nombre del usuario {nit}')
        name = c.ValidStr()
        print(f'Ingrese el email de {name}')
        email = c.ValidStr()
        persona = {
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
        print(f'Desea agregar un telefono al registro de {name}? S(si) N(no)')
        add = c.ValidStr().upper()
        if (add == 'S'):
            isactive = True
            while isactive:
                print('Que tipo telefono quiere agregar')
                print(listtipos)
                tipo = c.ValidStr().lower()
                if (tipo in listtipos):
                    print('Escriba el numuero de telefono que desea agregar')
                    tel = c.validInt()
                    persona['telefono'][tipo].append(tel)
                    print('Desea agregar otro telefono? Si (S) No (N)')
                    rete = c.ValidStr().upper()
                    if (rete == 'S'):
                        isactive = True
                    elif(rete == 'N'):
                        isactive = False
                        personas['personasj'].update({nit:persona})
                    else:
                        isactive = False
                        print('Opcion escrita no es correcta, no se agregó ninugn registro al sistema de personas')
                        os.system('pause')
                        return
                else:
                    print('No se pudo encontrar el tipo de telefono, vuelvalo a intentar')
                    isactive = True            
        elif (add == 'N'):
            personas['personasj'].update({cc:persona})
            print(f'La persona {name} ha sido agregada correctamente')
            os.system('pause')
            return
        else:
            print('opcion ingresada no valida')
            os.system('pause')
            Addpersona(personas)
    else:
        print('El tipo de persona seleccionado no es valido')
        os.system('pause')
        Addpersona(personas)
