from termcolor import colored

from core.app import *
from helpers.menu import ver_menu
from helpers.utils import limpiar_consola, volver_menu
from controller.historial_controller import HistorialController


def main():
    while True:
        limpiar_consola()
        HistorialController.ver()
        ver_menu()
        eleccion = input(
            colored('\nElige una opción (0-6): ', 'yellow')
        )
        match eleccion:
            case '1':
                limpiar_consola()
                calcular_operaciones_simple()
                volver_menu()
            case '2':
                limpiar_consola()
                calcular_sumatoria_promedio()
                volver_menu()
            case'3':
                limpiar_consola()
                calcular_area_circulo()
                volver_menu()
            case '4':
                limpiar_consola()
                calcular_mayor_de_tres()
                volver_menu()
            case '5':
                limpiar_consola()
                verificar_anio_bisiesto()
                volver_menu()
            case '6':
                limpiar_consola()
                HistorialController.inicio()
            case '0':
                print(
                    colored(
                        'Saliendo de la aplicacion... \n  ¡Nos vemos!', 'light_cyan'
                    )
                )
                break
            case _:
                print(
                    colored('\n Opción no válida, porfavor intente de nuevo.',
                            'light_red', attrs=['bold']
                            )
                )
                volver_menu()


if __name__ == "__main__":
    main()
