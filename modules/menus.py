import sys
from tabulate import tabulate
import os
import modules.corefiles as core
import modules.activos as act
import modules.persona as per
import modules.persona as prs
campus = core.VerifyEx()
activos,personas,zonas,asignaciones = campus.values()
def MainMenu():
    def Excecute(func):
        os.system('cls')
        func
        MainMenu()

    titulo = '''
    *****************************************
    * SISTEMA G&C DE INVENTARIO CAMPUSLANDS *
    *****************************************
    '''
    print(titulo)
    menu =[['1.', 'Activos'], ['2.', 'Personal'], ['3.', 'Zonas'], ['4.', 'Asignación de Activos'], ['5.', 'Reportes'], ['6.', 'Movimiento Activos'], ['7.', 'Salir']]
    print(tabulate(menu, tablefmt='grid'))
    op = input('\n)..'  )
    if op == '1':
       Excecute(act.Activos(activos))
    elif op == '2':
        Excecute(per.Personas(personas))
    elif op == '3':
        pass
    elif op == '4':
        pass
    elif op == '5':
        pass
    elif op == '6':
        pass
    elif op == '7':
        finalUpt = {
            'activos':activos,
            'personas':personas,
            'zonas': zonas,
            'asignaciones':asignaciones
        }
        core.UpdateFile('campus.json',finalUpt)
        sys.exit('Vuelva pronto!')
    else:
        MainMenu()

def MenuControl():
    lstOp = (1,2,3,4,5)
    menu =[['1.', 'Agregar'], ['2.', 'Editar'], ['3.', 'Eliminar'], ['4.', 'Buscar'], ['5.', 'Regresar al menu principal']]
    print(tabulate(menu, tablefmt='grid'))
    try:
        op = int(input('\n)..'  ))
        if (op not in lstOp):
            MenuControl()
    except ValueError:
        MenuControl()
    else:
        return op