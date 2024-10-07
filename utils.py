import os


def limpiar_consola():
    # Para Windows
    if os.name == 'nt':
        os.system('cls')
    # Para Linux y macOS
    else:
        os.system('clear')


def vista_menu():
    print('\n--- Menú Calculadora ---')
    print('1. Calculadora Simple')
    print('2. Calcular promedio')
    print('3. Calcular área de un círculo')
    print('4. Comprobar el Mayor de 3 n°')
    print('5. Comprobar Año bisiesto')
    print('6. Historial')
    print('0. Salir')


def vista_menu_historial():
    print('\n--- Menú Historial ---')
    print('1. Ver Historial')
    print('2. Editar Historial')
    print('3. Borar Entrada del Historial')
    print('0. Volver')


def volver_menu():
    input('\nPresione "Enter" para continuar...')
    return limpiar_consola()
