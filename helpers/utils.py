from termcolor import colored


import os


def limpiar_consola():
    # Para Windows
    if os.name == 'nt':
        os.system('cls')
    # Para Linux y macOS
    else:
        os.system('clear')


def volver_menu():
    txt_verde = colored('"Enter"', 'light_green')
    txt1_azul =colored(f'Presione', 'light_blue')
    txt2_azul = colored(f'para continuar...', 'light_blue')
    input(f'\n{txt1_azul} {txt_verde} {txt2_azul}')
    return
