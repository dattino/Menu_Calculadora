from termcolor import colored


def ver_menu():
    print(
        colored('\nMenú Calculadora:\n', 'blue', attrs=['bold', 'underline'])
    )
    print(
        colored('1. Calculadora Simple', 'light_green')
    )
    print(
        colored('2. Calcular promedio', 'light_green')
    )
    print(
        colored('3. Calcular área de un círculo', 'light_green')
    )
    print(
        colored('4. Comprobar el Mayor de 3 n°', 'light_green')
    )
    print(
        colored('5. Comprobar Año bisiesto', 'light_green')
    )
    print(
        colored('6. Menú Historial', 'light_green', attrs=['bold'])
    )
    print(
        colored('0. Salir', 'red')
    )


def ver_menu_historial():
    print(
        colored('\n--- Menú Historial ---\n', 'blue', attrs=['bold', 'underline']))
    print(
        colored('1. Ver Historial', 'light_green'))
    print(
        colored('2. Editar Historial', 'light_green'))
    print(
        colored('3. Borar Entrada del Historial', 'light_green'))
    print(
        colored('0. Volver', 'red'))
