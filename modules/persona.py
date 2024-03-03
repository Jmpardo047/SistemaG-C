import os
import modules.menus as m
import modules.corefiles as c
def Personas(personas : dict):
    os.system('cls')
    v = m.MenuControl()
    if (v == 1):
        Addpersona(personas)
    elif (v == 2):
        EditPersonas(personas)
    elif (v == 3):
        DelPerso(personas)
    elif (v == 4):  
        SerchPerso(personas)
    elif (v == 5):
        pass

def Addpersona(personas : dict):
    os.system('cls')
    listTipos = ['movil','casa','personal','oficina']
    print('Escriba el tipo de persona que es (natural (N) o juridica (J))')
    tipo = c.ValidStr().upper()
    if (tipo == 'N'):
        print('Ingrese el número de cedula de la persona')
        cc = str(c.validInt())
        print(f'Ingrese el nombre de {cc}')
        name = c.ValidStr()
        print(f'Ingrese el email de {name}')
        email = c.ValidStr()
        rol = Roles()
        nwPersona = {
            'cc' : cc,
            'name' :  name,
            'email': email,
            'telefono':{
                'movil': [],
                'casa' : [],
                'personal' : [],
                'oficina' : []
            },
            'rol': rol
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
        nit = str(c.validInt())
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



def EditPersonas(personas : dict):
    os.system('cls')
    rta = c.ValidPpl(personas)
    if (bool(rta) == True):
        codigo,tipoperso = rta
        if (codigo in personas[tipoperso]):
            print('Escoja el item que desea modificar')
            listitem = list(personas[tipoperso][codigo])
            print(listitem)
            change = c.ValidStr().lower()
            if (change not in listitem):
                print('Valor ingresado no coincide con ninguna opcion')
                rp = bool(input('Desea volver a intentar? --- S(Si) o Enter(No)'))
                if (rp == True):
                    return(EditPersonas(personas))
                else:
                    return(Personas(personas))
            else:
                if (change == 'telefono'):
                    listtelefonos = list(personas[tipoperso][codigo]['telefono'])
                    print(listtelefonos)
                    cambio = c.ValidStr().lower()
                    if (cambio not in listtelefonos):
                        print('Valor ingresado no coincide con ninguna opcion')
                        rp = bool(input('Desea volver a intentar? --- S(Si) o Enter(No)'))
                        if (rp == True):
                            return(EditPersonas(personas))
                        else:
                            return(Personas(personas))
                    else:
                        newtel = c.validInt()
                        personas[tipoperso][codigo][change][cambio] = newtel
                        print(F'El valor {cambio} ha sido actualizado correctamente, desea hacer otro?')
                        rp = bool(input('Desea hacer otro cambio? --- S(Si) o Enter(No)'))
                        if (rp == True):
                            return(EditPersonas(personas))
                        else:
                            return(Personas(personas))
                elif(change == 'nit'):
                        print(f'Seleccione el nuevo valor que le quiere dar a {change}')
                        newvalue = c.validInt()
                        personas[tipoperso][codigo][change] = newvalue
                        print(F'El valor {change} ha sido actualizado correctamente, desea hacer otro?')
                        rp = bool(input('Desea hacer otro cambio? --- S(Si) o Enter(No)'))
                        if (rp == True):
                            return(EditPersonas(personas))
                        else:
                            return(Personas(personas))
                elif (change == 'cc'):
                        print(f'Seleccione el nuevo valor que le quiere dar a {change}')
                        newvalue = c.validInt()
                        personas[tipoperso][codigo][change] = newvalue
                        print(F'El valor {change} ha sido actualizado correctamente, desea hacer otro?')
                        rp = bool(input('Desea hacer otro cambio? --- S(Si) o Enter(No)'))
                        if (rp == True):
                            return(EditPersonas(personas))
                        else:
                            return(Personas(personas))
                elif (change == 'name'):
                        print(f'Seleccione el nueo valor que le quiere dar a {change}')
                        newvalue = c.ValidStr()
                        personas[tipoperso][codigo][change] = newvalue
                        print(F'El valor {change} ha sido actualizado correctamente, desea hacer otro?')
                        rp = bool(input('Desea hacer otro cambio? --- S(Si) o Enter(No)'))
                        if (rp == True):
                            return(EditPersonas(personas))
                        else:
                            return(Personas(personas))
                elif (change == 'email'):
                        print(f'Seleccione el nuevo valor que le quiere dar a {change}')
                        newvalue = c.ValidStr()
                        personas[tipoperso][codigo][change] = newvalue
                        print(F'El valor {change} ha sido actualizado correctamente, desea hacer otro?')
                        rp = bool(input('Desea hacer otro cambio? --- S(Si) o Enter(No)'))
                        if (rp == True):
                            return(EditPersonas(personas))
                        else:
                            return(Personas(personas))
        else:
            print('No se encuentra el tipo de persona seleccioando')
            rp = bool(input('Desea volver a intentar? --- S(Si) o Enter(No)'))
            if (rp == True):
                return(EditPersonas(personas))
            else:
                return(Personas(personas))
    else:
        pass

def DelPerso (personas: dict):
    os.system('cls')
    rta = c.ValidPpl(personas)
    if (bool(rta) == True):
        codigo,tipoperso = rta
        print('Ingrese los valores a eliminar ')
        personas[tipoperso].pop(codigo)
        print('El dato ingresado fue eliminado correctamente')
        os.system('pause')
    else:
        pass

def SerchPerso (personas : dict):
    os.system('cls')
    rta = c.ValidPpl(personas)
    if (bool(rta) == True):
        codigo,tipoperso = rta
        print('Ingrese la informacion de la persona que quiere buscar')
        print(personas[tipoperso][codigo])
        os.system('pause')
    else:
        pass

def Roles():
    os.system('cls')
    print('Ingrese el rol que va a tener la persona')
    print('1. Persona\n2. Admin')
    n = input(')..')
    if (n == '1'):
        rol = 'persona'
        return rol
    elif (n == '2'):
        rol = 'admin'
        return rol
    else:
        print('opcion invalida, reintentar')
        os.system('pause')
        return Roles()