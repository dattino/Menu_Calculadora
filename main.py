from termcolor import colored


from core.app import *
from helpers.menu import ver_menu, limpiar_consola
from helpers.file_helpers import read_json_file
from config import constants


def main():
    lista_historial = read_json_file(constants.HISTORIAL_PATH)
    print(f'{lista_historial}')
    while True:
        ver_menu()
        eleccion = input(colored('\nElige una opción (0-6): ', 'yellow'))
        match eleccion:
            case '1':
                limpiar_consola()
                calcular_operaciones_simple(lista_historial)
            case '2':
                limpiar_consola()
                calcular_sumatoria_promedio(lista_historial)
            case'3':
                limpiar_consola()
                calcular_area_circulo(lista_historial)
            case '4':
                limpiar_consola()
                calcular_mayor_de_tres(lista_historial)
            case '5':
                limpiar_consola()
                verificar_anio_bisiesto(lista_historial)
            case '6':
                if (len(lista_historial) < 1):
                    limpiar_consola()
                    print(colored('Historial no disponible', 'light_red', attrs=[]))
                    volver_menu()
                else:
                    controlador_historial(lista_historial)
            case '0':
                print(
                    colored('Saliendo de la aplicacion... \n  ¡Nos vemos!', 'light_cyan'))
                break
            case _:
                print('\n_Opción no válida, porfavor intente de nuevo.')


if __name__ == "__main__":
    main()
