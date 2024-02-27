import sys
from tabulate import tabulate
import os
def MainMenu():
    def Excecute(func):
        os.system('cls')
        func()
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
       pass
    elif op == '2':
        pass
    elif op == '3':
        pass
    elif op == '4':
        pass
    elif op == '5':
        pass
    elif op == '6':
        pass
    elif op == '7':
        sys.exit('Vuelva pronto!')
    else:
        MainMenu()