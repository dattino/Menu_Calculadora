from helpers.utils import limpiar_consola, volver_menu
from helpers.menu import ver_menu_historial
from helpers.file_helpers import write_json_file
from config import constants


from termcolor import colored


def controlador_historial(historial):
    while True:
        ver_menu_historial()
        eleccion = input(colored('\nElige una opción (0-3): ', 'yellow'))
        match eleccion:
            case '1':
                consultar_historial(historial)
            case '2':
                consultar_historial(historial)
                editar_historial(historial)
            case'3':
                consultar_historial(historial)
                borrar_historial(historial)
            case '0':
                break
            case _:
                print(
                    colored('\n_Opción no válida, porfavor intente de nuevo.', 'light_red'))


def consultar_historial(historial) -> list:
    limpiar_consola()
    if not historial:
        print(colored('Historial no disponible', 'light_red'))
        volver_menu()
        return
    print(colored('\n--- Historial ---\n', 'light_blue', attrs=['bold']))
    for index, entrada in enumerate(historial, start=1):
        estado_editado = '✔️' if (entrada['editado']) else '❌'
        print(colored(f'{index}. {
              entrada['nombre']} - Editado: {estado_editado}', 'dark_grey'))
        print(colored(f'   Operacion: {entrada['operacion']}', 'grey'))
    return volver_menu()


def agregar_historial(historial, nombre_aplicacion: str, resultado_almacenar: str) -> list:
    funcion = nombre_aplicacion
    descripcion = resultado_almacenar
    entrada = {
        'nombre': funcion,
        'operacion': descripcion,
        'editado': False,
    }
    historial.append(entrada)
    write_json_file(constants.HISTORIAL_PATH, historial)
    print(colored(f'Entrada {funcion} agregada al historial', 'green'))
    return volver_menu()


def editar_historial(historial):
    if (len(historial) > 0):
        try:
            index = int(
                input('Ingrece el índice a editar o 0 para salir: ')) - 1
            if (index == -1):
                return
            elif (index < 0 or index >= len(historial)):
                print(colored('Indice no disponible.', 'light_magenta'))
                editar_historial(historial)
                return
            else:
                entrada = historial[index]
                entrada['nombre'] = input(
                    f'Ingrese el nuevo nombre (actual: {entrada['nombre']}): ') or entrada['nombre']
                entrada['operacion'] = input(
                    f'Ingrese la nueva operación (actual: {entrada['operacion']}): ') or entrada['operacion']
                entrada['editado'] = True
                write_json_file(constants.HISTORIAL_PATH, historial)
                print(
                    colored(f'"{entrada['nombre']}" actualizada correctamente.', 'light_green'))
                return volver_menu()
        except ValueError:
            print(colored('Entrada errónea, porfavor ingrese un número.',
                  'light_red', attrs=['bold']))
            editar_historial(historial)
        return
    else:
        pass


def borrar_historial(historial):
    if (len(historial) > 0):
        try:
            index = int(
                input('Ingrece el índice a editar o 0 para salir: ')) - 1
            if (index == -1):
                return
            elif (index < 0 or index >= len(historial)):
                print(colored('Indice no disponible.', 'light_magenta'))
                borrar_historial(historial)
                return
            borrar_entrada = historial.pop(index)
            write_json_file(constants.HISTORIAL_PATH, historial)
            print(colored(f'Entrada "{
                  borrar_entrada['nombre']}" borrada correctamente.', on_color='on_red'))
            volver_menu()
        except ValueError:
            print(colored('Entrada errónea, porfavor ingrese un número.',
                  'light_red', attrs=['bold']))
            borrar_historial(historial)
        return
    else:
        pass
