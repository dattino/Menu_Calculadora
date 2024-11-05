from termcolor import colored


from helpers.utils import limpiar_consola


def ver_menu():
    limpiar_consola()
    print(colored('\nMenú Calculadora:\n',
          'blue', attrs=['bold', 'underline',]))
    print(colored('1. Calculadora Simple', 'light_green'))
    print(colored('2. Calcular promedio', 'light_green'))
    print(colored('3. Calcular área de un círculo', 'light_green'))
    print(colored('4. Comprobar el Mayor de 3 n°', 'light_green'))
    print(colored('5. Comprobar Año bisiesto', 'light_green'))
    print(colored('6. Historial', 'light_green'))
    print(colored('0. Salir', 'red'))


def ver_menu_historial():
    limpiar_consola()
    print(colored('\n--- Menú Historial ---\n', 'blue', attrs=['bold',]))
    print(colored('1. Ver Historial', 'light_green'))
    print(colored('2. Editar Historial', 'light_green'))
    print(colored('3. Borar Entrada del Historial', 'light_green'))
    print(colored('0. Volver', 'red'))
