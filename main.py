from termcolor import colored

from core.app import *
from helpers.menu import vista_menu


def main():
    n = 0
    if n < 1:
        lista_historial = []

    while True:
        vista_menu()
        eleccion = input(colored('\nElige una opción (0-6): ', 'yellow'))

        match eleccion:
            case '1':
                calculadora_simple(lista_historial)
                n += 1
            case '2':
                sumatoria_promedio(lista_historial)
                n += 1
            case'3':
                area_circulo(lista_historial)
                n += 1
            case '4':
                mayor_de_tres(lista_historial)
                n += 1
            case '5':
                anio_bisiesto(lista_historial)
                n += 1
            case '6':
                if (len(lista_historial) < 1):
                    limpiar_consola()
                    print(colored('Historial no disponible','light_red', attrs=[]))
                    volver_menu()
                else:
                    controlador_historial(lista_historial)
            case '0':
                print(colored('Saliendo de la aplicacion... \n  ¡Nos vemos!', 'light_cyan'))
                break
            case _:
                print('\n_Opción no válida, porfavor intente de nuevo.')


if __name__ == "__main__":
    main()
